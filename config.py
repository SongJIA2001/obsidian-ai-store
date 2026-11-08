"""配置加载：优先环境变量，其次同目录 config.json。

所有支付商户参数都从这里读取，代码里不写任何真实参数。
完整的参数清单见 config.example.json 和 README.md。
"""
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(BASE_DIR, "config.json")

# 配置项名称（环境变量名与 config.json 的键名一致）
KEYS = [
    "SITE_BASE_URL",          # 网站对外地址，如 https://shop.example.com（无尾斜杠）
    # 支付宝官方直连
    "ALIPAY_APP_ID",          # 支付宝开放平台应用 APPID
    "ALIPAY_PRIVATE_KEY_PATH",  # 应用私钥 PEM 文件路径
    "ALIPAY_PUBLIC_KEY_PATH",   # 支付宝公钥 PEM 文件路径（验签用）
    "ALIPAY_GATEWAY",         # 网关，默认 https://openapi.alipay.com/gateway.do
    "ALIPAY_NOTIFY_URL",      # 可空，默认 SITE_BASE_URL + /pay/notify/alipay
    # 微信支付官方直连（API v3）
    "WECHAT_APP_ID",          # 微信支付绑定的 AppID（公众号/服务号等）
    "WECHAT_MCH_ID",          # 微信支付商户号
    "WECHAT_PRIVATE_KEY_PATH",  # 商户 API 私钥 apiclient_key.pem 路径
    "WECHAT_CERT_SERIAL_NO",  # 商户 API 证书序列号
    "WECHAT_API_V3_KEY",      # API v3 密钥（32 位，商户平台设置）
    "WECHAT_PLATFORM_CERT_PATH",  # 微信支付平台证书 wechatpay.pem 路径（验签用）
    "WECHAT_NOTIFY_URL",      # 可空，默认 SITE_BASE_URL + /pay/notify/wechat
    # 易支付（彩虹易支付兼容协议，聚合支付）
    "EPAY_GATEWAY_URL",       # 易支付网关地址，如 https://pay.example.com
    "EPAY_PID",               # 易支付商户 ID（PID）
    "EPAY_KEY",               # 易支付商户密钥 KEY（保密，只读配置，绝不外泄）
    "EPAY_NOTIFY_URL",        # 可空，默认 SITE_BASE_URL + /pay/notify/epay
    "EPAY_RETURN_URL",        # 可空，默认 SITE_BASE_URL + /pay/return/epay
    "EPAY_RELAY_URL",         # 可空，查单中继地址（如 Cloudflare Worker）；非空时主动查单改走中继而非直连网关
    "EPAY_RELAY_TOKEN",       # 可空，中继鉴权口令（保密，只读配置，绝不外泄）；配了 RELAY_URL 就必须配它
    # 店主推送通知（新订单 / 新客服留言）
    "PUSH_PROVIDER",          # 可空，bark 或 serverchan；留空表示不推送
    "PUSH_KEY",               # 可空，推送通道 key（Bark 设备 key / Server 酱 SendKey，保密，只读配置，绝不外泄）
]

_DEFAULTS = {
    "ALIPAY_GATEWAY": "https://openapi.alipay.com/gateway.do",
    "PUSH_PROVIDER": "bark",  # 店主推送默认走 Bark（iPhone）；只填 PUSH_KEY 即可启用
}


def _load_file():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict):
                return {k: str(v) for k, v in data.items() if v is not None}
        except (OSError, ValueError):
            return {}
    return {}


_FILE_VALUES = _load_file()


def get(key, default=""):
    val = os.environ.get(key)
    if val:
        return val.strip()
    if key in _FILE_VALUES and _FILE_VALUES[key]:
        return _FILE_VALUES[key].strip()
    return _DEFAULTS.get(key, default)


def site_base_url():
    return get("SITE_BASE_URL").rstrip("/")


def notify_url(provider):
    explicit = get(f"{provider}_NOTIFY_URL")
    if explicit:
        return explicit
    base = site_base_url()
    if base:
        return f"{base}/pay/notify/{provider.lower()}"
    return ""


def return_url(provider):
    explicit = get(f"{provider}_RETURN_URL")
    if explicit:
        return explicit
    base = site_base_url()
    if base:
        return f"{base}/pay/return/{provider.lower()}"
    return ""
