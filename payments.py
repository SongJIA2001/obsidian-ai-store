"""支付宝 / 微信支付官方直连 + 易支付聚合集成。

- 支付宝电脑网站支付（alipay.trade.page.pay）：RSA2 签名生成跳转 URL；
  异步通知用支付宝公钥验签，并校验 app_id 与金额后才允许改单状态。
- 微信支付 API v3 Native 支付：商户私钥 RSA 签名请求，拿到 code_url 供
  前端展示二维码；异步通知先用微信支付平台证书验签，再用 API v3 密钥
  AES-256-GCM 解密，并校验商户号与金额后才允许改单状态。
- 易支付（彩虹易支付兼容协议）：MD5 签名跳转 {网关}/submit.php；
  异步通知（GET）验签后校验 trade_status 与金额才允许改单状态；
  另有主动查单兜底（api.php act=order），本机直连网关不通时可
  配置 EPAY_RELAY_URL / EPAY_RELAY_TOKEN 改走中继转发查单。
  签名只用标准库 hashlib，不依赖 cryptography；商户密钥 KEY 只从
  配置读取，不写日志、不返回给上层页面。

缺少任何必需参数时，configured() 返回 False，上层页面会如实提示
“支付参数未配置”，订单保持待支付——本模块从不伪造支付成功。
官方直连的签名/验签依赖 `cryptography` 包（见 requirements.txt）；
未安装时官方直连的 configured() 返回 False 并给出原因（不影响易支付）。
"""
import base64
import hashlib
import json
import os
import secrets
import time
import urllib.parse
import urllib.request
from decimal import Decimal, InvalidOperation

import config

try:
    from cryptography.exceptions import InvalidSignature
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    from cryptography.x509 import load_pem_x509_certificate
    _CRYPTO_OK = True
except Exception:  # pragma: no cover - cryptography 未安装时降级
    _CRYPTO_OK = False


class PaymentNotConfigured(Exception):
    """支付参数不全 / 支付组件不可用。"""


class PaymentError(Exception):
    """支付网关调用或验签失败。"""


def amount_equal(money, amount_cents):
    """金额数值比较：网关金额（字符串，如 "5"、"5.0"、"5.00"，单位元）
    与订单金额（分）数值相等才返回 True；为空或无法解析一律 False。

    不同网关对金额的格式化不一致（有的发 "5" 有的发 "5.00"），不能用
    字符串等值比较，必须按数值比。
    """
    if money is None:
        return False
    try:
        return Decimal(str(money).strip()) == \
            Decimal(amount_cents) / Decimal(100)
    except (InvalidOperation, ValueError, ArithmeticError):
        return False


# ---------------------------------------------------------------- 通用

def _load_private_key(path):
    if not path or not os.path.exists(path):
        raise PaymentNotConfigured(f"私钥文件不存在：{path or '(未配置)'}")
    with open(path, "rb") as f:
        data = f.read()
    try:
        return serialization.load_pem_private_key(data, password=None)
    except ValueError:
        # 尝试 PKCS8 之外的传统格式由 load_pem_private_key 已覆盖；
        # 若文件是支付宝工具生成的 PKCS1 也可被上面的接口解析。
        raise PaymentError("私钥文件解析失败，请确认是 PEM 格式且无密码")


def _load_public_key_from_pem(path, is_cert=False):
    if not path or not os.path.exists(path):
        raise PaymentNotConfigured(f"公钥/证书文件不存在：{path or '(未配置)'}")
    with open(path, "rb") as f:
        data = f.read()
    if is_cert or b"BEGIN CERTIFICATE" in data:
        return load_pem_x509_certificate(data).public_key()
    return serialization.load_pem_public_key(data)


def _rsa_sign(private_key, message_bytes):
    return private_key.sign(
        message_bytes, padding.PKCS1v15(), hashes.SHA256())


