"""店主推送通知：新订单已支付 / 新客服留言时推送到店主手机。

通道由 config 驱动（环境变量或 config.json）：
- PUSH_PROVIDER：bark（默认，店主已选定）或 serverchan（备选）；
- PUSH_KEY：对应通道的 key（Bark 的设备 key / Server 酱的 SendKey），
  属于机密，只读配置，绝不写日志。PUSH_KEY 为空 = 不推送。

未配置 key、通道名不认识或网络失败时一律静默跳过（返回 False），
推送绝不能影响下单、付款、留言等主流程。
"""
import threading
import urllib.parse
import urllib.request

import config

_TIMEOUT_SECONDS = 10
_BARK_BASE = "https://api.day.app"
_SERVERCHAN_BASE = "https://sctapi.ftqq.com"
_PROVIDERS = ("bark", "serverchan")


def _fetch(url, data=None):
    """实际发请求的一层（测试可替换此函数来 mock 网络）。
    data 为 dict 时做表单 POST，为 None 时 GET。返回响应文本。"""
    body = None
    headers = {"User-Agent": "curl/8.0"}
    if data is not None:
        body = urllib.parse.urlencode(data).encode("utf-8")
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    req = urllib.request.Request(url, data=body, headers=headers)
    with urllib.request.urlopen(req, timeout=_TIMEOUT_SECONDS) as resp:
        return resp.read().decode("utf-8", "replace")


def configured():
    return (config.get("PUSH_PROVIDER").strip().lower() in _PROVIDERS
            and bool(config.get("PUSH_KEY").strip()))


def send_push(title, body):
    """同步发送一条推送。成功返回 True；未配置 / 失败返回 False，
    绝不抛异常、绝不把 key 写进任何输出。"""
    provider = config.get("PUSH_PROVIDER").strip().lower()
    key = config.get("PUSH_KEY").strip()
    if provider not in _PROVIDERS or not key:
        return False
    try:
        if provider == "bark":
            url = "/".join([
                _BARK_BASE,
                urllib.parse.quote(key, safe=""),
                urllib.parse.quote(str(title), safe=""),
                urllib.parse.quote(str(body), safe=""),
            ])
            _fetch(url)
        else:  # serverchan
            url = f"{_SERVERCHAN_BASE}/{key}.send"
            _fetch(url, {"title": str(title), "desp": str(body)})
    except Exception:
        return False
    return True


def push_async(title, body):
    """后台线程发送，不阻塞调用方（付款回调 / 留言提交）。"""
    if not configured():
        return
    threading.Thread(target=send_push, args=(title, body),
                     name="push", daemon=True).start()
