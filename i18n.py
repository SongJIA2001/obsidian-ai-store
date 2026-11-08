# -*- coding: utf-8 -*-
"""muse798.com 多语言（upgrade19，2026-11-08，照 qaoqo 上 10 种语言）。

设计：简体中文是源语言，app.py 里的中文原文保持不变、中文路径
零改动；i18n 只为其他语言提供译文，缺失时回退 en → zh。
客户侧本地化，卖家后台保持中文。

语言代码与展示名（顺序照 qaoqo 语言菜单）：
zh 简体中文 / zh-TW 繁體中文 / en English / ja 日本語 /
ko 한국어 / fr Français / de Deutsch / es Español /
pt Português (Brasil) / ru Русский。

其余 7 个语种（ja/ko/fr/de/es/pt/ru）的译文在 i18n_extra.py，
由 merge_extra() 合并进来；文件不存在时自动跳过（回退 en/zh）。
"""

LANGS = [
    ("zh", "简体中文"),
    ("zh-TW", "繁體中文"),
    ("en", "English"),
    ("ja", "日本語"),
    ("ko", "한국어"),
    ("fr", "Français"),
    ("de", "Deutsch"),
    ("es", "Español"),
    ("pt", "Português (Brasil)"),
    ("ru", "Русский"),
]
LANG_CODES = [c for c, _ in LANGS]
DEFAULT_LANG = "zh"

# Accept-Language 首选 → 本站语言代码
_AL_MAP = {
    "zh-tw": "zh-TW", "zh-hk": "zh-TW", "zh-mo": "zh-TW",
    "zh": "zh", "zh-cn": "zh", "zh-sg": "zh",
    "en": "en", "ja": "ja", "ko": "ko", "fr": "fr", "de": "de",
    "es": "es", "pt": "pt", "pt-br": "pt", "ru": "ru",
}


def negotiate(cookie_lang="", accept_language=""):
    if cookie_lang in LANG_CODES:
        return cookie_lang
    for part in (accept_language or "").split(","):
        tag = part.split(";")[0].strip().lower()
        if tag in _AL_MAP:
            return _AL_MAP[tag]
        base = tag.split("-")[0]
        if base in _AL_MAP:
            return _AL_MAP[base]
    return DEFAULT_LANG


# ---------------------------------------------------------------- UI 文案
# 键名分组：nav / home / common / order / orders / wallet / support /
# auth / track / pay / misc。zh 与模板原文逐字一致（中文路径零变化）。
STRINGS = {
    "zh": {
        "nav.home": "首页", "nav.order": "立即下单",
        "nav.my_orders": "我的订单", "nav.wallet": "我的钱包",
        "nav.support": "在线客服", "nav.guide": "使用教程",
        "nav.admin": "卖家后台", "nav.logout": "退出登录",
        "nav.login": "登录", "nav.register": "注册",
        "nav.track": "订单查询",
        "footer.tag": "数字服务，无实物发货",
        "footer.privacy": "隐私政策", "footer.terms": "用户条款",
        "footer.cookies": "Cookie 政策",
        "home.search_ph": "搜索商品",
        "home.all": "全部",
        "home.buy": "立即购买 →", "home.soldout": "已售罄",
        "home.sold_n": "已售 {n} 单",
        "home.stock_n": "库存 {n} 件",
        "home.stock_low": "🔥 仅剩 {n} 件",
        "home.stock_plenty": "库存充足",
        "home.no_match": "没有匹配的商品",
        "common.yuan": "¥",
        "status.unpaid": "待支付",
        "status.paid": "已支付 / 待充值",
        "status.completed": "已完成（已到账）",
        "status.failed": "已失败",
        "status.refunded": "已退款",
        "status.cancelled": "已取消",
    },
    "en": {
        "nav.home": "Home", "nav.order": "Order Now",
        "nav.my_orders": "My Orders", "nav.wallet": "My Wallet",
        "nav.support": "Support", "nav.guide": "Guide",
        "nav.admin": "Seller Admin", "nav.logout": "Log Out",
        "nav.login": "Log In", "nav.register": "Register",
        "nav.track": "Track Order",
        "footer.tag": "Digital services only, no physical shipping",
        "footer.privacy": "Privacy Policy", "footer.terms": "Terms of Service",
        "footer.cookies": "Cookie Policy",
        "home.search_ph": "Search products",
        "home.all": "All",
        "home.buy": "Buy Now →", "home.soldout": "Sold Out",
        "home.sold_n": "{n} sold",
        "home.stock_n": "{n} in stock",
        "home.stock_low": "🔥 Only {n} left",
        "home.stock_plenty": "In stock",
        "home.no_match": "No matching products",
        "common.yuan": "¥",
        "status.unpaid": "Awaiting Payment",
        "status.paid": "Paid / Awaiting Delivery",
        "status.completed": "Completed (Delivered)",
        "status.failed": "Failed",
        "status.refunded": "Refunded",
        "status.cancelled": "Cancelled",
    },
    "zh-TW": {
        "nav.home": "首頁", "nav.order": "立即下單",
        "nav.my_orders": "我的訂單", "nav.wallet": "我的錢包",
        "nav.support": "線上客服", "nav.guide": "使用教學",
        "nav.admin": "賣家後台", "nav.logout": "登出",
        "nav.login": "登入", "nav.register": "註冊",
        "nav.track": "訂單查詢",
        "footer.tag": "數位服務，無實物出貨",
        "footer.privacy": "隱私政策", "footer.terms": "用戶條款",
        "footer.cookies": "Cookie 政策",
        "home.search_ph": "搜尋商品",
        "home.all": "全部",
        "home.buy": "立即購買 →", "home.soldout": "已售罄",
        "home.sold_n": "已售 {n} 單",
        "home.stock_n": "庫存 {n} 件",
        "home.stock_low": "🔥 僅剩 {n} 件",
        "home.stock_plenty": "庫存充足",
        "home.no_match": "沒有符合的商品",
        "common.yuan": "¥",
        "status.unpaid": "待付款",
        "status.paid": "已付款 / 待儲值",
        "status.completed": "已完成（已到帳）",
        "status.failed": "已失敗",
        "status.refunded": "已退款",
        "status.cancelled": "已取消",
    },
}


def tr(lang, key, **kw):
    """取译文：lang → en → zh → key 本身。支持 {name} 占位替换。"""
    for cand in (lang, "en", "zh"):
        table = STRINGS.get(cand) or {}
        if key in table:
            text = table[key]
            if kw:
                try:
                    return text.format(**kw)
                except (KeyError, IndexError):
                    return text
            return text
    return key


def _norm_lang(suffix):
    """变量后缀（大写、- 写成 _）→ 本站语言代码（zh-TW 特例）。"""
    code = suffix.replace("_", "-")
    if code.lower() == "zh-tw":
        return "zh-TW"
    return code.lower()


def merge_extra(module):
    """合并外部语种文件提供的译文表，存在哪个合哪个，互不覆盖 zh。

    约定（变量后缀 = 语言代码大写，- 写成 _，如 ZH_TW）：
    STRINGS_X {key: 文案} / PRODUCTS_X {pid: {name, points, desc,
    first_label, password_hint, first_err}} / BLOBS_X {kind: HTML} /
    WARRANTY_X {pid: 徽章文案或 None} / CAT_X {cat: 名称} /
    ANN_X [(文案, 链接), ...] / LEVEL_X [(等级名, 折扣标签), ...] /
    NOWARRANTY_X "无质保文案"。"""
    for name in dir(module):
        if name.startswith("STRINGS_"):
            lang = _norm_lang(name[len("STRINGS_"):])
            STRINGS.setdefault(lang, {}).update(getattr(module, name))
        elif name.startswith("PRODUCTS_"):
            lang = _norm_lang(name[len("PRODUCTS_"):])
            for pid, val in getattr(module, name).items():
                PRODUCT_I18N.setdefault(lang, {})[pid] = val
        elif name.startswith("BLOBS_"):
            lang = _norm_lang(name[len("BLOBS_"):])
            for kind, val in getattr(module, name).items():
                BLOBS.setdefault(lang, {})[kind] = val
        elif name.startswith("WARRANTY_"):
            lang = _norm_lang(name[len("WARRANTY_"):])
            WARRANTY_I18N.setdefault(lang, {}).update(
                getattr(module, name))
        elif name.startswith("CAT_"):
            lang = _norm_lang(name[len("CAT_"):])
            CAT_I18N.setdefault(lang, {}).update(getattr(module, name))
        elif name.startswith("ANN_"):
            lang = _norm_lang(name[len("ANN_"):])
            ANNOUNCEMENTS_I18N[lang] = getattr(module, name)
        elif name.startswith("LEVEL_"):
            lang = _norm_lang(name[len("LEVEL_"):])
            LEVEL_I18N[lang] = getattr(module, name)
        elif name.startswith("NOWARRANTY_"):
            lang = _norm_lang(name[len("NOWARRANTY_"):])
            NO_WARRANTY_LABEL[lang] = getattr(module, name)