def _rsa_verify(public_key, signature, message_bytes):
    public_key.verify(
        signature, message_bytes, padding.PKCS1v15(), hashes.SHA256())


# ---------------------------------------------------------------- 配置检查

_ALIPAY_REQUIRED = ["ALIPAY_APP_ID", "ALIPAY_PRIVATE_KEY_PATH",
                    "ALIPAY_PUBLIC_KEY_PATH"]
_WECHAT_REQUIRED = ["WECHAT_APP_ID", "WECHAT_MCH_ID",
                    "WECHAT_PRIVATE_KEY_PATH", "WECHAT_CERT_SERIAL_NO",
                    "WECHAT_API_V3_KEY", "WECHAT_PLATFORM_CERT_PATH"]
_EPAY_REQUIRED = ["EPAY_GATEWAY_URL", "EPAY_PID", "EPAY_KEY"]


def configured(provider):
    """返回 (是否可用, 不可用原因)。"""
    if provider == "epay":
        # 易支付签名只用 MD5（标准库），不依赖 cryptography
        missing = [k for k in _EPAY_REQUIRED if not config.get(k)]
        if not config.notify_url("EPAY"):
            missing.append("SITE_BASE_URL 或 EPAY_NOTIFY_URL")
        if not config.return_url("EPAY"):
            missing.append("SITE_BASE_URL 或 EPAY_RETURN_URL")
        if missing:
            return False, "缺少参数：" + "、".join(missing)
        return True, ""
    if not _CRYPTO_OK:
        return False, "服务器未安装支付加密组件（cryptography），请先执行 pip install -r requirements.txt"
    if provider == "alipay":
        required = _ALIPAY_REQUIRED
    elif provider == "wechat":
        required = _WECHAT_REQUIRED
    else:
        return False, "未知支付方式"
    missing = [k for k in required if not config.get(k)]
    if provider == "alipay" and not config.notify_url("ALIPAY"):
        missing.append("SITE_BASE_URL 或 ALIPAY_NOTIFY_URL")
    if provider == "wechat" and not config.notify_url("WECHAT"):
        missing.append("SITE_BASE_URL 或 WECHAT_NOTIFY_URL")
    key_paths = [k for k in required if k.endswith("_PATH")]
    for k in key_paths:
        if config.get(k) and not os.path.exists(config.get(k)):
            missing.append(f"{k} 指向的文件不存在")
    if missing:
        return False, "缺少参数：" + "、".join(missing)
    return True, ""


# ---------------------------------------------------------------- 支付宝

def alipay_create_payment(order_no, amount_cents, subject):
    """生成支付宝电脑网站支付跳转 URL（GET 拼参 + RSA2 签名）。"""
    ok, reason = configured("alipay")
    if not ok:
        raise PaymentNotConfigured(reason)
    total_amount = f"{amount_cents // 100}.{amount_cents % 100:02d}"
    biz_content = json.dumps({
        "out_trade_no": order_no,
        "product_code": "FAST_INSTANT_TRADE_PAY",
        "total_amount": total_amount,
        "subject": subject,
    }, ensure_ascii=False, separators=(",", ":"))
    params = {
        "app_id": config.get("ALIPAY_APP_ID"),
        "method": "alipay.trade.page.pay",
        "format": "JSON",
        "charset": "utf-8",
        "sign_type": "RSA2",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "version": "1.0",
        "notify_url": config.notify_url("ALIPAY"),
        "biz_content": biz_content,
    }
    if config.site_base_url():
        params["return_url"] = config.site_base_url() + "/my-orders"
    sign_content = "&".join(f"{k}={params[k]}" for k in sorted(params))
    private_key = _load_private_key(config.get("ALIPAY_PRIVATE_KEY_PATH"))
    signature = base64.b64encode(
        _rsa_sign(private_key, sign_content.encode("utf-8"))).decode()
    params["sign"] = signature
    gateway = config.get("ALIPAY_GATEWAY")
    return gateway + "?" + urllib.parse.urlencode(params)


def alipay_verify_notify(form):
    """验签支付宝异步通知。成功返回 dict（含 out_trade_no/total_amount/
    trade_status/trade_no），失败抛 PaymentError。"""
    ok, reason = configured("alipay")
    if not ok:
        raise PaymentNotConfigured(reason)
    params = {k: v for k, v in form.items()}
    sign = params.pop("sign", "")
    params.pop("sign_type", None)
    if not sign:
        raise PaymentError("通知缺少 sign")
    sign_content = "&".join(
        f"{k}={params[k]}" for k in sorted(params) if params[k] != "")
    public_key = _load_public_key_from_pem(
        config.get("ALIPAY_PUBLIC_KEY_PATH"))
    try:
        _rsa_verify(public_key, base64.b64decode(sign),
                    sign_content.encode("utf-8"))
    except Exception:
        raise PaymentError("支付宝通知验签失败")
    if params.get("app_id") != config.get("ALIPAY_APP_ID"):
        raise PaymentError("支付宝通知 app_id 不匹配")
    return params


# ---------------------------------------------------------------- 微信支付

_WECHAT_NATIVE_URL = "https://api.mch.weixin.qq.com/v3/pay/transactions/native"


def wechat_create_native(order_no, amount_cents, description):
    """调用 Native 下单，返回 code_url（用于生成二维码）。"""
    ok, reason = configured("wechat")
    if not ok:
        raise PaymentNotConfigured(reason)
    body_dict = {
        "appid": config.get("WECHAT_APP_ID"),
        "mchid": config.get("WECHAT_MCH_ID"),
        "description": description,
        "out_trade_no": order_no,
        "notify_url": config.notify_url("WECHAT"),
        "amount": {"total": amount_cents, "currency": "CNY"},
    }
    body = json.dumps(body_dict, ensure_ascii=False, separators=(",", ":"))
    timestamp = str(int(time.time()))
    nonce = secrets.token_hex(16)
    message = f"POST\n/v3/pay/transactions/native\n{timestamp}\n{nonce}\n{body}\n"
    private_key = _load_private_key(config.get("WECHAT_PRIVATE_KEY_PATH"))
    signature = base64.b64encode(
        _rsa_sign(private_key, message.encode("utf-8"))).decode()
    auth = (
        'WECHATPAY2-SHA256-RSA2048 '
        f'mchid="{config.get("WECHAT_MCH_ID")}",'
        f'nonce_str="{nonce}",'
        f'signature="{signature}",'
        f'timestamp="{timestamp}",'
        f'serial_no="{config.get("WECHAT_CERT_SERIAL_NO")}"'
    )
    req = urllib.request.Request(
        _WECHAT_NATIVE_URL,
        data=body.encode("utf-8"),
        headers={"Authorization": auth, "Accept": "application/json",
                 "Content-Type": "application/json"},
        method="POST")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:300]
        raise PaymentError(f"微信支付下单失败（HTTP {e.code}）：{detail}")
    except OSError as e:
        raise PaymentError(f"微信支付下单网络错误：{e}")
    code_url = data.get("code_url")
    if not code_url:
        raise PaymentError(f"微信支付下单返回缺少 code_url：{data}")
    return code_url