# ---------------------------------------------------------------- 商品译文
# pid -> {name, points, desc, first_label, password_hint}
# zh 不在此表（用 app.py 原文）。
PRODUCT_I18N = {'en': {'gemini-pro-24m': {'name': 'Gemini Pro 24-Month Top-Up',
                           'points': ['Topped up to your own Google account, 24 months of '
                                      'membership',
                                      'No account password needed — only the top-up email and a '
                                      'backup email',
                                      'Alipay accepted',
                                      'Manual top-up after payment; track progress in My Orders'],
                           'desc': 'Gemini Pro membership top-up service, 24 months. After '
                                   'payment, the seller manually tops up the Google account you '
                                   'provide — no account password is ever needed.',
                           'first_label': 'Google account email to top up',
                           'password_hint': 'We will never ask for your Google account password at '
                                            'any step.'},
        'muse-account-1b': {'name': 'Muse Ready Account · 1B Tokens',
                            'points': ['Ready-to-use account with 1B tokens of usage',
                                       'In plain words: tokens ≈ the amount of text the AI reads '
                                       'and writes; 1B tokens is roughly hundreds of millions of '
                                       'Chinese characters — plenty for everyday chat and writing '
                                       'for a long time (estimate; actual use depends on '
                                       'conversation length)',
                                       'Delivered manually by the seller via your contact info '
                                       'after payment',
                                       'Alipay accepted',
                                       'Track delivery progress in My Orders'],
                            'desc': 'Muse ready account with 1B tokens. Delivered manually by the '
                                    'seller via the contact info you provide.',
                            'first_label': 'Email to receive the account',
                            'password_hint': 'After payment, the seller delivers the account via '
                                             'the contact info you provide — please make sure it '
                                             'is accurate.'},
        'muse-2b': {'name': 'Muse · 2B Tokens',
                    'points': ['Muse account with 2B tokens',
                               'In plain words: tokens ≈ the amount of text the AI reads and '
                               'writes; 2B is twice 1B and holds up well even with heavy daily use '
                               '(estimate; actual use depends on conversation length)',
                               'Processed manually by the seller after payment and delivered via '
                               'your contact info',
                               'Alipay accepted',
                               'Track progress in My Orders'],
                    'desc': 'Muse, 2B tokens. Processed manually by the seller after payment and '
                            'delivered via your contact info.',
                    'first_label': 'Receiving email',
                    'password_hint': 'After payment, the seller delivers via the contact info you '
                                     'provide — please make sure it is accurate.'},
        'muse3-1b': {'name': 'Muse · 31B Tokens',
                     'points': ['Muse account with 31B tokens',
                                'In plain words: tokens ≈ the amount of text the AI reads and '
                                'writes; 31B is about 31× the 1B plan, built for long-term heavy '
                                'use (estimate; actual use depends on conversation length)',
                                'Processed manually by the seller after payment and delivered via '
                                'your contact info',
                                'Alipay accepted',
                                'Track progress in My Orders'],
                     'desc': 'Muse, 31B tokens. Processed manually by the seller after payment and '
                             'delivered via your contact info.',
                     'first_label': 'Receiving email',
                     'password_hint': 'After payment, the seller delivers via the contact info you '
                                      'provide — please make sure it is accurate.'},
        'chatgpt-go-3m': {'name': 'ChatGPT Go 3 Months',
                          'points': ['Ready account, 3 months of ChatGPT Go membership',
                                     'Delivery format: email | password | 2FA secret',
                                     '3-day warranty',
                                     '2FA codes: open https://2fa.fun/ , enter the 2FA secret and '
                                     'click Get Code — codes refresh every 30 seconds',
                                     'Delivered manually by the seller via your contact info after '
                                     'payment',
                                     'Alipay accepted',
                                     'Track delivery progress in My Orders'],
                          'desc': 'ChatGPT Go ready account, 3 months, activated via Apple Pay. '
                                  'Delivered manually by the seller via your contact info.',
                          'first_label': 'Email to receive the account',
                          'password_hint': 'After payment, the seller delivers the account via the '
                                           'contact info you provide — please make sure it is '
                                           'accurate.'},
        'chatgpt-plus-1m-applepay': {'name': 'ChatGPT Plus 1 Month (Apple Pay)',
                                     'points': ['Ready account, 1 month of ChatGPT Plus, activated '
                                                'via Apple Pay',
                                                'Delivery format: email / password / 2FA secret',
                                                'Warranty: covers first login within 1 hour only '
                                                '(1H first-login warranty) — please log in and '
                                                'verify as soon as you receive it',
                                                'Delivered manually by the seller via your contact '
                                                'info after payment',
                                                'Alipay accepted',
                                                'Track delivery progress in My Orders'],
                                     'desc': 'ChatGPT Plus ready account, 1 month, activated via '
                                             'Apple Pay. Delivered manually by the seller via your '
                                             'contact info.',
                                     'first_label': 'Email to receive the account',
                                     'password_hint': 'After payment, the seller delivers the '
                                                      'account via the contact info you provide — '
                                                      'please make sure it is accurate.'},
        'grok-plus-1m': {'name': 'Grok Plus 1 Month',
                         'points': ['Ready account, 1 month of Grok Plus membership',
                                    'Shared AI usage pool, including Grok chat, voice, Imagine and '
                                    'Build',
                                    'Includes Grok API access; use at grok.com',
                                    'Delivery format: email + password (both can be changed)',
                                    'Do not unlink the account from X, or usage may be affected',
                                    'No warranty on this product; login-check services are not '
                                    'covered',
                                    'Delivered manually by the seller via your contact info after '
                                    'payment',
                                    'Alipay accepted',
                                    'Track delivery progress in My Orders'],
                         'desc': 'Grok Plus ready account, 1 month. Delivered manually by the '
                                 'seller via your contact info.',
                         'first_label': 'Email to receive the account',
                         'password_hint': 'After payment, the seller delivers the account via the '
                                          'contact info you provide — please make sure it is '
                                          'accurate.'},
        'grok-plus-7d': {'name': 'Grok Plus 7 Days',
                         'points': ['Ready account, 7 days of Grok Plus membership',
                                    '1-day warranty',
                                    'Shared AI usage pool, including Grok chat, voice, Imagine and '
                                    'Build',
                                    'Includes Grok API access; use at grok.com',
                                    'Delivery format: email + password (both can be changed)',
                                    'Do not unlink the account from X, or usage may be affected',
                                    'Login-check services are not covered by the warranty',
                                    'Delivered manually by the seller via your contact info after '
                                    'payment',
                                    'Alipay accepted',
                                    'Track delivery progress in My Orders'],
                         'desc': 'Grok Plus ready account, 7 days. Delivered manually by the '
                                 'seller via your contact info.',
                         'first_label': 'Email to receive the account',
                         'password_hint': 'After payment, the seller delivers the account via the '
                                          'contact info you provide — please make sure it is '
                                          'accurate.'},
        'gmail-old-account': {'name': 'Aged Gmail Account (2010–2022), Random Region',
                              'points': ['Aged Gmail account registered 2010–2022, region assigned '
                                         'randomly',
                                         'Delivery format: email account + login password + backup '
                                         'email + 2FA',
                                         '24H first-login warranty: covers first login within 24 '
                                         'hours only — please log in and verify as soon as you '
                                         'receive it',
                                         'Login may require phone verification; please arrange '
                                         'your own SMS receiving method',
                                         'A stable, trusted network environment is recommended for '
                                         'login',
                                         'Delivered manually by the seller via your contact info '
                                         'after payment',
                                         'Alipay accepted',
                                         'Track delivery progress in My Orders'],
                              'desc': 'Aged Gmail account, registered 2010–2022, random region. '
                                      'Delivered manually by the seller via your contact info.',
                              'first_label': 'Email to receive the account',
                              'password_hint': 'After payment, the seller delivers the account via '
                                               'the contact info you provide — please make sure it '
                                               'is accurate.'}},
 'zh-TW': {'gemini-pro-24m': {'name': 'Gemini Pro 24個月代充',
                              'points': ['代充到您自己的 Google 帳號，會員時長 24 個月',
                                         '全程不需要提供帳號密碼，只需儲值信箱與輔助信箱',
                                         '支援支付寶付款',
                                         '付款後人工儲值，進度可在「我的訂單」即時查看'],
                              'desc': 'Gemini Pro 會員代充服務，時長 24 個月。付款後由店主為您填寫的 Google '
                                      '帳號人工完成儲值，全程不需要提供帳號密碼。',
                              'first_label': '要儲值的 Google 帳號信箱',
                              'password_hint': '我們不會在任何環節向您索取 Google 帳號密碼。'},
           'muse-account-1b': {'name': 'Muse 成品號 · 10億詞元',
                               'points': ['成品號，內含 10 億詞元額度',
                                          '先說人話：詞元 ≈ AI 讀寫的文字量，10 '
                                          '億詞元約合數億漢字，日常聊天、寫作能用很久（約數，實際消耗看每次對話長短）',
                                          '付款後由店主人工出貨，透過聯絡方式交付帳號',
                                          '支援支付寶付款',
                                          '出貨進度可在「我的訂單」即時查看'],
                               'desc': 'Muse 成品號，內含 10 億詞元額度。付款後由店主人工出貨，透過您填寫的聯絡方式交付帳號。',
                               'first_label': '接收帳號的信箱',
                               'password_hint': '付款後店主會透過您填寫的聯絡方式交付帳號，請確保聯絡方式準確無誤。'},
           'muse-2b': {'name': 'Muse · 20億詞元',
                       'points': ['Muse，含 20 億詞元',
                                  '先說人話：詞元 ≈ AI 讀寫的文字量，20 億是 10 億的兩倍，天天重度用也耐用（約數，實際消耗看每次對話長短）',
                                  '付款後由店主人工處理，透過聯絡方式交付',
                                  '支援支付寶付款',
                                  '處理進度可在「我的訂單」即時查看'],
                       'desc': 'Muse，20 億詞元。付款後由店主人工處理，透過您填寫的聯絡方式交付。',
                       'first_label': '接收信箱',
                       'password_hint': '付款後店主會透過您填寫的聯絡方式交付，請確保聯絡方式準確無誤。'},
           'muse3-1b': {'name': 'Muse · 310億詞元',
                        'points': ['Muse，含 310 億詞元',
                                   '先說人話：詞元 ≈ AI 讀寫的文字量，310 億約為 10 億的 31 '
                                   '倍，適合長期高頻使用（約數，實際消耗看每次對話長短）',
                                   '付款後由店主人工處理，透過聯絡方式交付',
                                   '支援支付寶付款',
                                   '處理進度可在「我的訂單」即時查看'],
                        'desc': 'Muse，310 億詞元。付款後由店主人工處理，透過您填寫的聯絡方式交付。',
                        'first_label': '接收信箱',
                        'password_hint': '付款後店主會透過您填寫的聯絡方式交付，請確保聯絡方式準確無誤。'},
           'chatgpt-go-3m': {'name': 'ChatGPT Go 三個月',
                             'points': ['成品號，ChatGPT Go 會員時長 3 個月',
                                        '交付格式：信箱 | 密碼 | 2FA 密鑰',
                                        '質保 3 天',
                                        '2FA 驗證碼：打開 https://2fa.fun/ 輸入 2FA 密鑰，點擊「取得驗證碼」，驗證碼每 30 '
                                        '秒自動更新一次',
                                        '付款後由店主人工出貨，透過聯絡方式交付帳號',
                                        '支援支付寶付款',
                                        '出貨進度可在「我的訂單」即時查看'],
                             'desc': 'ChatGPT Go 成品號，時長 3 個月，Apple Pay '
                                     '支付開通。付款後由店主人工出貨，透過您填寫的聯絡方式交付帳號。',
                             'first_label': '接收帳號的信箱',
                             'password_hint': '付款後店主會透過您填寫的聯絡方式交付帳號，請確保聯絡方式準確無誤。'},
           'chatgpt-plus-1m-applepay': {'name': 'ChatGPT Plus 1月 Apple Pay',
                                        'points': ['成品號，ChatGPT Plus 會員時長 1 個月，Apple Pay 支付開通',
                                                   '交付格式：信箱 / 密碼 / 2FA 密鑰',
                                                   '質保：僅保障 1 小時內首次登入（1H 質保首登），請收到後盡快登入驗證',
                                                   '付款後由店主人工出貨，透過聯絡方式交付帳號',
                                                   '支援支付寶付款',
                                                   '出貨進度可在「我的訂單」即時查看'],
                                        'desc': 'ChatGPT Plus 成品號，時長 1 個月，Apple Pay '
                                                '支付開通。付款後由店主人工出貨，透過您填寫的聯絡方式交付帳號。',
                                        'first_label': '接收帳號的信箱',
                                        'password_hint': '付款後店主會透過您填寫的聯絡方式交付帳號，請確保聯絡方式準確無誤。'},
           'grok-plus-1m': {'name': 'Grok Plus 1個月',
                            'points': ['成品號，Grok Plus 會員時長 1 個月',
                                       '共享 AI 使用額度池，含 Grok 聊天、語音、Imagine 和 Build',
                                       '含 Grok API 存取權限，官網 grok.com 登入使用',
                                       '交付格式：信箱 + 密碼，信箱和密碼均可修改',
                                       '請勿解除與 X 的關聯，否則可能影響使用',
                                       '本商品無質保；登入檢測服務不在保固範圍內',
                                       '付款後由店主人工出貨，透過聯絡方式交付帳號',
                                       '支援支付寶付款',
                                       '出貨進度可在「我的訂單」即時查看'],
                            'desc': 'Grok Plus 成品號，時長 1 個月。付款後由店主人工出貨，透過您填寫的聯絡方式交付帳號。',
                            'first_label': '接收帳號的信箱',
                            'password_hint': '付款後店主會透過您填寫的聯絡方式交付帳號，請確保聯絡方式準確無誤。'},
           'grok-plus-7d': {'name': 'Grok Plus 7天',
                            'points': ['成品號，Grok Plus 會員時長 7 天',
                                       '質保 1 天',
                                       '共享 AI 使用額度池，含 Grok 聊天、語音、Imagine 和 Build',
                                       '含 Grok API 存取權限，官網 grok.com 登入使用',
                                       '交付格式：信箱 + 密碼，信箱和密碼均可修改',
                                       '請勿解除與 X 的關聯，否則可能影響使用',
                                       '登入檢測服務不在保固範圍內',
                                       '付款後由店主人工出貨，透過聯絡方式交付帳號',
                                       '支援支付寶付款',
                                       '出貨進度可在「我的訂單」即時查看'],
                            'desc': 'Grok Plus 成品號，時長 7 天。付款後由店主人工出貨，透過您填寫的聯絡方式交付帳號。',
                            'first_label': '接收帳號的信箱',
                            'password_hint': '付款後店主會透過您填寫的聯絡方式交付帳號，請確保聯絡方式準確無誤。'},
           'gmail-old-account': {'name': '老號 Gmail 谷歌信箱（2010–2022）隨機地區',
                                 'points': ['Gmail 谷歌信箱老號，2010–2022 年註冊，地區隨機',
                                            '交付格式：信箱帳號 + 登入密碼 + 輔助信箱 + 2FA',
                                            '24H 質保首登：僅保障 24 小時內首次登入，請收到後盡快登入驗證',
                                            '登入時可能需要手機驗證，請自備接碼方式',
                                            '建議使用穩定、可信的網路環境登入',
                                            '付款後由店主人工出貨，透過聯絡方式交付帳號',
                                            '支援支付寶付款',
                                            '出貨進度可在「我的訂單」即時查看'],
                                 'desc': 'Gmail 老號信箱，2010–2022 年註冊，地區隨機。付款後由店主人工出貨，透過您填寫的聯絡方式交付帳號。',
                                 'first_label': '接收帳號的信箱',
                                 'password_hint': '付款後店主會透過您填寫的聯絡方式交付帳號，請確保聯絡方式準確無誤。'}}}