def wechat_verify_and_decrypt_notify(headers, body_bytes):
    """验签并解密微信支付通知。成功返回解密后的交易 dict。

    headers 需包含 wechatpay-timestamp / wechatpay-nonce /
    wechatpay-signature / wechatpay-serial（键名小写）。
    """
    ok, reason = configured("wechat")
    if not ok:
        raise PaymentNotConfigured(reason)
    timestamp = headers.get("wechatpay-timestamp", "")
    nonce = headers.get("wechatpay-nonce", "")
    signature = headers.get("wechatpay-signature", "")
    if not (timestamp and nonce and signature):
        raise PaymentError("微信通知缺少签名头")
    # 防重放：时间戳与本机时间差不超过 5 分钟
    try:
        if abs(int(time.time()) - int(timestamp)) > 300:
            raise PaymentError("微信通知时间戳过期")
    except ValueError:
        raise PaymentError("微信通知时间戳格式错误")
    public_key = _load_public_key_from_pem(
        config.get("WECHAT_PLATFORM_CERT_PATH"), is_cert=True)
    message = f"{timestamp}\n{nonce}\n".encode("utf-8") + body_bytes + b"\n"
    try:
        _rsa_verify(public_key, base64.b64decode(signature), message)
    except Exception:
        raise PaymentError("微信通知验签失败")
    try:
        payload = json.loads(body_bytes.decode("utf-8"))
        resource = payload["resource"]
        api_key = config.get("WECHAT_API_V3_KEY").encode("utf-8")
        if len(api_key) != 32:
            raise PaymentError("WECHAT_API_V3_KEY 必须是 32 位")
        plaintext = AESGCM(api_key).decrypt(
            resource["nonce"].encode("utf-8"),
            base64.b64decode(resource["ciphertext"]),
            (resource.get("associated_data") or "").encode("utf-8"))
        trade = json.loads(plaintext.decode("utf-8"))
    except PaymentError:
        raise
    except Exception as e:
        raise PaymentError(f"微信通知解密失败：{e}")
    if trade.get("mchid") != config.get("WECHAT_MCH_ID"):
        raise PaymentError("微信通知商户号不匹配")
    if trade.get("appid") != config.get("WECHAT_APP_ID"):
        raise PaymentError("微信通知 appid 不匹配")
    return trade


# ---------------------------------------------------------------- 易支付

def _epay_sign(params, key):
    """彩虹易支付 MD5 签名：参数名 ASCII 升序，跳过空值与 sign/sign_type，
    拼成 k=v&k=v 后在末尾直接追加商户 KEY，取 MD5 小写十六进制。"""
    pairs = [(k, str(v)) for k, v in params.items()
             if k not in ("sign", "sign_type") and v is not None
             and str(v) != ""]
    sign_str = "&".join(f"{k}={v}" for k, v in sorted(pairs))
    return hashlib.md5((sign_str + key).encode("utf-8")).hexdigest()


def _epay_submit_url():
    gateway = config.get("EPAY_GATEWAY_URL").rstrip("/")
    if gateway.endswith("submit.php"):
        return gateway
    return gateway + "/submit.php"


def _epay_base_url():
    """网关基址：与 _epay_submit_url 同一套处理——去掉尾斜杠，
    若配置值以 submit.php 结尾则先剥掉，得到可拼其他端点的基址。"""
    gateway = config.get("EPAY_GATEWAY_URL").rstrip("/")
    if gateway.endswith("submit.php"):
        gateway = gateway[:-len("submit.php")].rstrip("/")
    return gateway


def _epay_api_url():
    return _epay_base_url() + "/api.php"


def epay_create_payment(order_no, amount_cents, subject, pay_type):
    """生成易支付跳转 URL：GET {网关}/submit.php?带签名的参数。

    pay_type 为 "alipay"（易支付-支付宝）或 "wxpay"（易支付-微信）。
    """
    ok, reason = configured("epay")
    if not ok:
        raise PaymentNotConfigured(reason)
    if pay_type not in ("alipay", "wxpay"):
        raise PaymentError(f"易支付不支持的支付类型：{pay_type}")
    params = {
        "pid": config.get("EPAY_PID"),
        "type": pay_type,
        "out_trade_no": order_no,
        "notify_url": config.notify_url("EPAY"),
        "return_url": config.return_url("EPAY"),
        "name": subject,
        "money": f"{amount_cents // 100}.{amount_cents % 100:02d}",
    }
    params["sign"] = _epay_sign(params, config.get("EPAY_KEY"))
    params["sign_type"] = "MD5"
    return _epay_submit_url() + "?" + urllib.parse.urlencode(params)


def epay_verify_notify(params):
    """验签易支付异步通知（GET 参数 dict）。成功返回 params，
    失败抛 PaymentError / PaymentNotConfigured。KEY 只参与本地验签，
    绝不出现在返回值、日志或异常文本中。"""
    ok, reason = configured("epay")
    if not ok:
        raise PaymentNotConfigured(reason)
    params = {k: v for k, v in params.items()}
    sign = params.get("sign", "")
    if not sign:
        raise PaymentError("易支付通知缺少 sign")
    expected = _epay_sign(params, config.get("EPAY_KEY"))
    if not secrets.compare_digest(expected, sign.strip().lower()):
        raise PaymentError("易支付通知验签失败")
    if params.get("pid") != config.get("EPAY_PID"):
        raise PaymentError("易支付通知 pid 不匹配")
    return params


def _epay_query_via_relay(relay_url, relay_token, out_trade_no):
    """经中继查单：GET {中继}?out_trade_no=<订单号>，请求头带
    X-Relay-Token。中继代为请求网关 api.php act=order 并原样返回其
    JSON，本函数对返回体的处理与直连模式完全一致。

    token 只放在请求头里发送给中继本身，绝不写日志、不进异常
    文本；中继返回非 200 或响应含 relay_error 一律抛 PaymentError
    （按查询失败处理，绝不误判已支付）。
    """
    sep = "&" if "?" in relay_url else "?"
    url = relay_url + sep + urllib.parse.urlencode(
        {"out_trade_no": out_trade_no})
    req = urllib.request.Request(
        url, headers={"Accept": "application/json",
                      "User-Agent": "curl/8.0",
                      "X-Relay-Token": relay_token}, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception:
        # 不带原始异常文本，避免任何敏感信息泄漏进日志
        raise PaymentError("易支付查单请求失败")
    if not isinstance(data, dict):
        raise PaymentError("易支付查单返回格式异常")
    if data.get("relay_error"):
        raise PaymentError("易支付查单请求失败")
    return data


def epay_query_order(out_trade_no):
    """主动查单：GET {网关}/api.php?act=order&pid&key&out_trade_no。

    经典易支付返回 JSON dict：code=1 查询成功，status=1 已支付 / 0
    未支付，money 为金额（元，格式不固定），trade_no 为网关单号。
    未配置抛 PaymentNotConfigured，网络或返回格式异常抛 PaymentError。
    KEY 只作为请求参数发送给网关本身，绝不写日志、不进异常文本。

    中继模式：EPAY_RELAY_URL 非空时改走中继（本机直连网关不通时
    用，如经 Cloudflare Worker 转发），查单语义与直连完全一致；
    此时还必须配置 EPAY_RELAY_TOKEN，缺失视为未配置。
    """
    missing = [k for k in _EPAY_REQUIRED if not config.get(k)]
    if missing:
        raise PaymentNotConfigured("缺少参数：" + "、".join(missing))
    relay_url = config.get("EPAY_RELAY_URL")
    if relay_url:
        relay_token = config.get("EPAY_RELAY_TOKEN")
        if not relay_token:
            raise PaymentNotConfigured("缺少参数：EPAY_RELAY_TOKEN")
        return _epay_query_via_relay(relay_url, relay_token, out_trade_no)
    params = {
        "act": "order",
        "pid": config.get("EPAY_PID"),
        "key": config.get("EPAY_KEY"),
        "out_trade_no": out_trade_no,
    }
    url = _epay_api_url() + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        url, headers={"Accept": "application/json",
                      "User-Agent": "curl/8.0"}, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception:
        # 不带原始异常文本，避免请求 URL（含 KEY）泄漏进日志
        raise PaymentError("易支付查单请求失败")
    if not isinstance(data, dict):
        raise PaymentError("易支付查单返回格式异常")
    return data