# first_err 译文补丁（下单校验报错）
_FIRST_ERR = {'en': {'gemini-pro-24m': 'The Google account email to top up is not a valid email format', 'muse-account-1b': 'The receiving account email format is incorrect', 'muse-2b': 'The receiving email format is incorrect', 'muse3-1b': 'The receiving email format is incorrect', 'chatgpt-go-3m': 'The receiving account email format is incorrect', 'chatgpt-plus-1m-applepay': 'The receiving account email format is incorrect', 'grok-plus-1m': 'The receiving account email format is incorrect', 'grok-plus-7d': 'The receiving account email format is incorrect', 'gmail-old-account': 'The receiving account email format is incorrect'}, 'zh-TW': {'gemini-pro-24m': '要儲值的 Google 帳號信箱格式不正確', 'muse-account-1b': '接收帳號的信箱格式不正確', 'muse-2b': '接收信箱格式不正確', 'muse3-1b': '接收信箱格式不正確', 'chatgpt-go-3m': '接收帳號的信箱格式不正確', 'chatgpt-plus-1m-applepay': '接收帳號的信箱格式不正確', 'grok-plus-1m': '接收帳號的信箱格式不正確', 'grok-plus-7d': '接收帳號的信箱格式不正確', 'gmail-old-account': '接收帳號的信箱格式不正確'}}
for _l, _m in _FIRST_ERR.items():
    for _pid, _e in _m.items():
        if _pid in PRODUCT_I18N.get(_l, {}):
            PRODUCT_I18N[_l][_pid]['first_err'] = _e


LEVEL_I18N = {
    "en": [("Standard", ""), ("Silver", "2% off"), ("Gold", "5% off"),
           ("Platinum", "8% off"), ("Black Gold", "12% off")],
    "zh-TW": [("普通會員", ""), ("白銀會員", "9.8 折"),
              ("黃金會員", "9.5 折"), ("鉑金會員", "9.2 折"),
              ("黑金會員", "8.8 折")],
}

# 大块文案（公告 / 质保徽章 / 分类名 / 等级名）：键 -> {lang: 文案}
WARRANTY_I18N = {
    "en": {
        "gemini-pro-24m": "🛡 Full refund if top-up fails",
        "muse-account-1b": "🛡 First-login guarantee",
        "muse-2b": "🛡 First-login guarantee",
        "muse3-1b": "🛡 First-login guarantee",
        "chatgpt-go-3m": "🛡 3-day warranty",
        "chatgpt-plus-1m-applepay": "🛡 1-hour warranty · first login",
        "grok-plus-1m": None,
        "grok-plus-7d": "🛡 1-day warranty",
        "gmail-old-account": "🛡 24-hour warranty · first login",
    },
    "zh-TW": {
        "gemini-pro-24m": "🛡 充不上全額退",
        "muse-account-1b": "🛡 保首登",
        "muse-2b": "🛡 保首登",
        "muse3-1b": "🛡 保首登",
        "chatgpt-go-3m": "🛡 質保 3 天",
        "chatgpt-plus-1m-applepay": "🛡 質保 1 小時 · 首登",
        "grok-plus-1m": None,
        "grok-plus-7d": "🛡 質保 1 天",
        "gmail-old-account": "🛡 質保 24 小時 · 首登",
    },
}
NO_WARRANTY_LABEL = {
    "en": "No warranty", "zh-TW": "無質保", "ja": "保証なし",
    "ko": "보증 없음", "fr": "Sans garantie", "de": "Keine Garantie",
    "es": "Sin garantía", "pt": "Sem garantia", "ru": "Без гарантии",
}
CAT_I18N = {
    "en": {"gemini": "Gemini", "muse": "Muse", "openai": "OpenAI",
           "grok": "Grok", "gmail": "Gmail"},
    "zh-TW": {"gemini": "Gemini", "muse": "Muse", "openai": "OpenAI",
              "grok": "Grok", "gmail": "Gmail"},
}
ANNOUNCEMENTS_I18N = {
    "en": [
        ("🎉 First top-up bonus: first wallet top-up of ¥10+ gets ¥2 free, ¥15+ gets ¥5 free — see My Wallet →", "/wallet"),
        ("🛡 Buyer protection: full refund before delivery; see each product's warranty badge and the Guide →", "/guide"),
        ("💬 Manual delivery: the seller processes orders by hand after payment; track progress in My Orders, or contact Support →", "/support"),
    ],
    "zh-TW": [
        ("🎉 首充福利：首次儲值滿 ¥10 贈 ¥2、滿 ¥15 贈 ¥5，去錢包看看 →", "/wallet"),
        ("🛡 售後保障：未交付可全額退款，各商品質保見卡片徽章與教學頁 →", "/guide"),
        ("💬 人工交付：付款後店主人工處理，進度在「我的訂單」即時可查，有問題點線上客服 →", "/support"),
    ],
}

# 大块 HTML 文案：BLOBS[lang][kind]，kind ∈ guide / legal_privacy /
# legal_terms / legal_cookies / usage_muse / usage_gemini /
# usage_openai / usage_grok / usage_gmail。zh 不在此（app.py 原文）。
BLOBS = {}


BLOBS.update({'en': {'usage_muse': '<ol>\n'
                      '          <li>Go to muse.ai and log in with the <b>email and password</b> in the '
                      'delivery.</li>\n'
                      '          <li>The delivery format is usually "email - password - code link"; if a '
                      'verification code is needed, open the code link to get it.</li>\n'
                      '          <li>If you see "you have joined the waitlist", that is usually a regional '
                      'restriction — switch to a <b>US or Canada</b> network node and log in again.</li>\n'
                      '          <li>Some accounts may require face-photo verification; whether it passes is '
                      'decided by Muse officially.</li>\n'
                      '          <li>Account problems or need help? Contact the seller on QQ 1006025461 '
                      '(include your order number).</li>\n'
                      '        </ol>',
        'usage_gemini': '<ol>\n'
                        '          <li>Make sure the Google email and backup email you entered at checkout '
                        'are correct.</li>\n'
                        '          <li>Add the seller on QQ 1006025461 with your order number, and cooperate '
                        'to complete the top-up.</li>\n'
                        '          <li>Afterwards, confirm on your Google account subscription page that '
                        'Gemini Pro is active (24 months).</li>\n'
                        '          <li>You never need to provide your Google account password — refuse '
                        'anyone who asks.</li>\n'
                        '        </ol>',
        'usage_grok': '<ol>\n'
                      '          <li>Go to grok.com and log in with the <b>email and password</b> in the '
                      'delivery.</li>\n'
                      '          <li>Both email and password can be changed; <b>do not unlink the account '
                      'from X</b>, or usage may be affected.</li>\n'
                      '          <li>The 7-day plan has a 1-day warranty; the 1-month plan has no warranty; '
                      'login-check services are not covered.</li>\n'
                      '          <li>Account problems or need help? Contact the seller on QQ 1006025461 '
                      '(include your order number).</li>\n'
                      '        </ol>',
        'usage_gmail': '<ol>\n'
                       '          <li>Log in to Gmail with the <b>email account and password</b> in the '
                       'delivery; use the backup email and 2FA when verification is required.</li>\n'
                       '          <li>This product is covered only for <b>first login within 24 hours</b> — '
                       'please log in and verify as soon as you receive it.</li>\n'
                       '          <li>Phone verification may be required at login; please arrange your own '
                       'SMS receiving method, and use a stable, trusted network.</li>\n'
                       '          <li>Account problems or need help? Contact the seller on QQ 1006025461 '
                       '(include your order number).</li>\n'
                       '        </ol>',
        'usage_openai': '<ol>\n'
                        '          <li>Go to chatgpt.com and log in with the <b>email and password</b> in '
                        'the delivery.</li>\n'
                        '          <li>If a verification code is needed, open https://2fa.fun/ , enter the '
                        '<b>2FA secret</b> from the delivery and click "Get Code" — codes refresh every 30 '
                        'seconds.</li>\n'
                        '          <li>The ChatGPT Plus 1-month plan covers <b>first login within 1 hour</b> '
                        'only — log in and verify as soon as you receive it; the ChatGPT Go 3-month plan has '
                        'a 3-day warranty.</li>\n'
                        '          <li>Account problems or need help? Contact the seller on QQ 1006025461 '
                        '(include your order number).</li>\n'
                        '        </ol>',
        'usage_default': '<ul>\n'
                         '          <li>Just follow the delivery content above.</li>\n'
                         '          <li>Any questions? Contact the seller on QQ 1006025461 with your order '
                         'number.</li>\n'
                         '        </ul>'},
 'zh-TW': {'usage_muse': '<ol>\n'
                         '          <li>打開 muse.ai，使用交付內容中的<b>信箱和密碼</b>登入。</li>\n'
                         '          <li>交付格式一般為「信箱 - 密碼 - 接碼連結」，登入需要驗證碼時，打開接碼連結取得。</li>\n'
                         '          <li>若提示「你已加入等候名單」，多為地區限制，可切換<b>美國或加拿大</b>網路節點後重新登入。</li>\n'
                         '          <li>部分帳號可能需要人臉照片驗證，能否通過由 Muse 官方判定。</li>\n'
                         '          <li>帳號異常或不會用，聯絡店主 QQ 1006025461（備註訂單號）。</li>\n'
                         '        </ol>',
           'usage_gemini': '<ol>\n'
                           '          <li>確認下單時填的 Google 信箱、輔助信箱無誤。</li>\n'
                           '          <li>添加店主 QQ 1006025461 並備註訂單號，配合店主完成代充。</li>\n'
                           '          <li>完成後在 Google 帳號的訂閱頁面確認 Gemini Pro 已生效（時長 24 個月）。</li>\n'
                           '          <li>全程不需要提供 Google 帳號密碼，任何人索取都要拒絕。</li>\n'
                           '        </ol>',
           'usage_grok': '<ol>\n'
                         '          <li>打開 grok.com，使用交付內容中的<b>信箱和密碼</b>登入。</li>\n'
                         '          <li>信箱和密碼均可修改；<b>請勿解除與 X 的關聯</b>，否則可能影響使用。</li>\n'
                         '          <li>Grok Plus 7天款質保 1 天，1 個月款無質保；登入檢測服務不在保固範圍內。</li>\n'
                         '          <li>帳號異常或不會用，聯絡店主 QQ 1006025461（備註訂單號）。</li>\n'
                         '        </ol>',
           'usage_gmail': '<ol>\n'
                          '          <li>使用交付內容中的<b>信箱帳號和登入密碼</b>登入 Gmail，需要驗證時用交付的輔助信箱與 2FA。</li>\n'
                          '          <li>本商品 <b>24 小時內首次登入</b>才在質保內，收到後請盡快登入驗證。</li>\n'
                          '          <li>登入時可能需要手機驗證，請自備接碼方式；建議使用穩定、可信的網路環境登入。</li>\n'
                          '          <li>帳號異常或不會用，聯絡店主 QQ 1006025461（備註訂單號）。</li>\n'
                          '        </ol>',
           'usage_openai': '<ol>\n'
                           '          <li>打開 chatgpt.com，使用交付內容中的<b>信箱和密碼</b>登入。</li>\n'
                           '          <li>登入需要驗證碼時，打開 https://2fa.fun/ ，輸入交付內容中的 <b>2FA '
                           '密鑰</b>，點擊「取得驗證碼」，驗證碼每 30 秒自動更新一次。</li>\n'
                           '          <li>ChatGPT Plus 1月款僅保障 <b>1 小時內首次登入</b>，收到後請盡快登入驗證；ChatGPT Go 三個月款質保 '
                           '3 天。</li>\n'
                           '          <li>帳號異常或不會用，聯絡店主 QQ 1006025461（備註訂單號）。</li>\n'
                           '        </ol>',
           'usage_default': '<ul>\n'
                            '          <li>按上方交付內容使用即可。</li>\n'
                            '          <li>有任何問題，聯絡店主 QQ 1006025461 並提供訂單號。</li>\n'
                            '        </ul>'}})


def _deep_blobs(payload):
    """按 kind 深合并进 BLOBS（不能用 BLOBS.update 整表替换，
    否则会冲掉先写入的同语种 usage_* 文案）。"""
    for _l, _t in payload.items():
        BLOBS.setdefault(_l, {}).update(_t)


_deep_blobs({'en': {'legal_privacy': '\n'
                         '        <h2>What we collect</h2>\n'
                         '        <ul>\n'
                         '          <li><b>Account info</b>: your registered email and login password '
                         '(stored salted and hashed — we cannot see it in plain text).</li>\n'
                         '          <li><b>Order info</b>: the products and amounts you purchased, plus the '
                         'top-up email, backup email, contact info and delivery content you provided when '
                         'ordering.</li>\n'
                         '          <li><b>Wallet &amp; support records</b>: top-up / spending history and '
                         'your support chat content.</li>\n'
                         '          <li><b>Security records</b>: to prevent account theft and order fraud, '
                         'the system records security information such as failed login counts.</li>\n'
                         '        </ul>\n'
                         '        <h2>What it is used for</h2>\n'
                         '        <ul>\n'
                         '          <li>Processing orders, completing delivery and providing '
                         'after-sales;</li>\n'
                         '          <li>Keeping accounts and funds safe;</li>\n'
                         '          <li>We do not sell or rent your personal information, and do not use it '
                         'for ad profiling.</li>\n'
                         '        </ul>\n'
                         '        <h2>What we will never do</h2>\n'
                         '        <ul>\n'
                         '          <li>At no point will this site <b>ask for your Google account or any '
                         'other third-party account password</b> — do not give it to anyone.</li>\n'
                         '          <li>Payments are completed through third-party payment platforms; this '
                         'site never touches or stores your bank card details or payment passwords.</li>\n'
                         '        </ul>\n'
                         '        <h2>Retention &amp; deletion</h2>\n'
                         '        <p>Order records are kept for a period for after-sales and reconciliation. '
                         'To delete your account and personal information, contact us via Support or the '
                         "seller's QQ 1006025461; we will process it after verifying your identity.</p>",
        'legal_terms': '\n'
                       '        <h2>Nature of the service</h2>\n'
                       '        <p>This site sells digital products (membership top-up services and ready '
                       'accounts), delivered manually by the seller, with no physical shipping.</p>\n'
                       '        <h2>Ordering &amp; payment</h2>\n'
                       '        <ul>\n'
                       '          <li>Product prices, stock and warranty are as shown on the product '
                       'pages.</li>\n'
                       '          <li>Whether a payment succeeded is determined by the order status; if the '
                       'payment system confirms with a delay, contact the seller with your payment proof for '
                       'manual verification — you will never be asked to pay twice.</li>\n'
                       '          <li>Please make sure the top-up email, contact info and other details are '
                       'accurate when ordering; losses caused by incorrect information provided by the buyer '
                       'are borne by the buyer. If you notice a mistake, contact the seller '
                       'immediately.</li>\n'
                       '        </ul>\n'
                       '        <h2>Warranty &amp; refunds</h2>\n'
                       '        <ul>\n'
                       '          <li>Orders not yet delivered can be fully refunded at any time by '
                       'contacting the seller.</li>\n'
                       "          <li>Each product's warranty scope and period are as shown in the product "
                       'card badges and the <a href="/guide">Guide\'s after-sales rules</a>, which '
                       'prevail.</li>\n'
                       '          <li>Delivered orders beyond the warranty scope are not refundable.</li>\n'
                       '        </ul>\n'
                       '        <h2>Buyer notes</h2>\n'
                       '        <ul>\n'
                       '          <li>After receiving a ready account, please log in and verify it within '
                       'the warranty period;</li>\n'
                       '          <li>Bans or invalidation caused by changing the password yourself, lending '
                       "the account, or misuse (including violating the target platform's rules) are not "
                       'covered by the warranty.</li>\n'
                       '        </ul>\n'
                       '        <h2>Changes to these terms</h2>\n'
                       '        <p>Updates to these terms are published on this page; continuing to use this '
                       "site means acceptance. Questions? Contact us via Support or the seller's QQ "
                       '1006025461.</p>',
        'legal_cookies': '\n'
                         '        <h2>Which cookies this site uses</h2>\n'
                         '        <ul>\n'
                         '          <li><b>Login session cookie (essential)</b>: keeps you logged in after '
                         'login and performs form security checks; it expires when you log out or after its '
                         'lifetime.</li>\n'
                         '          <li>The home page announcement\'s "closed" preference is stored locally '
                         'in your browser (localStorage) and is not uploaded to the server.</li>\n'
                         '        </ul>\n'
                         '        <h2>What we do not do</h2>\n'
                         '        <ul>\n'
                         '          <li>No advertising cookies, no cross-site tracking;</li>\n'
                         '          <li>No third-party analytics or user profiling services.</li>\n'
                         '        </ul>\n'
                         '        <h2>Third-party pages</h2>\n'
                         '        <p>During payment you are redirected to third-party payment pages such as '
                         "Alipay; the cookies those pages use are governed by the third parties' own "
                         'policies, not this site.</p>\n'
                         '        <h2>Your choices</h2>\n'
                         '        <p>You can clear or disable cookies in your browser, but with cookies '
                         'disabled you cannot stay logged in, and therefore cannot order or view orders.</p>',
        'guide': '<div class="card guide"><h1>Guide</h1>\n        <h2>1. How buying works</h2>\n        <ol>\n          <li><b>Register / log in</b>: create an account with your email (needed for ordering and tracking orders).</li>\n          <li><b>Choose a product and order</b>: on the home page, click "Buy Now" on a product, fill in the details as prompted and submit.</li>\n          <li><b>Pay</b>: we currently accept <b>Alipay</b>. After successful payment, the order automatically becomes "Paid / Awaiting Delivery" within about 1 minute.</li>\n          <li><b>Wait for the seller</b>: the seller processes orders in payment order; track progress anytime in My Orders.</li>\n        </ol>\n        <h2>2. Gemini Pro top-up (needs your cooperation)</h2>\n        <ol>\n          <li>At checkout, fill in the <b>Google email to top up</b> and a <b>backup email</b> — both must be correct.</li>\n          <li>After payment, please <b>add the seller on QQ (see below)</b>, mention your order number when adding — the top-up needs real-time cooperation with the seller.</li>\n          <li>When done, the membership is credited to your own Google account, for 24 months.</li>\n        </ol>\n        <p class="hint">⚠️ Important: you <b>never need to provide your Google account password</b> at any point. The seller will never ask for your password; never give it to anyone who asks.</p>\n        <h2>3. Muse ready accounts (just wait for delivery)</h2>\n        <ol>\n          <li>At checkout, you only need to fill in your <b>contact info</b> so the seller can reach you.</li>\n          <li>After payment, the seller sends the <b>account and password into your order</b>: open My Orders and find them in the "Delivery" section of the order — one click to copy.</li>\n          <li>Once received, log in to muse.ai promptly to confirm the account works, and keep the credentials safe.</li>\n          <li>"Tokens" ≈ the amount of text the AI reads and writes: 100M tokens is roughly tens of millions of Chinese characters, and 1B tokens lasts a long time for everyday chat and writing (estimates; actual use depends on conversation length).</li>\n        </ol>\n        <h2>4. Payment &amp; after-sales</h2>\n        <ul>\n          <li>If your order status has not updated for a long time after payment (over 10 minutes), contact the seller on QQ with your order number.</li>\n          <li>All order statuses are as shown on the My Orders page.</li>\n        </ul>\n        <h2>After-sales &amp; refund rules (order with confidence)</h2>\n        <ul>\n          <li><b>Refundable before delivery</b>: any time before an order is delivered (marked "Completed"), contact the seller to cancel and get a <b>full refund</b>.</li>\n          <li><b>How refunds arrive</b>: for balance-paid orders, the refund returns instantly and automatically to your site balance; for Alipay-paid orders, the seller refunds via Alipay to the original payment route.</li>\n          <li><b>Gemini top-ups</b>: if the top-up fails for reasons on the seller\'s side, a full refund; if a wrong email you provided caused a misdirected top-up, contact the seller immediately to verify and resolve it; memberships successfully credited are not refundable without cause.</li>\n          <li><b>Muse ready accounts</b>: first-login guarantee — please complete your first login and verify promptly after delivery; if the first login fails, contact the seller immediately (with your order number) — after verification we will replace or refund it; once the first login succeeds, later account issues (including changing the password yourself or misuse) are not covered.</li>\n          <li>All after-sales go through <b>Support</b> or the seller\'s QQ (see below) — please include your order number.</li>\n        </ul>\n        <h2>5. Wallet top-ups &amp; support</h2>\n        <ul>\n          <li><b>Top up</b>: in My Wallet you can top up in advance via Alipay; later orders can then be paid directly with your balance, without an Alipay redirect each time.</li>\n          <li><b>Support</b>: the "Support" item in the top navigation lets you message the seller directly; after the seller replies, a red number badge appears in the navigation.</li>\n          <li>If a balance-paid order is refunded, the amount returns to your balance automatically.</li>\n        </ul>\n        </div>'},
 'zh-TW': {'legal_privacy': '\n'
                            '        <h2>我們收集哪些資訊</h2>\n'
                            '        <ul>\n'
                            '          <li><b>帳號資訊</b>：註冊信箱、登入密碼（加鹽雜湊保存，我們看不到明文）。</li>\n'
                            '          <li><b>訂單資訊</b>：所購商品與金額，以及您下單時填寫的儲值信箱、輔助信箱、聯絡方式和交付內容。</li>\n'
                            '          <li><b>錢包與客服記錄</b>：儲值 / 消費流水、線上客服的聊天內容。</li>\n'
                            '          <li><b>安全記錄</b>：為防盜號與防刷單，系統會記錄登入失敗次數等安全資訊。</li>\n'
                            '        </ul>\n'
                            '        <h2>這些資訊用來做什麼</h2>\n'
                            '        <ul>\n'
                            '          <li>處理訂單、完成交付、提供售後；</li>\n'
                            '          <li>保障帳號與資金安全；</li>\n'
                            '          <li>不出售、不出租您的個人資訊，不用於廣告畫像。</li>\n'
                            '        </ul>\n'
                            '        <h2>我們絕不會做的事</h2>\n'
                            '        <ul>\n'
                            '          <li>本站任何環節<b>不會向您索取 Google 帳號或其他第三方帳號的密碼</b>，請勿向任何人提供。</li>\n'
                            '          <li>付款透過第三方支付平台完成，本站不接觸、不保存您的銀行卡資訊與支付密碼。</li>\n'
                            '        </ul>\n'
                            '        <h2>保存與刪除</h2>\n'
                            '        <p>訂單記錄會為售後與對帳保留一段時間。如需刪除帳號及個人資訊，請透過線上客服或店主 QQ 1006025461 '
                            '聯絡，核驗身分後處理。</p>',
           'legal_terms': '\n'
                          '        <h2>服務性質</h2>\n'
                          '        <p>本站銷售數位商品（會員代充服務與成品帳號），由店主人工交付，無實物出貨。</p>\n'
                          '        <h2>下單與付款</h2>\n'
                          '        <ul>\n'
                          '          <li>商品價格、庫存與質保以商品頁展示為準。</li>\n'
                          '          <li>付款是否成功以訂單狀態為準；如遇支付系統確認延遲，憑付款憑證聯絡店主人工核對處理，不會讓您重複付款。</li>\n'
                          '          <li>下單時請確保儲值信箱、聯絡方式等資訊準確；因買家填寫錯誤造成的損失由買家承擔，發現填錯請第一時間聯絡店主。</li>\n'
                          '        </ul>\n'
                          '        <h2>質保與退款</h2>\n'
                          '        <ul>\n'
                          '          <li>未交付的訂單可隨時聯絡店主全額退款。</li>\n'
                          '          <li>各商品質保範圍與時限見商品卡徽章和<a href="/guide">《使用教學》售後規則</a>，以那裡為準。</li>\n'
                          '          <li>已交付且超出質保範圍的，不支援退款。</li>\n'
                          '        </ul>\n'
                          '        <h2>買家須知</h2>\n'
                          '        <ul>\n'
                          '          <li>成品號收到後請在質保期內盡快登入驗證；</li>\n'
                          '          <li>買家自行改密、轉借或違規使用（含違反目標平台規則）導致的封禁、失效不在質保範圍。</li>\n'
                          '        </ul>\n'
                          '        <h2>條款變更</h2>\n'
                          '        <p>本條款更新後在本頁公布，繼續使用本站即視為接受。有疑問請透過線上客服或店主 QQ 1006025461 聯絡。</p>',
           'legal_cookies': '\n'
                            '        <h2>本站使用哪些 Cookie</h2>\n'
                            '        <ul>\n'
                            '          <li><b>登入工作階段 Cookie（必需）</b>：您登入後用來保持登入狀態，並做表單安全校驗；登出或過期後失效。</li>\n'
                            '          <li>首頁公告的「已關閉」偏好保存在您瀏覽器本地（localStorage），不會上傳伺服器。</li>\n'
                            '        </ul>\n'
                            '        <h2>我們不做的事</h2>\n'
                            '        <ul>\n'
                            '          <li>不使用廣告 Cookie，不做跨站追蹤；</li>\n'
                            '          <li>不接入第三方統計或用戶畫像服務。</li>\n'
                            '        </ul>\n'
                            '        <h2>第三方頁面</h2>\n'
                            '        <p>付款時會跳轉到支付寶等第三方支付頁面，那些頁面使用的 Cookie 由第三方自己的政策管理，與本站無關。</p>\n'
                            '        <h2>您的選擇</h2>\n'
                            '        <p>您可以在瀏覽器裡清除或停用 Cookie，但停用後將無法保持登入狀態，也就無法下單和查看訂單。</p>',
           'guide': '<div class="card guide"><h1>使用教學</h1>\n        <h2>一、通用購買流程</h2>\n        <ol>\n          <li><b>註冊 / 登入</b>：用信箱註冊一個帳號（下單和查訂單都要用它）。</li>\n          <li><b>選商品下單</b>：在首頁點商品的「立即購買」，按提示填寫資料並提交。</li>\n          <li><b>付款</b>：目前支援<b>支付寶</b>付款。付款成功後訂單會在約 1 分鐘內自動變為「已付款 / 待儲值」。</li>\n          <li><b>等店主處理</b>：店主按付款順序逐單處理，進度隨時在「我的訂單」裡查看。</li>\n        </ol>\n        <h2>二、Gemini Pro 代充（需要您配合）</h2>\n        <ol>\n          <li>下單時填<b>要儲值的 Google 信箱</b>和<b>輔助信箱</b>，兩個都要填對。</li>\n          <li>付款後請<b>添加店主 QQ（見下方）</b>，加好友時備註您的訂單號，代充需要店主與您即時配合。</li>\n          <li>完成後會員會充到您自己的 Google 帳號裡，時長 24 個月。</li>\n        </ol>\n        <p class="hint">⚠️ 重要：全程<b>不需要提供 Google 帳號密碼</b>，店主不會向您索取密碼；任何人向您索取密碼都不要給。</p>\n        <h2>三、Muse 成品號（等收貨即可）</h2>\n        <ol>\n          <li>下單時只需填<b>聯絡方式</b>，方便店主聯絡您。</li>\n          <li>付款後店主會把<b>帳號和密碼發到您的訂單裡</b>：打開「我的訂單」，在訂單下方「交付內容」處查看，可一鍵複製。</li>\n          <li>收到後請盡快登入 muse.ai 確認帳號可用，並妥善保管帳號密碼。</li>\n          <li>「詞元」≈ AI 讀寫的文字量：1 億詞元約合數千萬漢字，10 億詞元日常聊天、寫作能用很久（約數，實際消耗看每次對話長短）。</li>\n        </ol>\n        <h2>四、付款與售後</h2>\n        <ul>\n          <li>付款後狀態長時間（超過 10 分鐘）沒有更新，請聯絡店主 QQ 並發訂單號。</li>\n          <li>所有訂單狀態以「我的訂單」頁面顯示為準。</li>\n        </ul>\n        <h2>售後與退款規則（請放心下單）</h2>\n        <ul>\n          <li><b>未交付可退</b>：訂單還沒交付（未標記「已完成」）之前，隨時聯絡店主可取消並<b>全額退款</b>。</li>\n          <li><b>退款到帳方式</b>：用餘額支付的訂單，退款即時自動返還到您的站內餘額；用支付寶支付的訂單，由店主在支付寶側原路退回。</li>\n          <li><b>Gemini 代充</b>：因店主原因沒能充上的，全額退款；填寫的信箱有誤導致充錯的，請第一時間聯絡店主核對處理；已成功儲值到帳的會員不支援無理由退款。</li>\n          <li><b>Muse 成品號</b>：保首登——交付後請盡快完成首次登入確認；首次登入不上的，請第一時間聯絡店主（帶訂單號），核實後補發或退款；首次登入成功後帳號的後續問題（含自行改密、違規使用等）不在質保範圍。</li>\n          <li>售後統一走<b>線上客服</b>或店主 QQ（見下方），請帶上訂單號。</li>\n        </ul>\n        <h2>五、儲值與線上客服</h2>\n        <ul>\n          <li><b>儲值</b>：在「我的錢包」可用支付寶提前儲值；之後下單可直接用餘額付款，不用每次跳支付寶。</li>\n          <li><b>線上客服</b>：頂部導覽「線上客服」能直接給店主留言，店主人工回覆後，導覽會有紅色數字提醒。</li>\n          <li>用餘額支付的訂單如退款，金額會自動返還到您的餘額。</li>\n        </ul>\n        </div>'}})

MORE_STRINGS = {
    "zh": {
        "home.title": "全部商品",
        "hero.tagline": "主流 AI 会员 · 代充与成品号一站购",
        "hero.cta": "开始选购",
        "track.err_notfound": "订单号或联系方式不正确，请核对后重试",
        "track.result_title": "订单查询结果",
        "track.more": "继续查询",
        "chat.me": "我",
        "chat.seller": "店主",
        "chat.customer": "客户",
        "chat.empty": "暂无消息，在下面输入框留言，店主看到后会回复。",
        "lock.msg": "尝试次数过多，请 {m} 分钟后再试",
        "guide.contact": "联系店主",
        "guide.contact_hint": "工作时间一般都会在，留言请带订单号，处理更快。",
        "legal.privacy_title": "隐私政策",
        "legal.terms_title": "用户条款",
        "legal.cookies_title": "Cookie 政策",
        "legal.updated": "更新日期：2026-11-08 · 适用于 muse798.com（曜石 AI · OBSIDIAN）",
        "legal.contact_pre": "联系：",
        "legal.contact_post": " 或店主 QQ {qq}。",
        "rpay.result_title": "储值结果",
        "rpay.credited": "已到账",
        "rpay.confirming": "确认中",
        "rpay.tip_credited": "储值已到账，可到“我的钱包”查看余额。",
        "rpay.tip_confirming": "支付结果还在确认中，请稍后到“我的钱包”刷新查看。",
        "pay.title": "支付订单",
        "pay.order_no": "订单号：",
        "pay.product": "商品：",
        "pay.amount": "应付金额：",
        "pay.balance_btn": "余额支付（余额 ¥{b}）",
        "pay.balance_low_pre": "当前余额 ¥{b}，不足以支付本单，可先",
        "pay.goto_recharge": "去储值",
        "pay.balance_low_post": "。",
        "pay.balance_zero_pre": "余额为 ¥0.00，可先",
        "pay.recharge_word": "储值",
        "pay.balance_zero_post": "后用余额直接付款。",
        "pay.epay_btn": "易支付-支付宝",
        "pay.note": "支付完成后订单会自动变为“已支付 / 待充值”，店主会按顺序为您充值。未完成支付前订单保持“待支付”，不会扣款。",
        "pay.status_title": "订单状态",
        "pay.status_amount": "金额：",
        "pay.status_now": "当前状态：",
        "pay.tip_paid": "支付已确认，店主会按顺序为您充值。",
        "pay.tip_unpaid": "支付结果还在确认中（以支付平台的异步通知为准），请稍后在“我的订单”刷新查看；若未完成支付，订单会保持待支付，不会扣款。",
        "pay.tip_other": "订单状态如上，如有疑问请联系店主。",
        "pay.view_detail": "查看订单详情",
        "wallet.title": "我的钱包",
        "wallet.balance_label": "当前余额",
        "wallet.custom_label": "或输入自定义金额（元）",
        "wallet.custom_ph": "如 30",
        "wallet.recharge_btn": "支付宝储值",
        "wallet.note": "通过支付宝付款储值，到账后下单可直接用余额付款；单次储值 ¥1–¥5000。余额暂不支持提现，余额支付的订单退款时会自动返还到余额。",
        "wallet.bonus_banner": "🎁 <b>首充活动</b>：首次储值满 ¥10 到账 <b>¥12</b>，满 ¥15 到账 <b>¥20</b>，赠送随本金自动到账，每人限一次。",
        "wallet.paid_badge": "已到账",
        "wallet.unpaid_link": "待支付 · 去付款",
        "wallet.bonus_incl": "含首充赠送 ¥{b}，实到 ¥{t}",
        "wallet.no_recharges": "暂无储值记录",
        "wallet.no_logs": "暂无收支明细",
        "wallet.records": "储值记录",
        "wallet.rc_no": "储值单号",
        "wallet.amount": "金额",
        "wallet.status": "状态",
        "wallet.time": "时间",
        "wallet.logs": "收支明细",
        "wallet.type": "类型",
        "wallet.change": "变动",
        "wallet.balance": "余额",
        "wallet.note_col": "说明",
        "wallet.member_title": "👑 会员等级",
        "wallet.member_now": "当前等级：<b>{name}</b>（共 {n} 个等级，下单自动按等级打折）",
        "wallet.lv_current": "当前等级",
        "wallet.lv_next": "下一等级",
        "wallet.lv_member": "会员等级",
        "wallet.lv_disc_all": "全场 {label}",
        "wallet.lv_disc_default": "默认会员等级",
        "wallet.lv_req": "消费满 ¥{s} 或 充值满 ¥{r} 自动升级",
        "wallet.lv_manual": "当前等级由店主手动设置 🎁（自动进度：累计消费 ¥{s} · 累计充值 ¥{r}）",
        "wallet.lv_progress": "累计消费 ¥{s} · 累计充值 ¥{r}；距{name}：消费还差 ¥{ds} 或 充值还差 ¥{dr}",
        "wallet.lv_max": "累计消费 ¥{s} · 累计充值 ¥{r}；已是最高等级 🎉",
        "wallet.err_amount": "储值金额不正确：请输入 ¥1–¥5000 之间的金额。",
        "wallet.err_expired": "页面已过期，请刷新后重试。",
        "kind.recharge": "在线储值",
        "kind.bonus": "首充赠送",
        "kind.pay": "余额支付",
        "kind.refund": "退款返还",
        "kind.admin": "店主调账",
        "rpay.title": "储值付款",
        "rpay.no": "储值单号：",
        "rpay.amount": "储值金额：",
        "rpay.bonus_hint": "🎁 这是你的首次储值，本单到账后另赠 <b>¥{b}</b>，实际到账 <b>¥{t}</b>。",
        "rpay.note": "付款成功后余额自动到账，可在“我的钱包”查看；若到账稍有延迟，网站会每分钟自动向支付平台查单确认。",
        "rpay.not_found": "储值单不存在",
        "forgot.title": "忘记密码",
        "forgot.p1": "本站暂未开通邮件自助找回。忘记密码时，请联系店主核验身份后重置：",
        "forgot.li1": "通过页面上方「在线客服」留言，或添加店主 QQ <b>{qq}</b>，并提供你的<b>注册邮箱</b>；",
        "forgot.li2": "店主核验后会在后台为你重置密码，并把新密码发给你；",
        "forgot.li3_pre": "收到新密码后，请尽快用它",
        "forgot.li3_post": "确认可用。",
        "forgot.hint": "提醒：店主不会向你索要 Google 账号密码；密码重置只通过上述方式办理，不要轻信其他渠道。",
        "forgot.back": "返回登录",
        "qq.title": "代充需要店主协助",
        "qq.copy": "复制 QQ",
        "qq.note": "添加时请备注您的订单号，店主会协助您完成代充。提醒：店主不会向您索要 Google 账号密码。",
        "qq.pre": "请添加店主 QQ",
        "nf.title": "页面不存在",
        "nf.body": "你访问的页面可能已经被移动，或者地址输入有误。",
        "nf.home": "回首页",
        "nf.guide": "看使用教程",
        "support.title": "在线客服",
        "support.intro": "店主人工回复（不是机器人），一般几分钟内回复；也可以加店主 QQ {qq} 咨询。咨询订单请带上订单号。",
        "support.ph": "输入消息，如：订单 GM…… 还没到账",
        "support.send": "发送",
        "support.err_expired": "页面已过期，请刷新后重试。",
        "orders.title": "我的订单",
        "orders.empty": "还没有订单。",
        "orders.go_order": "去下单",
        "orders.no": "订单号",
        "orders.product": "商品",
        "orders.status": "状态",
        "orders.detail": "详情",
        "orders.pay": "去支付",
        "orders.cancel": "取消订单",
        "orders.cancel_confirm": "确认取消这个订单吗？",
        "orders.cancel_confirm2": "确认取消这个订单吗？取消后无法恢复。",
        "orders.delivery_title": "📦 交付内容（账号信息）",
        "common.copy": "复制",
        "orders.gemini_qq_pre": "代充协助 QQ：",
        "orders.gemini_qq_note": "（加好友请备注订单号）",
        "detail.title": "订单详情",
        "detail.not_found": "订单不存在",
        "detail.order_no": "订单号",
        "detail.product": "商品：",
        "detail.amount": "金额：",
        "detail.created": "下单时间：",
        "detail.paid_at": "付款时间：",
        "detail.status": "当前状态：",
        "detail.usage": "使用说明",
        "detail.delivery": "交付内容",
        "detail.delivery_keep": "请妥善保存交付内容，不要转发给他人。",
        "detail.delivery_account": "📦 账号信息",
        "detail.copy_all": "复制全部",
        "detail.download_all": "下载全部交付内容",
        "detail.view_orders": "查看订单",
        "detail.continue": "继续购物",
        "detail.file_suffix": "交付内容",
        "hero.completed": "订单已完成",
        "hero.paid": "已支付，店主处理中",
        "hero.unpaid": "订单待支付",
        "hero.failed": "订单已失败",
        "hero.refunded": "订单已退款",
        "hero.cancelled": "订单已取消",
        "tip.completed": "店主已处理完成，交付内容在下方（如有）。",
        "tip.paid": "付款已确认，店主会按顺序处理，完成后交付内容会出现在本页。",
        "tip.unpaid": "完成支付后，店主才会开始处理这一单。",
        "tip.failed": "这一单处理失败，售后请联系店主 QQ 并提供订单号。",
        "tip.refunded": "这一单已退款，如有疑问请联系店主。",
        "tip.cancelled": "这一单已取消，不会被处理；如需购买请重新下单。",
        "track.title": "订单查询",
        "track.intro": "没有注册 / 没有登录也能查：输入下单后得到的<b>订单号</b>，和下单时填写的<b>联系方式</b>（需与下单时完全一致），即可查看订单状态与交付内容。",
        "track.order_no": "订单号",
        "track.order_no_ph": "如下单成功页显示的订单号",
        "track.contact": "联系方式",
        "track.contact_ph": "下单时填写的联系方式",
        "track.submit": "查询订单",
        "track.alt_pre": "已注册用户也可以",
        "track.alt_login": "登录",
        "track.alt_mid": "后在「我的订单」里查看；实在查不到，加店主 QQ ",
        "track.alt_post": " 并备注订单号咨询。",
        "order.title": "下单",
        "order.soldout_title": "已售罄",
        "order.soldout_body": "😔 这个商品刚刚售罄了，店主补货后会重新上架。",
        "order.soldout_hint": "急用可以加店主 QQ {qq} 问问，或先看看其他商品。",
        "order.back_home": "← 返回首页选其他商品",
        "order.stock_hint": "🔥 仅剩 {n} 件，付款成功即为您锁定一件。",
        "order.required": "*必填",
        "order.aux_label": "辅助邮箱",
        "order.aux_hint": "充值时遇到验证会用到，必须填写且格式正确。",
        "order.contact_label": "联系方式",
        "order.contact_ph": "微信 / 手机 / QQ，方便店主联系您",
        "order.submit": "提交订单，去支付",
        "order.after_sale_pre": "售后：未交付可全额退款；交付的账号无法登录请第一时间联系店主处理。完整规则见",
        "order.after_sale_post": "。",
        "order.one_time": "一次付清",
        "order.member_line": "👑 {name}专享 {label}，本单已减 ¥{off}",
        "order.err_expired": "页面已过期，请刷新后重试",
        "order.err_soldout": "该商品已售罄",
        "order.err_aux_required": "辅助邮箱是必填项，不能为空",
        "order.err_aux_format": "辅助邮箱格式不正确",
        "order.err_contact_required": "联系方式是必填项",
        "trust.sold": "累计已售 {n} 单",
        "trust.avg_min": "平均约 {n} 分钟交付",
        "trust.avg_hour": "平均约 {n} 小时交付",
        "trust.nopass": "全程不索要账号密码",
        "auth.register": "注册",
        "auth.register_sub": "创建一个账号，马上开始下单",
        "auth.email": "邮箱",
        "auth.password_rule": "密码（至少 8 位）",
        "auth.password_set_ph": "设置一个密码",
        "auth.have_account": "已有账号？",
        "auth.go_login": "去登录",
        "auth.login": "登录",
        "auth.login_sub": "登录后即可下单，并随时查看订单进度",
        "auth.password": "密码",
        "auth.password_ph": "请输入密码",
        "auth.no_account": "还没有账号？",
        "auth.register_now": "立即注册",
        "auth.forgot": "忘记密码",
        "auth.track_hint": "下单时没注册？可用订单号 + 联系方式",
        "auth.track_link": "免登录查单",
        "auth.err_email": "邮箱格式不正确",
        "auth.err_pw_short": "密码至少 8 位",
        "auth.err_email_taken": "这个邮箱已经注册过了，请直接登录",
        "auth.err_login": "邮箱或密码不正确",
    },
    "en": {
        "home.title": "All Products",
        "hero.tagline": "Premium AI memberships — top-ups & ready accounts, all in one place",
        "hero.cta": "Browse products",
        "track.err_notfound": "Order number or contact info is incorrect — please check and try again",
        "track.result_title": "Order Lookup Result",
        "track.more": "Track Another",
        "chat.me": "Me",
        "chat.seller": "Seller",
        "chat.customer": "Customer",
        "chat.empty": "No messages yet. Leave a message below and the seller will reply when they see it.",
        "lock.msg": "Too many attempts — please try again in {m} min",
        "guide.contact": "Contact the Seller",
        "guide.contact_hint": "The seller is usually around during working hours. Include your order number in messages for faster handling.",
        "legal.privacy_title": "Privacy Policy",
        "legal.terms_title": "Terms of Service",
        "legal.cookies_title": "Cookie Policy",
        "legal.updated": "Last updated: 2026-11-08 · Applies to muse798.com (OBSIDIAN AI)",
        "legal.contact_pre": "Contact: ",
        "legal.contact_post": " or the seller on QQ {qq}.",
        "rpay.result_title": "Top-Up Result",
        "rpay.credited": "Credited",
        "rpay.confirming": "Confirming",
        "rpay.tip_credited": "Your top-up has been credited — check the balance in My Wallet.",
        "rpay.tip_confirming": "Your payment is still being confirmed — please refresh My Wallet shortly.",
        "pay.title": "Pay for Order",
        "pay.order_no": "Order No.: ",
        "pay.product": "Product: ",
        "pay.amount": "Amount due: ",
        "pay.balance_btn": "Pay with Balance (balance ¥{b})",
        "pay.balance_low_pre": "Your balance is ¥{b}, not enough for this order. You can ",
        "pay.goto_recharge": "top up first",
        "pay.balance_low_post": ".",
        "pay.balance_zero_pre": "Your balance is ¥0.00. You can ",
        "pay.recharge_word": "top up",
        "pay.balance_zero_post": " and then pay with balance directly.",
        "pay.epay_btn": "Pay with Alipay",
        "pay.note": "After payment, the order automatically becomes \"Paid / Awaiting Delivery\" and the seller will process it in turn. Until payment completes, the order stays unpaid and nothing is charged.",
        "pay.status_title": "Order Status",
        "pay.status_amount": "Amount: ",
        "pay.status_now": "Status: ",
        "pay.tip_paid": "Payment confirmed. The seller will process your order in turn.",
        "pay.tip_unpaid": "Your payment result is still being confirmed (the payment platform's async notification is authoritative). Please refresh My Orders shortly. If payment was not completed, the order stays unpaid and nothing is charged.",
        "pay.tip_other": "The order status is shown above. Questions? Contact the seller.",
        "pay.view_detail": "View Order Details",
        "wallet.title": "My Wallet",
        "wallet.balance_label": "Current balance",
        "wallet.custom_label": "Or enter a custom amount (CNY)",
        "wallet.custom_ph": "e.g. 30",
        "wallet.recharge_btn": "Top Up with Alipay",
        "wallet.note": "Top up via Alipay; once credited, you can pay orders directly with your balance. Single top-up ¥1–¥5000. Balance cannot be withdrawn; refunds for balance-paid orders are returned to your balance automatically.",
        "wallet.bonus_banner": "🎁 <b>First top-up offer</b>: first top-up of ¥10+ credits <b>¥12</b>; ¥15+ credits <b>¥20</b>. The bonus arrives automatically with the principal. One per person.",
        "wallet.paid_badge": "Credited",
        "wallet.unpaid_link": "Unpaid · Pay now",
        "wallet.bonus_incl": "Includes first-top-up bonus ¥{b}; ¥{t} credited in total",
        "wallet.no_recharges": "No top-up records yet",
        "wallet.no_logs": "No transactions yet",
        "wallet.records": "Top-Up Records",
        "wallet.rc_no": "Top-Up No.",
        "wallet.amount": "Amount",
        "wallet.status": "Status",
        "wallet.time": "Time",
        "wallet.logs": "Transactions",
        "wallet.type": "Type",
        "wallet.change": "Change",
        "wallet.balance": "Balance",
        "wallet.note_col": "Note",
        "wallet.member_title": "👑 Membership Level",
        "wallet.member_now": "Current level: <b>{name}</b> ({n} levels in total; discounts apply automatically when ordering)",
        "wallet.lv_current": "Current",
        "wallet.lv_next": "Next",
        "wallet.lv_member": "Member",
        "wallet.lv_disc_all": "{label} sitewide",
        "wallet.lv_disc_default": "Default tier",
        "wallet.lv_req": "Auto-upgrade at ¥{s} spent or ¥{r} topped up",
        "wallet.lv_manual": "Your level was set manually by the seller 🎁 (auto progress: ¥{s} spent · ¥{r} topped up)",
        "wallet.lv_progress": "Total spent ¥{s} · total topped up ¥{r}; to {name}: ¥{ds} more in spending or ¥{dr} more in top-ups",
        "wallet.lv_max": "Total spent ¥{s} · total topped up ¥{r}; you are at the highest level 🎉",
        "wallet.err_amount": "Invalid top-up amount: please enter between ¥1 and ¥5000.",
        "wallet.err_expired": "This page has expired — please refresh and try again.",
        "kind.recharge": "Online top-up",
        "kind.bonus": "First-top-up bonus",
        "kind.pay": "Balance payment",
        "kind.refund": "Refund",
        "kind.admin": "Seller adjustment",
        "rpay.title": "Top-Up Payment",
        "rpay.no": "Top-Up No.: ",
        "rpay.amount": "Top-Up amount: ",
        "rpay.bonus_hint": "🎁 This is your first top-up: an extra <b>¥{b}</b> bonus will be credited, <b>¥{t}</b> in total.",
        "rpay.note": "After successful payment, your balance is credited automatically — check My Wallet. If crediting is slightly delayed, the site checks with the payment platform every minute.",
        "rpay.not_found": "Top-Up Not Found",
        "forgot.title": "Forgot Password",
        "forgot.p1": "Email self-service recovery is not available yet. If you forgot your password, contact the seller to verify your identity and reset it:",
        "forgot.li1": "Message us via Support at the top of the page, or add the seller on QQ <b>{qq}</b>, and provide your <b>registered email</b>;",
        "forgot.li2": "After verification, the seller will reset your password in the backend and send you the new one;",
        "forgot.li3_pre": "Once you receive the new password, please ",
        "forgot.li3_post": " as soon as possible to confirm it works.",
        "forgot.hint": "Note: the seller will never ask for your Google account password. Password resets are only handled this way — beware of other channels.",
        "forgot.back": "Back to Login",
        "qq.title": "Top-up needs the seller's help",
        "qq.copy": "Copy QQ",
        "qq.note": "Please mention your order number when adding. The seller will help you complete the top-up. Note: the seller will never ask for your Google account password.",
        "qq.pre": "Please add the seller on QQ",
        "nf.title": "Page Not Found",
        "nf.body": "The page you visited may have been moved, or the address was typed incorrectly.",
        "nf.home": "Back to Home",
        "nf.guide": "Read the Guide",
        "support.title": "Support",
        "support.intro": "The seller replies personally (not a bot), usually within a few minutes. You can also add the seller on QQ {qq}. For order questions, please include your order number.",
        "support.ph": "Type a message, e.g. Order GM... not credited yet",
        "support.send": "Send",
        "support.err_expired": "This page has expired — please refresh and try again.",
        "orders.title": "My Orders",
        "orders.empty": "No orders yet.",
        "orders.go_order": "Place an Order",
        "orders.no": "Order No.",
        "orders.product": "Product",
        "orders.status": "Status",
        "orders.detail": "Details",
        "orders.pay": "Pay Now",
        "orders.cancel": "Cancel Order",
        "orders.cancel_confirm": "Cancel this order?",
        "orders.cancel_confirm2": "Cancel this order? This cannot be undone.",
        "orders.delivery_title": "📦 Delivery (account info)",
        "common.copy": "Copy",
        "orders.gemini_qq_pre": "Top-up help QQ:",
        "orders.gemini_qq_note": "(mention your order number when adding)",
        "detail.title": "Order Details",
        "detail.not_found": "Order Not Found",
        "detail.order_no": "Order No.",
        "detail.product": "Product: ",
        "detail.amount": "Amount: ",
        "detail.created": "Ordered at: ",
        "detail.paid_at": "Paid at: ",
        "detail.status": "Status: ",
        "detail.usage": "How to Use",
        "detail.delivery": "Delivery",
        "detail.delivery_keep": "Keep your delivery content safe — do not forward it to others.",
        "detail.delivery_account": "📦 Account Info",
        "detail.copy_all": "Copy All",
        "detail.download_all": "Download Delivery",
        "detail.view_orders": "View Orders",
        "detail.continue": "Continue Shopping",
        "detail.file_suffix": "delivery",
        "hero.completed": "Order Completed",
        "hero.paid": "Paid — Seller Processing",
        "hero.unpaid": "Awaiting Payment",
        "hero.failed": "Order Failed",
        "hero.refunded": "Order Refunded",
        "hero.cancelled": "Order Cancelled",
        "tip.completed": "The seller has completed this order; the delivery is below (if any).",
        "tip.paid": "Payment confirmed. The seller processes orders in turn; the delivery will appear on this page when done.",
        "tip.unpaid": "The seller starts processing only after payment is completed.",
        "tip.failed": "This order failed to process. For after-sales, contact the seller on QQ with your order number.",
        "tip.refunded": "This order has been refunded. Questions? Contact the seller.",
        "tip.cancelled": "This order was cancelled and will not be processed. Please place a new order if you still want it.",
        "track.title": "Track Order",
        "track.intro": "No registration or login needed: enter the <b>order number</b> you received after ordering and the <b>contact info</b> you used (must match exactly) to see the order status and delivery.",
        "track.order_no": "Order number",
        "track.order_no_ph": "The order number shown after ordering",
        "track.contact": "Contact info",
        "track.contact_ph": "The contact info you used when ordering",
        "track.submit": "Track Order",
        "track.alt_pre": "Registered users can also ",
        "track.alt_login": "log in",
        "track.alt_mid": " and check My Orders. Still can't find it? Add the seller on QQ ",
        "track.alt_post": " with your order number.",
        "order.title": "Order",
        "order.soldout_title": "Sold Out",
        "order.soldout_body": "😔 This product just sold out. It will be back once the seller restocks.",
        "order.soldout_hint": "In a hurry? Add the seller on QQ {qq} or browse other products first.",
        "order.back_home": "← Back to home for other products",
        "order.stock_hint": "🔥 Only {n} left — one is reserved for you once payment succeeds.",
        "order.required": "*required",
        "order.aux_label": "Backup email",
        "order.aux_hint": "Used if verification is needed during top-up. Required, and must be a valid format.",
        "order.contact_label": "Contact info",
        "order.contact_ph": "WeChat / phone / QQ, so the seller can reach you",
        "order.submit": "Place Order & Pay",
        "order.after_sale_pre": "After-sales: full refund before delivery; if a delivered account can't log in, contact the seller right away. Full rules in the ",
        "order.after_sale_post": ".",
        "order.one_time": "one-time payment",
        "order.member_line": "👑 {name} perk: {label}, you save ¥{off} on this order",
        "order.err_expired": "This page has expired — please refresh and try again",
        "order.err_soldout": "This product is sold out",
        "order.err_aux_required": "Backup email is required and cannot be empty",
        "order.err_aux_format": "Backup email format is incorrect",
        "order.err_contact_required": "Contact info is required",
        "trust.sold": "{n} orders sold",
        "trust.avg_min": "Avg. delivery ≈ {n} min",
        "trust.avg_hour": "Avg. delivery ≈ {n} h",
        "trust.nopass": "We never ask for your account password",
        "auth.register": "Register",
        "auth.register_sub": "Create an account and start ordering right away",
        "auth.email": "Email",
        "auth.password_rule": "Password (at least 8 characters)",
        "auth.password_set_ph": "Set a password",
        "auth.have_account": "Already have an account?",
        "auth.go_login": "Log in",
        "auth.login": "Log In",
        "auth.login_sub": "Log in to order and track your orders anytime",
        "auth.password": "Password",
        "auth.password_ph": "Enter your password",
        "auth.no_account": "No account yet?",
        "auth.register_now": "Register now",
        "auth.forgot": "Forgot password",
        "auth.track_hint": "Ordered without registering? Use your order number + contact info for",
        "auth.track_link": "guest order tracking",
        "auth.err_email": "Invalid email format",
        "auth.err_pw_short": "Password must be at least 8 characters",
        "auth.err_email_taken": "This email is already registered — please log in",
        "auth.err_login": "Incorrect email or password",
    },
    "zh-TW": {
        "home.title": "全部商品",
        "hero.tagline": "主流 AI 會員 · 代充與成品號一站購",
        "hero.cta": "開始選購",
        "track.err_notfound": "訂單號或聯絡方式不正確，請核對後重試",
        "track.result_title": "訂單查詢結果",
        "track.more": "繼續查詢",
        "chat.me": "我",
        "chat.seller": "店主",
        "chat.customer": "客戶",
        "chat.empty": "暫無訊息，在下面輸入框留言，店主看到後會回覆。",
        "lock.msg": "嘗試次數過多，請 {m} 分鐘後再試",
        "guide.contact": "聯絡店主",
        "guide.contact_hint": "工作時間一般都會在，留言請帶訂單號，處理更快。",
        "legal.privacy_title": "隱私政策",
        "legal.terms_title": "用戶條款",
        "legal.cookies_title": "Cookie 政策",
        "legal.updated": "更新日期：2026-11-08 · 適用於 muse798.com（曜石 AI · OBSIDIAN）",
        "legal.contact_pre": "聯絡：",
        "legal.contact_post": " 或店主 QQ {qq}。",
        "rpay.result_title": "儲值結果",
        "rpay.credited": "已到帳",
        "rpay.confirming": "確認中",
        "rpay.tip_credited": "儲值已到帳，可到「我的錢包」查看餘額。",
        "rpay.tip_confirming": "付款結果還在確認中，請稍後到「我的錢包」重新整理查看。",
        "pay.title": "付款訂單",
        "pay.order_no": "訂單號：",
        "pay.product": "商品：",
        "pay.amount": "應付金額：",
        "pay.balance_btn": "餘額付款（餘額 ¥{b}）",
        "pay.balance_low_pre": "當前餘額 ¥{b}，不足以支付本單，可先",
        "pay.goto_recharge": "去儲值",
        "pay.balance_low_post": "。",
        "pay.balance_zero_pre": "餘額為 ¥0.00，可先",
        "pay.recharge_word": "儲值",
        "pay.balance_zero_post": "後用餘額直接付款。",
        "pay.epay_btn": "易支付-支付寶",
        "pay.note": "付款完成後訂單會自動變為「已付款 / 待儲值」，店主會按順序為您儲值。未完成付款前訂單保持「待付款」，不會扣款。",
        "pay.status_title": "訂單狀態",
        "pay.status_amount": "金額：",
        "pay.status_now": "當前狀態：",
        "pay.tip_paid": "付款已確認，店主會按順序為您儲值。",
        "pay.tip_unpaid": "付款結果還在確認中（以付款平台的非同步通知為準），請稍後在「我的訂單」重新整理查看；若未完成付款，訂單會保持待付款，不會扣款。",
        "pay.tip_other": "訂單狀態如上，如有疑問請聯絡店主。",
        "pay.view_detail": "查看訂單詳情",
        "wallet.title": "我的錢包",
        "wallet.balance_label": "當前餘額",
        "wallet.custom_label": "或輸入自訂金額（元）",
        "wallet.custom_ph": "如 30",
        "wallet.recharge_btn": "支付寶儲值",
        "wallet.note": "透過支付寶付款儲值，到帳後下單可直接用餘額付款；單次儲值 ¥1–¥5000。餘額暫不支援提現，餘額支付的訂單退款時會自動返還到餘額。",
        "wallet.bonus_banner": "🎁 <b>首充活動</b>：首次儲值滿 ¥10 到帳 <b>¥12</b>，滿 ¥15 到帳 <b>¥20</b>，贈送隨本金自動到帳，每人限一次。",
        "wallet.paid_badge": "已到帳",
        "wallet.unpaid_link": "待付款 · 去付款",
        "wallet.bonus_incl": "含首充贈送 ¥{b}，實到 ¥{t}",
        "wallet.no_recharges": "暫無儲值記錄",
        "wallet.no_logs": "暫無收支明細",
        "wallet.records": "儲值記錄",
        "wallet.rc_no": "儲值單號",
        "wallet.amount": "金額",
        "wallet.status": "狀態",
        "wallet.time": "時間",
        "wallet.logs": "收支明細",
        "wallet.type": "類型",
        "wallet.change": "變動",
        "wallet.balance": "餘額",
        "wallet.note_col": "說明",
        "wallet.member_title": "👑 會員等級",
        "wallet.member_now": "當前等級：<b>{name}</b>（共 {n} 個等級，下單自動按等級打折）",
        "wallet.lv_current": "當前等級",
        "wallet.lv_next": "下一等級",
        "wallet.lv_member": "會員等級",
        "wallet.lv_disc_all": "全場 {label}",
        "wallet.lv_disc_default": "預設會員等級",
        "wallet.lv_req": "消費滿 ¥{s} 或 儲值滿 ¥{r} 自動升級",
        "wallet.lv_manual": "當前等級由店主手動設定 🎁（自動進度：累計消費 ¥{s} · 累計儲值 ¥{r}）",
        "wallet.lv_progress": "累計消費 ¥{s} · 累計儲值 ¥{r}；距{name}：消費還差 ¥{ds} 或 儲值還差 ¥{dr}",
        "wallet.lv_max": "累計消費 ¥{s} · 累計儲值 ¥{r}；已是最高等級 🎉",
        "wallet.err_amount": "儲值金額不正確：請輸入 ¥1–¥5000 之間的金額。",
        "wallet.err_expired": "頁面已過期，請重新整理後重試。",
        "kind.recharge": "線上儲值",
        "kind.bonus": "首充贈送",
        "kind.pay": "餘額支付",
        "kind.refund": "退款返還",
        "kind.admin": "店主調帳",
        "rpay.title": "儲值付款",
        "rpay.no": "儲值單號：",
        "rpay.amount": "儲值金額：",
        "rpay.bonus_hint": "🎁 這是你的首次儲值，本單到帳後另贈 <b>¥{b}</b>，實際到帳 <b>¥{t}</b>。",
        "rpay.note": "付款成功後餘額自動到帳，可在「我的錢包」查看；若到帳稍有延遲，網站會每分鐘自動向付款平台查單確認。",
        "rpay.not_found": "儲值單不存在",
        "forgot.title": "忘記密碼",
        "forgot.p1": "本站暫未開通郵件自助找回。忘記密碼時，請聯絡店主核驗身分後重設：",
        "forgot.li1": "透過頁面上方「線上客服」留言，或添加店主 QQ <b>{qq}</b>，並提供你的<b>註冊信箱</b>；",
        "forgot.li2": "店主核驗後會在後台為你重設密碼，並把新密碼發給你；",
        "forgot.li3_pre": "收到新密碼後，請盡快用它",
        "forgot.li3_post": "確認可用。",
        "forgot.hint": "提醒：店主不會向你索取 Google 帳號密碼；密碼重設只透過上述方式辦理，不要輕信其他管道。",
        "forgot.back": "返回登入",
        "qq.title": "代充需要店主協助",
        "qq.copy": "複製 QQ",
        "qq.note": "添加時請備註您的訂單號，店主會協助您完成代充。提醒：店主不會向您索取 Google 帳號密碼。",
        "qq.pre": "請添加店主 QQ",
        "nf.title": "頁面不存在",
        "nf.body": "你造訪的頁面可能已經被移動，或者地址輸入有誤。",
        "nf.home": "回首頁",
        "nf.guide": "看使用教學",
        "support.title": "線上客服",
        "support.intro": "店主人工回覆（不是機器人），一般幾分鐘內回覆；也可以加店主 QQ {qq} 諮詢。諮詢訂單請帶上訂單號。",
        "support.ph": "輸入訊息，如：訂單 GM…… 還沒到帳",
        "support.send": "傳送",
        "support.err_expired": "頁面已過期，請重新整理後重試。",
        "orders.title": "我的訂單",
        "orders.empty": "還沒有訂單。",
        "orders.go_order": "去下單",
        "orders.no": "訂單號",
        "orders.product": "商品",
        "orders.status": "狀態",
        "orders.detail": "詳情",
        "orders.pay": "去付款",
        "orders.cancel": "取消訂單",
        "orders.cancel_confirm": "確認取消這個訂單嗎？",
        "orders.cancel_confirm2": "確認取消這個訂單嗎？取消後無法恢復。",
        "orders.delivery_title": "📦 交付內容（帳號資訊）",
        "common.copy": "複製",
        "orders.gemini_qq_pre": "代充協助 QQ：",
        "orders.gemini_qq_note": "（加好友請備註訂單號）",
        "detail.title": "訂單詳情",
        "detail.not_found": "訂單不存在",
        "detail.order_no": "訂單號",
        "detail.product": "商品：",
        "detail.amount": "金額：",
        "detail.created": "下單時間：",
        "detail.paid_at": "付款時間：",
        "detail.status": "當前狀態：",
        "detail.usage": "使用說明",
        "detail.delivery": "交付內容",
        "detail.delivery_keep": "請妥善保存交付內容，不要轉發給他人。",
        "detail.delivery_account": "📦 帳號資訊",
        "detail.copy_all": "複製全部",
        "detail.download_all": "下載全部交付內容",
        "detail.view_orders": "查看訂單",
        "detail.continue": "繼續購物",
        "detail.file_suffix": "交付內容",
        "hero.completed": "訂單已完成",
        "hero.paid": "已付款，店主處理中",
        "hero.unpaid": "訂單待付款",
        "hero.failed": "訂單已失敗",
        "hero.refunded": "訂單已退款",
        "hero.cancelled": "訂單已取消",
        "tip.completed": "店主已處理完成，交付內容在下方（如有）。",
        "tip.paid": "付款已確認，店主會按順序處理，完成後交付內容會出現在本頁。",
        "tip.unpaid": "完成付款後，店主才會開始處理這一單。",
        "tip.failed": "這一單處理失敗，售後請聯絡店主 QQ 並提供訂單號。",
        "tip.refunded": "這一單已退款，如有疑問請聯絡店主。",
        "tip.cancelled": "這一單已取消，不會被處理；如需購買請重新下單。",
        "track.title": "訂單查詢",
        "track.intro": "沒有註冊 / 沒有登入也能查：輸入下單後得到的<b>訂單號</b>，和下單時填寫的<b>聯絡方式</b>（需與下單時完全一致），即可查看訂單狀態與交付內容。",
        "track.order_no": "訂單號",
        "track.order_no_ph": "如下單成功頁顯示的訂單號",
        "track.contact": "聯絡方式",
        "track.contact_ph": "下單時填寫的聯絡方式",
        "track.submit": "查詢訂單",
        "track.alt_pre": "已註冊用戶也可以",
        "track.alt_login": "登入",
        "track.alt_mid": "後在「我的訂單」裡查看；實在查不到，加店主 QQ ",
        "track.alt_post": " 並備註訂單號諮詢。",
        "order.title": "下單",
        "order.soldout_title": "已售罄",
        "order.soldout_body": "😔 這個商品剛剛售罄了，店主補貨後會重新上架。",
        "order.soldout_hint": "急用可以加店主 QQ {qq} 問問，或先看看其他商品。",
        "order.back_home": "← 返回首頁選其他商品",
        "order.stock_hint": "🔥 僅剩 {n} 件，付款成功即為您鎖定一件。",
        "order.required": "*必填",
        "order.aux_label": "輔助信箱",
        "order.aux_hint": "儲值時遇到驗證會用到，必須填寫且格式正確。",
        "order.contact_label": "聯絡方式",
        "order.contact_ph": "微信 / 手機 / QQ，方便店主聯絡您",
        "order.submit": "提交訂單，去付款",
        "order.after_sale_pre": "售後：未交付可全額退款；交付的帳號無法登入請第一時間聯絡店主處理。完整規則見",
        "order.after_sale_post": "。",
        "order.one_time": "一次付清",
        "order.member_line": "👑 {name}專享 {label}，本單已減 ¥{off}",
        "order.err_expired": "頁面已過期，請重新整理後重試",
        "order.err_soldout": "該商品已售罄",
        "order.err_aux_required": "輔助信箱是必填項，不能為空",
        "order.err_aux_format": "輔助信箱格式不正確",
        "order.err_contact_required": "聯絡方式是必填項",
        "trust.sold": "累計已售 {n} 單",
        "trust.avg_min": "平均約 {n} 分鐘交付",
        "trust.avg_hour": "平均約 {n} 小時交付",
        "trust.nopass": "全程不索取帳號密碼",
        "auth.register": "註冊",
        "auth.register_sub": "建立一個帳號，馬上開始下單",
        "auth.email": "信箱",
        "auth.password_rule": "密碼（至少 8 位）",
        "auth.password_set_ph": "設定一個密碼",
        "auth.have_account": "已有帳號？",
        "auth.go_login": "去登入",
        "auth.login": "登入",
        "auth.login_sub": "登入後即可下單，並隨時查看訂單進度",
        "auth.password": "密碼",
        "auth.password_ph": "請輸入密碼",
        "auth.no_account": "還沒有帳號？",
        "auth.register_now": "立即註冊",
        "auth.forgot": "忘記密碼",
        "auth.track_hint": "下單時沒註冊？可用訂單號 + 聯絡方式",
        "auth.track_link": "免登入查單",
        "auth.err_email": "信箱格式不正確",
        "auth.err_pw_short": "密碼至少 8 位",
        "auth.err_email_taken": "這個信箱已經註冊過了，請直接登入",
        "auth.err_login": "信箱或密碼不正確",
    },
}
for _lang, _tbl in MORE_STRINGS.items():
    STRINGS.setdefault(_lang, {}).update(_tbl)

for _mod_name in ("i18n_ja_ko", "i18n_fr_de_es", "i18n_pt_ru",
                  "i18n_extra"):
    try:
        import importlib
        merge_extra(importlib.import_module(_mod_name))
    except Exception:
        pass


def product_text(lang, pid, zh_name, zh_points):
    """返回 (name, points)：zh 直接用原文；其他语言有译文用译文，
    否则回退 en，再回退中文。"""
    if lang == "zh":
        return zh_name, zh_points
    for cand in (lang, "en"):
        entry = (PRODUCT_I18N.get(cand) or {}).get(pid)
        if entry:
            return entry["name"], list(entry["points"])
    return zh_name, zh_points


def product_field(lang, pid, field, zh_value):
    """取商品的单个本地化字段（desc / first_label / password_hint）；
    zh 直接用原文。"""
    if lang == "zh":
        return zh_value
    for cand in (lang, "en"):
        entry = (PRODUCT_I18N.get(cand) or {}).get(pid)
        if entry and entry.get(field):
            return entry[field]
    return zh_value


def blob(lang, kind):
    if lang == "zh":
        return None
    for cand in (lang, "en"):
        val = (BLOBS.get(cand) or {}).get(kind)
        if val:
            return val
    return None
