#!/usr/bin/env python3
"""曜石 AI · OBSIDIAN —— 单文件 Web 应用（仅 Python 标准库）。

功能：商品页、邮箱注册/登录、下单（辅助邮箱必填）、我的订单、
支付宝/微信官方直连支付（含回调验签改单）、卖家后台处理订单。

运行：python3 app.py   （环境变量 PORT / HOST / GEMINI_DB 可选）
首次启动：若设置了 GEMINI_ADMIN_EMAIL 和 GEMINI_ADMIN_PASSWORD，
且管理员账号不存在，会自动创建管理员。
"""
import hashlib
import html
import json
import os
import re
import secrets
import sqlite3
import threading
import time
from datetime import datetime
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, quote, urlparse

import config
import i18n
import notify
import payments
import qrcode_gen

# ------------------------------------------------------ 多语言（upgrade19）
# 当前请求语言放在线程本地里：由 Handler._resolve_lang 按
# Cookie lang → Accept-Language → zh 的顺序在分发前设定。
# 中文是源语言：模板里的中文原文即 zh 文案，其他语言经 T() 覆盖，
# 缺失译文回退 en → zh。卖家后台不本地化（店主自用）。
_LANG = threading.local()


def cur_lang():
    return getattr(_LANG, "lang", "zh")


def set_cur_lang(lang):
    _LANG.lang = lang if lang in i18n.LANG_CODES else "zh"


def T(key, **kw):
    return i18n.tr(cur_lang(), key, **kw)


def SL(status):
    """客户侧订单状态文案（按当前语言）；后台仍用 STATUS_LABELS。"""
    if cur_lang() == "zh":
        return STATUS_LABELS.get(status, status)
    return i18n.tr(cur_lang(), f"status.{status}")


def loc_product(p):
    """(本地化商品名, 本地化 points)；无译文时回退中文原文。"""
    return i18n.product_text(cur_lang(), p["id"], p["name"],
                             p["points"])


def loc_field(p, field):
    """商品单个字段的本地化值（desc / first_label 等）。"""
    return i18n.product_field(cur_lang(), p["id"], field, p[field])


def loc_level(lvl):
    """(本地化等级名, 本地化折扣标签)；中文用 LEVELS 原文。"""
    if cur_lang() == "zh":
        return LEVELS[lvl]["name"], LEVELS[lvl]["label"]
    table = (i18n.LEVEL_I18N.get(cur_lang())
             or i18n.LEVEL_I18N.get("en") or [])
    if 0 <= lvl < len(table):
        return table[lvl]
    return LEVELS[lvl]["name"], LEVELS[lvl]["label"]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.environ.get("GEMINI_DB", os.path.join(BASE_DIR, "store.db"))

PRODUCTS = [
    {
        "id": "gemini-pro-24m",
        "name": "Gemini Pro 24个月代充",
        "price_cents": 2880,
        "price_suffix": "一次付清",
        "price_note": "/ 24 个月 · 一次付清",
        "official_price": "¥3,480",
        "official_note": "官方 $19.99/月 ≈ ¥145/月 · 24 个月约",
        "save_text": "省 ¥3,400+",
        # 开站前私域历史销量，店主提供
        "sold_base": 778,
        "desc": ("Gemini Pro 会员代充服务，时长 24 个月。付款后由店主为您 "
                 "填写的 Google 账号人工完成充值，全程不需要提供账号密码。"),
        "points": [
            "代充到您自己的 Google 账号，会员时长 24 个月",
            "全程不需要提供账号密码，只需充值邮箱与辅助邮箱",
            "支持支付宝付款",
            "付款后人工充值，进度可在“我的订单”实时查看",
        ],
        "first_label": "要充值的 Google 账号邮箱",
        "first_err": "要充值的 Google 账号邮箱格式不正确",
        "password_hint": "我们不会在任何环节向您索要 Google 账号密码。",
        "needs_email": True,
        "cat": "gemini", "cat_label": "GOOGLE",
        "tint": "#E7F0EA",
        "icon": """<svg width="52" height="52" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 65 65"><mask id="maskme" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="0" y="0" width="65" height="65"><path d="M32.447 0c.68 0 1.273.465 1.439 1.125a38.904 38.904 0 001.999 5.905c2.152 5 5.105 9.376 8.854 13.125 3.751 3.75 8.126 6.703 13.125 8.855a38.98 38.98 0 005.906 1.999c.66.166 1.124.758 1.124 1.438 0 .68-.464 1.273-1.125 1.439a38.902 38.902 0 00-5.905 1.999c-5 2.152-9.375 5.105-13.125 8.854-3.749 3.751-6.702 8.126-8.854 13.125a38.973 38.973 0 00-2 5.906 1.485 1.485 0 01-1.438 1.124c-.68 0-1.272-.464-1.438-1.125a38.913 38.913 0 00-2-5.905c-2.151-5-5.103-9.375-8.854-13.125-3.75-3.749-8.125-6.702-13.125-8.854a38.973 38.973 0 00-5.905-2A1.485 1.485 0 010 32.448c0-.68.465-1.272 1.125-1.438a38.903 38.903 0 005.905-2c5-2.151 9.376-5.104 13.125-8.854 3.75-3.749 6.703-8.125 8.855-13.125a38.972 38.972 0 001.999-5.905A1.485 1.485 0 0132.447 0z" fill="#000"/><path d="M32.447 0c.68 0 1.273.465 1.439 1.125a38.904 38.904 0 001.999 5.905c2.152 5 5.105 9.376 8.854 13.125 3.751 3.75 8.126 6.703 13.125 8.855a38.98 38.98 0 005.906 1.999c.66.166 1.124.758 1.124 1.438 0 .68-.464 1.273-1.125 1.439a38.902 38.902 0 00-5.905 1.999c-5 2.152-9.375 5.105-13.125 8.854-3.749 3.751-6.702 8.126-8.854 13.125a38.973 38.973 0 00-2 5.906 1.485 1.485 0 01-1.438 1.124c-.68 0-1.272-.464-1.438-1.125a38.913 38.913 0 00-2-5.905c-2.151-5-5.103-9.375-8.854-13.125-3.75-3.749-8.125-6.702-13.125-8.854a38.973 38.973 0 00-5.905-2A1.485 1.485 0 010 32.448c0-.68.465-1.272 1.125-1.438a38.903 38.903 0 005.905-2c5-2.151 9.376-5.104 13.125-8.854 3.75-3.749 6.703-8.125 8.855-13.125a38.972 38.972 0 001.999-5.905A1.485 1.485 0 0132.447 0z" fill="url(#prefix__paint0_linear_2001_67)"/></mask><g mask="url(#maskme)"><g filter="url(#prefix__filter0_f_2001_67)"><path d="M-5.859 50.734c7.498 2.663 16.116-2.33 19.249-11.152 3.133-8.821-.406-18.131-7.904-20.794-7.498-2.663-16.116 2.33-19.25 11.151-3.132 8.822.407 18.132 7.905 20.795z" fill="#FFE432"/></g><g filter="url(#prefix__filter1_f_2001_67)"><path d="M27.433 21.649c10.3 0 18.651-8.535 18.651-19.062 0-10.528-8.35-19.062-18.651-19.062S8.78-7.94 8.78 2.587c0 10.527 8.35 19.062 18.652 19.062z" fill="#FC413D"/></g><g filter="url(#prefix__filter2_f_2001_67)"><path d="M20.184 82.608c10.753-.525 18.918-12.244 18.237-26.174-.68-13.93-9.95-24.797-20.703-24.271C6.965 32.689-1.2 44.407-.519 58.337c.681 13.93 9.95 24.797 20.703 24.271z" fill="#00B95C"/></g><g filter="url(#prefix__filter3_f_2001_67)"><path d="M20.184 82.608c10.753-.525 18.918-12.244 18.237-26.174-.68-13.93-9.95-24.797-20.703-24.271C6.965 32.689-1.2 44.407-.519 58.337c.681 13.93 9.95 24.797 20.703 24.271z" fill="#00B95C"/></g><g filter="url(#prefix__filter4_f_2001_67)"><path d="M30.954 74.181c9.014-5.485 11.427-17.976 5.389-27.9-6.038-9.925-18.241-13.524-27.256-8.04-9.015 5.486-11.428 17.977-5.39 27.902 6.04 9.924 18.242 13.523 27.257 8.038z" fill="#00B95C"/></g><g filter="url(#prefix__filter5_f_2001_67)"><path d="M67.391 42.993c10.132 0 18.346-7.91 18.346-17.666 0-9.757-8.214-17.667-18.346-17.667s-18.346 7.91-18.346 17.667c0 9.757 8.214 17.666 18.346 17.666z" fill="#3186FF"/></g><g filter="url(#prefix__filter6_f_2001_67)"><path d="M-13.065 40.944c9.33 7.094 22.959 4.869 30.442-4.972 7.483-9.84 5.987-23.569-3.343-30.663C4.704-1.786-8.924.439-16.408 10.28c-7.483 9.84-5.986 23.57 3.343 30.664z" fill="#FBBC04"/></g><g filter="url(#prefix__filter7_f_2001_67)"><path d="M34.74 51.43c11.135 7.656 25.896 5.524 32.968-4.764 7.073-10.287 3.779-24.832-7.357-32.488C49.215 6.52 34.455 8.654 27.382 18.94c-7.072 10.288-3.779 24.833 7.357 32.49z" fill="#3186FF"/></g><g filter="url(#prefix__filter8_f_2001_67)"><path d="M54.984-2.336c2.833 3.852-.808 11.34-8.131 16.727-7.324 5.387-15.557 6.631-18.39 2.78-2.833-3.853.807-11.342 8.13-16.728 7.324-5.387 15.558-6.631 18.39-2.78z" fill="#749BFF"/></g><g filter="url(#prefix__filter9_f_2001_67)"><path d="M31.727 16.104C43.053 5.598 46.94-8.626 40.41-15.666c-6.53-7.04-21.006-4.232-32.332 6.274s-15.214 24.73-8.683 31.77c6.53 7.04 21.006 4.232 32.332-6.274z" fill="#FC413D"/></g><g filter="url(#prefix__filter10_f_2001_67)"><path d="M8.51 53.838c6.732 4.818 14.46 5.55 17.262 1.636 2.802-3.915-.384-10.994-7.116-15.812-6.731-4.818-14.46-5.55-17.261-1.636-2.802 3.915.383 10.994 7.115 15.812z" fill="#FFEE48"/></g></g><defs><filter id="prefix__filter0_f_2001_67" x="-19.824" y="13.152" width="39.274" height="43.217" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation="2.46" result="effect1_foregroundBlur_2001_67"/></filter><filter id="prefix__filter1_f_2001_67" x="-15.001" y="-40.257" width="84.868" height="85.688" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation="11.891" result="effect1_foregroundBlur_2001_67"/></filter><filter id="prefix__filter2_f_2001_67" x="-20.776" y="11.927" width="79.454" height="90.916" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation="10.109" result="effect1_foregroundBlur_2001_67"/></filter><filter id="prefix__filter3_f_2001_67" x="-20.776" y="11.927" width="79.454" height="90.916" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation="10.109" result="effect1_foregroundBlur_2001_67"/></filter><filter id="prefix__filter4_f_2001_67" x="-19.845" y="15.459" width="79.731" height="81.505" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation="10.109" result="effect1_foregroundBlur_2001_67"/></filter><filter id="prefix__filter5_f_2001_67" x="29.832" y="-11.552" width="75.117" height="73.758" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation="9.606" result="effect1_foregroundBlur_2001_67"/></filter><filter id="prefix__filter6_f_2001_67" x="-38.583" y="-16.253" width="78.135" height="78.758" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation="8.706" result="effect1_foregroundBlur_2001_67"/></filter><filter id="prefix__filter7_f_2001_67" x="8.107" y="-5.966" width="78.877" height="77.539" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation="7.775" result="effect1_foregroundBlur_2001_67"/></filter><filter id="prefix__filter8_f_2001_67" x="13.587" y="-18.488" width="56.272" height="51.81" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation="6.957" result="effect1_foregroundBlur_2001_67"/></filter><filter id="prefix__filter9_f_2001_67" x="-15.526" y="-31.297" width="70.856" height="69.306" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation="5.876" result="effect1_foregroundBlur_2001_67"/></filter><filter id="prefix__filter10_f_2001_67" x="-14.168" y="20.964" width="55.501" height="51.571" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation="7.273" result="effect1_foregroundBlur_2001_67"/></filter><linearGradient id="prefix__paint0_linear_2001_67" x1="18.447" y1="43.42" x2="52.153" y2="15.004" gradientUnits="userSpaceOnUse"><stop stop-color="#4893FC"/><stop offset=".27" stop-color="#4893FC"/><stop offset=".777" stop-color="#969DFF"/><stop offset="1" stop-color="#BD99FE"/></linearGradient></defs></svg>""",
    },
    {
        "id": "muse-account-1b",
        "name": "Muse 成品号 · 10亿词元",
        "price_cents": 500,
        "price_suffix": "一次付清",
        "price_note": "/ 个 · 一次付清",
        "desc": ("Muse 成品号，内含 10 亿词元额度。付款后由店主人工发货，"
                 "通过您填写的联系方式交付账号。"),
        "points": [
            "成品号，内含 10 亿词元额度",
            "先说人话：词元 ≈ AI 读写的文字量，10 亿词元约合数亿汉字，日常聊天、写作能用很久（约数，实际消耗看每次对话长短）",
            "付款后由店主人工发货，通过联系方式交付账号",
            "支持支付宝付款",
            "发货进度可在“我的订单”实时查看",
        ],
        "first_label": "接收账号的邮箱",
        "first_err": "接收账号的邮箱格式不正确",
        "password_hint": "付款后店主会通过您填写的联系方式交付账号，请确保联系方式准确无误。",
        "needs_email": False,
        "cat": "muse", "cat_label": "MUSE",
        "tint": "#EFEAFB",
        # 开站前私域历史销量，店主提供
        "sold_base": 556,
        "initial_stock": 20,
        "icon": """<svg viewBox="0 0 100 100" width="54" height="54" fill="none"><path d="M24.6257 16.1214C28.2365 16.1214 30.8187 18.9408 30.8187 23.3643C30.8185 27.7868 30.1055 31.7765 28.9225 40.2466C28.0743 46.1813 26.62 55.2418 26.0132 59.0088C27.1782 56.7815 29.9074 51.5757 30.3914 50.5982C36.1081 39.061 42.0657 28.7544 43.7826 26.0254C46.0594 22.382 48.062 20.9229 51.1597 20.9229C52.7685 20.923 54.6826 21.7357 55.6315 22.819C56.9178 24.2895 57.1859 26.6602 57.1411 29.244C57.0738 33.2073 56.5599 39.5264 55.8553 46.5698C55.5416 49.7057 54.9365 56.1066 54.5288 60.4004C58.1883 53.8532 64.9609 41.8109 67.6921 37.6058C70.0727 33.9402 72.466 31.5797 75.6836 31.5796C78.4595 31.5796 81.8809 33.5416 81.6772 38.7573C81.3774 46.4556 80.2673 63.2232 79.7607 70.7479C83.1662 65.7913 87.6377 58.4543 89.3148 55.6966C91.0104 52.908 92.75 50.6542 95.3898 50.5778C98.0987 50.4995 99.913 52.341 99.9959 55.1839C100.078 58.0277 98.3835 61.2256 96.1344 64.856C93.6937 68.7957 90.9621 73.0123 87.6383 76.9491C84.3148 80.8856 81.2604 83.8782 76.5991 83.8786C72.4243 83.8786 69.4869 81.1043 69.283 76.0254C69.1768 73.364 69.6804 67.6405 70.0602 63.1673C70.5 57.9875 71.0315 52.9861 71.403 49.6786C67.7337 56.3979 60.0101 70.4676 56.5348 75.9603C53.1343 81.3339 51.4774 83.2269 47.8882 83.2275C44.2977 83.2275 42.7226 80.6416 42.6717 76.7497C42.6142 72.5285 45.7852 47.1821 46.8587 38.737C45.1183 42.4616 40.839 51.6056 38.1551 57.0435C35.5587 62.3055 31.204 71.3978 28.0436 76.6357C25.7668 80.4094 23.2092 83.2273 19.4173 83.2275C15.6252 83.2275 13.4847 80.6784 13.4847 76.5788C13.4847 72.4794 14.6716 65.6492 15.9465 57.1777C16.5839 53.0781 17.3108 48.6133 18.1315 43.8761C18.7324 40.448 19.7764 34.4169 20.4183 30.7129C17.502 35.2539 12.2536 43.4278 10.6567 45.8903C8.88113 48.6291 7.28747 50.626 4.64681 50.6266C1.7329 50.6266 0.000532901 48.3522 0 45.7113C0 43.0703 1.34323 41.0344 3.52376 37.4512C6.32403 32.8465 11.3578 26.57 14.1154 23.2747C17.3656 19.3912 20.6139 16.1219 24.6257 16.1214Z" fill="url(#mg)"/><defs><linearGradient id="mg" x1="133.245" y1="109.046" x2="24.9203" y2="-12.5565" gradientUnits="userSpaceOnUse"><stop offset="0.254808" stop-color="#0082FB"/><stop offset="0.697115" stop-color="#0064E0"/><stop offset="1" stop-color="#0040DC"/></linearGradient></defs></svg>""",
    },
    {
        "id": "muse-2b",
        "name": "Muse · 20亿词元",
        "price_cents": 700,
        "price_suffix": "一次付清",
        "price_note": "/ 份 · 一次付清",
        "desc": ("Muse，20 亿词元。付款后由店主人工处理，"
                 "通过您填写的联系方式交付。"),
        "points": [
            "Muse，含 20 亿词元",
            "先说人话：词元 ≈ AI 读写的文字量，20 亿是 10 亿的两倍，天天重度用也耐用（约数，实际消耗看每次对话长短）",
            "付款后由店主人工处理，通过联系方式交付",
            "支持支付宝付款",
            "处理进度可在“我的订单”实时查看",
        ],
        "first_label": "接收邮箱",
        "first_err": "接收邮箱格式不正确",
        "password_hint": "付款后店主会通过您填写的联系方式交付，请确保联系方式准确无误。",
        "needs_email": False,
        "cat": "muse", "cat_label": "MUSE",
        "tint": "#FDF0E4",
        # 开站前私域历史销量，店主提供
        "sold_base": 1996,
        "initial_stock": 20,
        "icon": """<svg viewBox="0 0 100 100" width="54" height="54" fill="none"><path d="M24.6257 16.1214C28.2365 16.1214 30.8187 18.9408 30.8187 23.3643C30.8185 27.7868 30.1055 31.7765 28.9225 40.2466C28.0743 46.1813 26.62 55.2418 26.0132 59.0088C27.1782 56.7815 29.9074 51.5757 30.3914 50.5982C36.1081 39.061 42.0657 28.7544 43.7826 26.0254C46.0594 22.382 48.062 20.9229 51.1597 20.9229C52.7685 20.923 54.6826 21.7357 55.6315 22.819C56.9178 24.2895 57.1859 26.6602 57.1411 29.244C57.0738 33.2073 56.5599 39.5264 55.8553 46.5698C55.5416 49.7057 54.9365 56.1066 54.5288 60.4004C58.1883 53.8532 64.9609 41.8109 67.6921 37.6058C70.0727 33.9402 72.466 31.5797 75.6836 31.5796C78.4595 31.5796 81.8809 33.5416 81.6772 38.7573C81.3774 46.4556 80.2673 63.2232 79.7607 70.7479C83.1662 65.7913 87.6377 58.4543 89.3148 55.6966C91.0104 52.908 92.75 50.6542 95.3898 50.5778C98.0987 50.4995 99.913 52.341 99.9959 55.1839C100.078 58.0277 98.3835 61.2256 96.1344 64.856C93.6937 68.7957 90.9621 73.0123 87.6383 76.9491C84.3148 80.8856 81.2604 83.8782 76.5991 83.8786C72.4243 83.8786 69.4869 81.1043 69.283 76.0254C69.1768 73.364 69.6804 67.6405 70.0602 63.1673C70.5 57.9875 71.0315 52.9861 71.403 49.6786C67.7337 56.3979 60.0101 70.4676 56.5348 75.9603C53.1343 81.3339 51.4774 83.2269 47.8882 83.2275C44.2977 83.2275 42.7226 80.6416 42.6717 76.7497C42.6142 72.5285 45.7852 47.1821 46.8587 38.737C45.1183 42.4616 40.839 51.6056 38.1551 57.0435C35.5587 62.3055 31.204 71.3978 28.0436 76.6357C25.7668 80.4094 23.2092 83.2273 19.4173 83.2275C15.6252 83.2275 13.4847 80.6784 13.4847 76.5788C13.4847 72.4794 14.6716 65.6492 15.9465 57.1777C16.5839 53.0781 17.3108 48.6133 18.1315 43.8761C18.7324 40.448 19.7764 34.4169 20.4183 30.7129C17.502 35.2539 12.2536 43.4278 10.6567 45.8903C8.88113 48.6291 7.28747 50.626 4.64681 50.6266C1.7329 50.6266 0.000532901 48.3522 0 45.7113C0 43.0703 1.34323 41.0344 3.52376 37.4512C6.32403 32.8465 11.3578 26.57 14.1154 23.2747C17.3656 19.3912 20.6139 16.1219 24.6257 16.1214Z" fill="url(#mg)"/><defs><linearGradient id="mg" x1="133.245" y1="109.046" x2="24.9203" y2="-12.5565" gradientUnits="userSpaceOnUse"><stop offset="0.254808" stop-color="#0082FB"/><stop offset="0.697115" stop-color="#0064E0"/><stop offset="1" stop-color="#0040DC"/></linearGradient></defs></svg>""",
    },
    {
        "id": "muse3-1b",
        "name": "Muse · 310亿词元",
        "price_cents": 1500,
        "price_suffix": "一次付清",
        "price_note": "/ 份 · 一次付清",
        "desc": ("Muse，310 亿词元。付款后由店主人工处理，"
                 "通过您填写的联系方式交付。"),
        "points": [
            "Muse，含 310 亿词元",
            "先说人话：词元 ≈ AI 读写的文字量，310 亿约为 10 亿的 31 倍，适合长期高频使用（约数，实际消耗看每次对话长短）",
            "付款后由店主人工处理，通过联系方式交付",
            "支持支付宝付款",
            "处理进度可在“我的订单”实时查看",
        ],
        "first_label": "接收邮箱",
        "first_err": "接收邮箱格式不正确",
        "password_hint": "付款后店主会通过您填写的联系方式交付，请确保联系方式准确无误。",
        "needs_email": False,
        "cat": "muse", "cat_label": "MUSE",
        "tint": "#E8F0FE",
        # 开站前私域历史销量，店主提供
        "sold_base": 5631,
        "initial_stock": 20,
        "icon": """<svg viewBox="0 0 100 100" width="54" height="54" fill="none"><path d="M24.6257 16.1214C28.2365 16.1214 30.8187 18.9408 30.8187 23.3643C30.8185 27.7868 30.1055 31.7765 28.9225 40.2466C28.0743 46.1813 26.62 55.2418 26.0132 59.0088C27.1782 56.7815 29.9074 51.5757 30.3914 50.5982C36.1081 39.061 42.0657 28.7544 43.7826 26.0254C46.0594 22.382 48.062 20.9229 51.1597 20.9229C52.7685 20.923 54.6826 21.7357 55.6315 22.819C56.9178 24.2895 57.1859 26.6602 57.1411 29.244C57.0738 33.2073 56.5599 39.5264 55.8553 46.5698C55.5416 49.7057 54.9365 56.1066 54.5288 60.4004C58.1883 53.8532 64.9609 41.8109 67.6921 37.6058C70.0727 33.9402 72.466 31.5797 75.6836 31.5796C78.4595 31.5796 81.8809 33.5416 81.6772 38.7573C81.3774 46.4556 80.2673 63.2232 79.7607 70.7479C83.1662 65.7913 87.6377 58.4543 89.3148 55.6966C91.0104 52.908 92.75 50.6542 95.3898 50.5778C98.0987 50.4995 99.913 52.341 99.9959 55.1839C100.078 58.0277 98.3835 61.2256 96.1344 64.856C93.6937 68.7957 90.9621 73.0123 87.6383 76.9491C84.3148 80.8856 81.2604 83.8782 76.5991 83.8786C72.4243 83.8786 69.4869 81.1043 69.283 76.0254C69.1768 73.364 69.6804 67.6405 70.0602 63.1673C70.5 57.9875 71.0315 52.9861 71.403 49.6786C67.7337 56.3979 60.0101 70.4676 56.5348 75.9603C53.1343 81.3339 51.4774 83.2269 47.8882 83.2275C44.2977 83.2275 42.7226 80.6416 42.6717 76.7497C42.6142 72.5285 45.7852 47.1821 46.8587 38.737C45.1183 42.4616 40.839 51.6056 38.1551 57.0435C35.5587 62.3055 31.204 71.3978 28.0436 76.6357C25.7668 80.4094 23.2092 83.2273 19.4173 83.2275C15.6252 83.2275 13.4847 80.6784 13.4847 76.5788C13.4847 72.4794 14.6716 65.6492 15.9465 57.1777C16.5839 53.0781 17.3108 48.6133 18.1315 43.8761C18.7324 40.448 19.7764 34.4169 20.4183 30.7129C17.502 35.2539 12.2536 43.4278 10.6567 45.8903C8.88113 48.6291 7.28747 50.626 4.64681 50.6266C1.7329 50.6266 0.000532901 48.3522 0 45.7113C0 43.0703 1.34323 41.0344 3.52376 37.4512C6.32403 32.8465 11.3578 26.57 14.1154 23.2747C17.3656 19.3912 20.6139 16.1219 24.6257 16.1214Z" fill="url(#mg)"/><defs><linearGradient id="mg" x1="133.245" y1="109.046" x2="24.9203" y2="-12.5565" gradientUnits="userSpaceOnUse"><stop offset="0.254808" stop-color="#0082FB"/><stop offset="0.697115" stop-color="#0064E0"/><stop offset="1" stop-color="#0040DC"/></linearGradient></defs></svg>""",
    },
    {
        "id": "chatgpt-go-3m",
        "name": "ChatGPT Go 三个月",
        "price_cents": 4499,
        "price_suffix": "一次付清",
        "price_note": "/ 个 · 一次付清",
        "desc": ("ChatGPT Go 成品号，时长 3 个月，Apple Pay 支付开通。"
                 "付款后由店主人工发货，通过您填写的联系方式交付账号。"),
        "points": [
            "成品号，ChatGPT Go 会员时长 3 个月",
            "交付格式：邮箱 | 密码 | 2FA 密钥",
            "质保 3 天",
            "2FA 验证码：打开 https://2fa.fun/ 输入 2FA 密钥，点击“获取验证码”，验证码每 30 秒自动更新一次",
            "付款后由店主人工发货，通过联系方式交付账号",
            "支持支付宝付款",
            "发货进度可在“我的订单”实时查看",
        ],
        "first_label": "接收账号的邮箱",
        "first_err": "接收账号的邮箱格式不正确",
        "password_hint": "付款后店主会通过您填写的联系方式交付账号，请确保联系方式准确无误。",
        "needs_email": False,
        "cat": "openai", "cat_label": "OPENAI",
        "tint": "#E6F4F1",
        # 新商品暂无私域历史销量，按 0 计
        "sold_base": 0,
        "icon": """<svg viewBox="0 0 100 100" width="54" height="54" fill="none" stroke="#111111" stroke-width="6" stroke-linecap="round"><ellipse cx="50" cy="50" rx="15" ry="28"/><ellipse cx="50" cy="50" rx="15" ry="28" transform="rotate(60 50 50)"/><ellipse cx="50" cy="50" rx="15" ry="28" transform="rotate(120 50 50)"/></svg>""",
    },
    {
        "id": "chatgpt-plus-1m-applepay",
        "name": "ChatGPT Plus 1月 Apple Pay",
        "price_cents": 4199,
        "price_suffix": "一次付清",
        "price_note": "/ 个 · 一次付清",
        "desc": ("ChatGPT Plus 成品号，时长 1 个月，Apple Pay 支付开通。"
                 "付款后由店主人工发货，通过您填写的联系方式交付账号。"),
        "points": [
            "成品号，ChatGPT Plus 会员时长 1 个月，Apple Pay 支付开通",
            "交付格式：邮箱 / 密码 / 2FA 密钥",
            "质保：仅保障 1 小时内首次登录（1H 质保首登），请收到后尽快登录验证",
            "付款后由店主人工发货，通过联系方式交付账号",
            "支持支付宝付款",
            "发货进度可在“我的订单”实时查看",
        ],
        "first_label": "接收账号的邮箱",
        "first_err": "接收账号的邮箱格式不正确",
        "password_hint": "付款后店主会通过您填写的联系方式交付账号，请确保联系方式准确无误。",
        "needs_email": False,
        "cat": "openai", "cat_label": "OPENAI",
        "tint": "#ECECEC",
        # 新商品暂无私域历史销量，按 0 计
        "sold_base": 0,
        "icon": """<svg viewBox="0 0 100 100" width="54" height="54"><rect x="6" y="6" width="88" height="88" rx="24" fill="#111111"/><g fill="none" stroke="#ffffff" stroke-width="5" stroke-linecap="round"><ellipse cx="50" cy="50" rx="11" ry="20"/><ellipse cx="50" cy="50" rx="11" ry="20" transform="rotate(60 50 50)"/><ellipse cx="50" cy="50" rx="11" ry="20" transform="rotate(120 50 50)"/></g></svg>""",
    },
    {
        "id": "grok-plus-1m",
        "name": "Grok Plus 1个月",
        "price_cents": 4994,
        "price_suffix": "一次付清",
        "price_note": "/ 个 · 一次付清",
        "desc": ("Grok Plus 成品号，时长 1 个月。付款后由店主人工发货，"
                 "通过您填写的联系方式交付账号。"),
        "points": [
            "成品号，Grok Plus 会员时长 1 个月",
            "共享 AI 使用额度池，含 Grok 聊天、语音、Imagine 和 Build",
            "含 Grok API 访问权限，官网 grok.com 登录使用",
            "交付格式：邮箱 + 密码，邮箱和密码均可修改",
            "请勿解除与 X 的关联，否则可能影响使用",
            "本商品无质保；登录检测服务不在保修范围内",
            "付款后由店主人工发货，通过联系方式交付账号",
            "支持支付宝付款",
            "发货进度可在“我的订单”实时查看",
        ],
        "first_label": "接收账号的邮箱",
        "first_err": "接收账号的邮箱格式不正确",
        "password_hint": "付款后店主会通过您填写的联系方式交付账号，请确保联系方式准确无误。",
        "needs_email": False,
        "cat": "grok", "cat_label": "GROK",
        "tint": "#EDEEF0",
        # 新商品暂无私域历史销量，按 0 计
        "sold_base": 0,
        "icon": """<svg viewBox="0 0 100 100" width="54" height="54"><circle cx="50" cy="50" r="44" fill="#111111"/><path d="M33 68 L62 32" stroke="#ffffff" stroke-width="7" stroke-linecap="round"/><path d="M40 32 L68 60" stroke="#ffffff" stroke-width="7" stroke-linecap="round" opacity="0.55"/></svg>""",
    },
    {
        "id": "grok-plus-7d",
        "name": "Grok Plus 7天",
        "price_cents": 4049,
        "price_suffix": "一次付清",
        "price_note": "/ 个 · 一次付清",
        "desc": ("Grok Plus 成品号，时长 7 天。付款后由店主人工发货，"
                 "通过您填写的联系方式交付账号。"),
        "points": [
            "成品号，Grok Plus 会员时长 7 天",
            "质保 1 天",
            "共享 AI 使用额度池，含 Grok 聊天、语音、Imagine 和 Build",
            "含 Grok API 访问权限，官网 grok.com 登录使用",
            "交付格式：邮箱 + 密码，邮箱和密码均可修改",
            "请勿解除与 X 的关联，否则可能影响使用",
            "登录检测服务不在保修范围内",
            "付款后由店主人工发货，通过联系方式交付账号",
            "支持支付宝付款",
            "发货进度可在“我的订单”实时查看",
        ],
        "first_label": "接收账号的邮箱",
        "first_err": "接收账号的邮箱格式不正确",
        "password_hint": "付款后店主会通过您填写的联系方式交付账号，请确保联系方式准确无误。",
        "needs_email": False,
        "cat": "grok", "cat_label": "GROK",
        "tint": "#EDEEF0",
        # 新商品暂无私域历史销量，按 0 计
        "sold_base": 0,
        "icon": """<svg viewBox="0 0 100 100" width="54" height="54"><circle cx="50" cy="50" r="44" fill="#111111"/><path d="M33 68 L62 32" stroke="#ffffff" stroke-width="7" stroke-linecap="round"/><path d="M40 32 L68 60" stroke="#ffffff" stroke-width="7" stroke-linecap="round" opacity="0.55"/></svg>""",
    },
    {
        "id": "gmail-old-account",
        "name": "老号 Gmail 谷歌邮箱（2010–2022）随机地区",
        "price_cents": 1754,
        "price_suffix": "一次付清",
        "price_note": "/ 个 · 一次付清",
        "desc": ("Gmail 老号邮箱，2010–2022 年注册，地区随机。付款后由店主 "
                 "人工发货，通过您填写的联系方式交付账号。"),
        "points": [
            "Gmail 谷歌邮箱老号，2010–2022 年注册，地区随机",
            "交付格式：邮箱账号 + 登录密码 + 辅助邮箱 + 2FA",
            "24H 质保首登：仅保障 24 小时内首次登录，请收到后尽快登录验证",
            "登录时可能需要手机验证，请自备接码方式",
            "建议使用稳定、可信的网络环境登录",
            "付款后由店主人工发货，通过联系方式交付账号",
            "支持支付宝付款",
            "发货进度可在“我的订单”实时查看",
        ],
        "first_label": "接收账号的邮箱",
        "first_err": "接收账号的邮箱格式不正确",
        "password_hint": "付款后店主会通过您填写的联系方式交付账号，请确保联系方式准确无误。",
        "needs_email": False,
        "cat": "gmail", "cat_label": "GOOGLE",
        "tint": "#FDECEA",
        # 新商品暂无私域历史销量，按 0 计
        "sold_base": 0,
        "icon": """<svg viewBox="0 0 100 100" width="54" height="54"><path d="M14 78 V30 L50 56 L86 30 V78 H66 V46 L50 58 L34 46 V78 Z" fill="#EA4335"/><path d="M14 30 L34 46 V78 H14 Z" fill="#FBBC04"/><path d="M86 30 L66 46 V78 H86 Z" fill="#34A853"/><path d="M14 24 L50 50 L86 24 L86 30 L50 56 L14 30 Z" fill="#4285F4"/></svg>""",
    },
]
PRODUCTS_BY_ID = {p["id"]: p for p in PRODUCTS}

# 商品卡质保徽章文案：与各商品 points 及 /guide 售后规则逐项对齐，
# 不夸大。None 表示灰色口径（如实标注无质保）。
WARRANTY_BADGES = {
    "gemini-pro-24m": "🛡 充不上全额退",
    "muse-account-1b": "🛡 保首登",
    "muse-2b": "🛡 保首登",
    "muse3-1b": "🛡 保首登",
    "chatgpt-go-3m": "🛡 质保 3 天",
    "chatgpt-plus-1m-applepay": "🛡 质保 1 小时 · 首登",
    "grok-plus-1m": None,          # 本商品无质保，卡上如实标注
    "grok-plus-7d": "🛡 质保 1 天",
    "gmail-old-account": "🛡 质保 24 小时 · 首登",
}

def warranty_html(pid):
    """商品卡质保徽章 HTML（按当前语言）；无该商品条目返回空串。"""
    lang = cur_lang()
    if lang == "zh":
        if pid not in WARRANTY_BADGES:
            return ""
        label = WARRANTY_BADGES[pid]
        if label is None:
            return ('<div><span class="wbadge off">无质保</span></div>')
        return f'<div><span class="wbadge">{esc(label)}</span></div>'
    table = i18n.WARRANTY_I18N.get(lang) or {}
    if pid not in table:
        table = i18n.WARRANTY_I18N.get("en") or {}
    if pid not in table:
        return ""
    label = table[pid]
    if label is None:
        off = (i18n.NO_WARRANTY_LABEL.get(lang)
               or i18n.NO_WARRANTY_LABEL.get("en", "No warranty"))
        return f'<div><span class="wbadge off">{esc(off)}</span></div>'
    return f'<div><span class="wbadge">{esc(label)}</span></div>'


# 首页顶部公告轮播文案（4 秒自动切换一条，可点 × 关闭、关后不再弹）
ANNOUNCEMENTS = [
    ("🎉 首充福利：首次储值满 ¥10 赠 ¥2、满 ¥15 赠 ¥5，"
     "去钱包看看 →", "/wallet"),
    ("🛡 售后保障：未交付可全额退款，各商品质保见卡片徽章"
     "与教程页 →", "/guide"),
    ("💬 人工交付：付款后店主人工处理，进度在「我的订单」"
     "实时可查，有问题点在线客服 →", "/support"),
]
DEFAULT_PRODUCT = PRODUCTS[0]
PRODUCT_NAME = DEFAULT_PRODUCT["name"]
PRODUCT_DESC = DEFAULT_PRODUCT["desc"]
AMOUNT_CENTS = DEFAULT_PRODUCT["price_cents"]

# ---------- 会员等级（2026-11-08 店主定版，照其提供的等级图） ----------
# 升级口径：累计消费（已付款订单实付金额）或累计充值（已到账储值
# 本金，不含赠送）任一达标即自动升级，只升不降。折扣在下单时按
# 当前等级作用到订单金额上（支付宝 / 余额支付同价）；储值本身
# 不打折。rate 为千分比：980 = 9.8 折。
LEVELS = [
    {"name": "普通会员", "rate": 1000, "label": "",
     "spend_cents": 0, "recharge_cents": 0},
    {"name": "白银会员", "rate": 980, "label": "9.8 折",
     "spend_cents": 50000, "recharge_cents": 80000},
    {"name": "黄金会员", "rate": 950, "label": "9.5 折",
     "spend_cents": 200000, "recharge_cents": 300000},
    {"name": "铂金会员", "rate": 920, "label": "9.2 折",
     "spend_cents": 500000, "recharge_cents": 800000},
    {"name": "黑金会员", "rate": 880, "label": "8.8 折",
     "spend_cents": 1200000, "recharge_cents": 2000000},
]


def level_for_totals(spend_cents, recharge_cents):
    """按累计消费 / 充值算应得等级序号（任一达标取最高）。"""
    lvl = 0
    for i, lv in enumerate(LEVELS):
        if (spend_cents >= lv["spend_cents"]
                or recharge_cents >= lv["recharge_cents"]):
            lvl = i
    return lvl


def user_totals(user_id, conn=None):
    """累计消费（paid/completed 订单实付）与累计充值（paid 储值本金）。"""
    own = conn is None
    if own:
        conn = db()
    spend = conn.execute(
        "SELECT COALESCE(SUM(amount_cents), 0) AS s FROM orders"
        " WHERE user_id=? AND status IN ('paid', 'completed')",
        (user_id,)).fetchone()["s"]
    recharge = conn.execute(
        "SELECT COALESCE(SUM(amount_cents), 0) AS s FROM recharges"
        " WHERE user_id=? AND status='paid'",
        (user_id,)).fetchone()["s"]
    if own:
        conn.close()
    return int(spend), int(recharge)


def refresh_user_level(user_id):
    """重算并保存用户等级：只升不降。返回当前等级序号。"""
    spend, recharge = user_totals(user_id)
    computed = level_for_totals(spend, recharge)
    conn = db()
    row = conn.execute("SELECT level FROM users WHERE id=?",
                       (user_id,)).fetchone()
    stored = 0
    if row is not None:
        try:
            stored = int(row["level"] or 0)
        except Exception:
            stored = 0
    new = max(stored, computed)
    if row is not None and new != stored:
        conn.execute("UPDATE users SET level=? WHERE id=?",
                     (new, user_id))
        conn.commit()
    conn.close()
    return new


def user_level(user):
    """从用户行取生效等级序号：店主手动设置（level_manual 非空）
    优先于自动等级（level）；老行无这些列时按普通会员。"""
    if not user:
        return 0
    try:
        manual = user["level_manual"]
    except Exception:
        manual = None
    if manual is not None:
        try:
            return min(max(int(manual), 0), len(LEVELS) - 1)
        except (TypeError, ValueError):
            pass
    try:
        lvl = int(user["level"] or 0)
    except Exception:
        return 0
    return min(max(lvl, 0), len(LEVELS) - 1)


def member_price_cents(price_cents, lvl):
    """按等级折扣算会员价（分，四舍五入到分）。"""
    rate = LEVELS[min(max(lvl, 0), len(LEVELS) - 1)]["rate"]
    return (int(price_cents) * rate + 500) // 1000


def get_product(pid):
    """下单链路查商品：走运行时目录（含后台改价/改名/新增），
    下架商品也返回（带 active 标记，由调用方拦截下单）；
    完全未知的 pid 回退默认商品（保持旧行为）。"""
    found = catalog_by_id(include_inactive=True).get(pid or "")
    return found if found is not None else DEFAULT_PRODUCT


# ---------- 商品目录（代码目录 + 后台管理覆盖层） ----------
# 代码里的 PRODUCTS 是出厂目录；店主在「商品管理」里的改名、改价、
# 改卖点、上下架、排序存入 products_admin 表作为覆盖行（is_custom=0），
# 后台新增的商品整行都是自定义商品（is_custom=1，图标/底色按分类
# 借用同类内置商品）。运行时一切商品读取都走 catalog_products()，
# 代码目录只作种子与回退。库存仍在 inventory 表，两边共用。

def _product_admin_rows():
    try:
        conn = db()
        rows = conn.execute("SELECT * FROM products_admin").fetchall()
        conn.close()
    except Exception:
        return {}
    return {r["pid"]: r for r in rows}


def _points_to_text(points):
    return "\n".join(points or [])


def _points_from_text(text):
    return [ln.strip() for ln in (text or "").splitlines() if ln.strip()]


def _cat_defaults(cat):
    """新商品按分类借用同类内置商品的图标、底色与分类标签。"""
    for p in PRODUCTS:
        if p["cat"] == cat:
            return p["icon"], p["tint"], p["cat_label"]
    return "✦", "#EEF0F4", (cat or "AI").upper()


def catalog_products(include_inactive=False):
    """运行时有效商品列表（已按排序排好）。"""
    rows = _product_admin_rows()
    items = []
    for idx, base in enumerate(PRODUCTS):
        p = dict(base)
        p["active"] = True
        p["_sort"] = (idx + 1) * 10
        r = rows.get(p["id"])
        if r is not None:
            p.update({
                "name": r["name"], "price_cents": r["price_cents"],
                "sold_base": r["sold_base"],
                "desc": r["desc"],
                "points": _points_from_text(r["points"]),
                "first_label": r["first_label"],
                "first_err": r["first_err"],
                "password_hint": r["password_hint"],
                "needs_email": bool(r["needs_email"]),
                "price_suffix": r["price_suffix"],
                "price_note": r["price_note"],
                "active": bool(r["active"]),
            })
            if r["sort"] is not None:
                p["_sort"] = r["sort"]
        items.append(p)
    for r in rows.values():
        if not r["is_custom"]:
            continue
        icon, tint, cat_label = _cat_defaults(r["cat"])
        items.append({
            "id": r["pid"], "name": r["name"],
            "price_cents": r["price_cents"],
            "price_suffix": r["price_suffix"] or "一次付清",
            "price_note": r["price_note"] or "/ 份 · 一次付清",
            "sold_base": r["sold_base"], "desc": r["desc"],
            "points": _points_from_text(r["points"]),
            "first_label": r["first_label"],
            "first_err": r["first_err"],
            "password_hint": r["password_hint"],
            "needs_email": bool(r["needs_email"]),
            "cat": r["cat"], "cat_label": r["cat_label"] or cat_label,
            "tint": r["tint"] or tint, "icon": icon,
            "active": bool(r["active"]),
            "_sort": r["sort"] if r["sort"] is not None else 10000,
            "is_custom": True,
        })
    items.sort(key=lambda p: p["_sort"])
    if not include_inactive:
        items = [p for p in items if p.get("active", True)]
    return items


def catalog_by_id(include_inactive=True):
    return {p["id"]: p
            for p in catalog_products(include_inactive=include_inactive)}


SELLER_QQ = "1006025461"

SITE_NAME = "曜石 AI · OBSIDIAN"
SITE_DESC = ("Gemini Pro 24 个月会员代充仅 ¥28.8（官方约 ¥145/月），"
             "另有 Muse 成品号 / 词元包、ChatGPT Go / Plus 成品号、"
             "Grok Plus、老号 Gmail。支付宝付款、人工交付、"
             "全程不索要账号密码，进度实时可查。")

# 站点图标：Gemini 官方四角星造型 + 官方渐变（供 /favicon.svg 与 og:image 用）
FAVICON_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 65 65">'
    '<defs><linearGradient id="g" x1="18.447" y1="43.42" x2="52.153"'
    ' y2="15.004" gradientUnits="userSpaceOnUse">'
    '<stop stop-color="#4893FC"/><stop offset=".27" stop-color="#4893FC"/>'
    '<stop offset=".777" stop-color="#969DFF"/>'
    '<stop offset="1" stop-color="#BD99FE"/></linearGradient></defs>'
    '<path d="M32.447 0c.68 0 1.273.465 1.439 1.125a38.904 38.904 0 001.999'
    ' 5.905c2.152 5 5.105 9.376 8.854 13.125 3.751 3.75 8.126 6.703 13.125'
    ' 8.855a38.98 38.98 0 005.906 1.999c.66.166 1.124.758 1.124 1.438 0'
    ' .68-.464 1.273-1.125 1.439a38.902 38.902 0 00-5.905 1.999c-5 2.152'
    '-9.375 5.105-13.125 8.854-3.749 3.751-6.702 8.126-8.854 13.125a38.973'
    ' 38.973 0 00-2 5.906 1.485 1.485 0 01-1.438 1.124c-.68 0-1.272-.464'
    '-1.438-1.125a38.913 38.913 0 00-2-5.905c-2.151-5-5.103-9.375-8.854'
    '-13.125-3.75-3.749-8.125-6.702-13.125-8.854a38.973 38.973 0 00-5.905-2'
    'A1.485 1.485 0 010 32.448c0-.68.465-1.272 1.125-1.438a38.903 38.903 0'
    ' 005.905-2c5-2.151 9.376-5.104 13.125-8.854 3.75-3.749 6.703-8.125'
    ' 8.855-13.125a38.972 38.972 0 001.999-5.905A1.485 1.485 0 0132.447 0z"'
    ' fill="url(#g)"/></svg>')


def order_product(row):
    """按订单记录找到对应商品（先按 product_id，老订单按名称匹配）。
    走运行时目录（含下架与后台新增商品），保证老订单仍能解析。"""
    try:
        pid = row["product_id"]
    except Exception:
        pid = ""
    catalog = catalog_products(include_inactive=True)
    if pid:
        for p in catalog:
            if p["id"] == pid:
                return p
    for p in catalog:
        if p["name"] == row["product_name"]:
            return p
    return None


BALANCE_KIND_LABELS = {
    "recharge": "在线储值",
    "bonus": "首充赠送",
    "pay": "余额支付",
    "refund": "退款返还",
    "admin": "店主调账",
}

# 首充活动：用户首次成功储值时按实付金额赠送固定金额（分）。
# 满 ¥10 赠 ¥2（到账 ¥12），满 ¥15 赠 ¥5（到账 ¥20），每人仅一次；
# 按从高到低匹配，只取最高一档。已成功储值过的用户不再参加。
FIRST_RECHARGE_BONUS_TIERS = ((1500, 500), (1000, 200))


def first_recharge_bonus_cents(conn, user_id, amount_cents):
    """返回这笔储值应得的首充赠送（分）：该用户此前没有任何
    已到账储值记录、且本笔实付达到门槛时，按最高档赠送，否则 0。
    必须在本笔储值标记 paid 之前调用。"""
    row = conn.execute(
        "SELECT COUNT(*) AS c FROM recharges"
        " WHERE user_id=? AND status='paid'", (user_id,)).fetchone()
    if row["c"] > 0:
        return 0
    for threshold, bonus in FIRST_RECHARGE_BONUS_TIERS:
        if amount_cents >= threshold:
            return bonus
    return 0


def has_paid_recharge(conn, user_id):
    row = conn.execute(
        "SELECT COUNT(*) AS c FROM recharges"
        " WHERE user_id=? AND status='paid'", (user_id,)).fetchone()
    return row["c"] > 0


def support_unread_count():
    conn = db()
    n = conn.execute(
        "SELECT COUNT(*) AS c FROM support_messages"
        " WHERE sender='user' AND is_read=0").fetchone()["c"]
    conn.close()
    return n


def admin_tabs(active):
    badge = ""
    if active != "support":
        n = support_unread_count()
        if n:
            badge = f'<span class="sup-badge">{n}</span>'
    def cls(name):
        return ' class="on"' if name == active else ""
    return (f'<p class="tabs"><a{cls("orders")} href="/admin">订单处理</a>'
            f'<a{cls("products")} href="/admin/products">商品管理</a>'
            f'<a{cls("wallet")} href="/admin/wallet">储值管理</a>'
            f'<a{cls("support")} href="/admin/support">客服消息{badge}</a></p>')


def chat_bubbles(messages, viewer):
    """渲染聊天气泡，返回 (html, 最后一条消息 id)。
    viewer='user'：客户消息靠右；viewer='admin'：店主消息靠右。"""
    out = ""
    last_id = 0
    for m in messages:
        if viewer == "user":
            mine = m["sender"] == "user"
            who = T("chat.me") if mine else T("chat.seller")
        else:
            mine = m["sender"] == "admin"
            who = T("chat.me") if mine else T("chat.customer")
        out += ('<div class="msg ' + ("me" if mine else "them") + '">'
                '<span class="who">' + who + '</span>'
                + esc(m["body"])
                + '<span class="tm">' + esc(m["created_at"])
                + '</span></div>')
        last_id = m["id"]
    if not out:
        out = ('<p class="hint" id="chatEmpty">' + T("chat.empty")
               + '</p>')
    return out, last_id


CHAT_POLL_JS = """
<script>
(function(){
  var box = document.getElementById('chatBox');
  if(!box) return;
  var last = parseInt(box.getAttribute('data-last') || '0', 10);
  var url = box.getAttribute('data-poll');
  function escHtml(s){var d = document.createElement('div');
    d.textContent = s; return d.innerHTML;}
  function scrollEnd(){ box.scrollTop = box.scrollHeight; }
  scrollEnd();
  setInterval(function(){
    var sep = url.indexOf('?') >= 0 ? '&' : '?';
    fetch(url + sep + 'after=' + last, {credentials:'same-origin'})
      .then(function(r){ return r.json(); })
      .then(function(data){
        var msgs = data.messages || [];
        msgs.forEach(function(m){
          var empty = document.getElementById('chatEmpty');
          if(empty) empty.remove();
          var div = document.createElement('div');
          div.className = 'msg ' + (m.mine ? 'me' : 'them');
          div.innerHTML = '<span class="who">' + escHtml(m.who) +
            '</span>' + escHtml(m.body) +
            '<span class="tm">' + escHtml(m.created_at) + '</span>';
          box.appendChild(div);
          if(m.id > last) last = m.id;
        });
        if(msgs.length) scrollEnd();
      }).catch(function(){});
  }, 8000);
})();
</script>
"""


def qq_box():
    return f"""
        <div class="qqbox" data-copywrap>
          💬 <b>{T('qq.title')}</b>：{T('qq.pre')}
          <b class="qqnum copytext">{SELLER_QQ}</b><button class="copybtn"
            type="button">{T('qq.copy')}</button><br>
          <span class="hint">{T('qq.note')}</span>
        </div>"""


def copy_script():
    return """
<script>
document.querySelectorAll('.copybtn').forEach(function(b){
  b.addEventListener('click', function(){
    var wrap = b.closest('[data-copywrap]');
    var t = wrap ? wrap.querySelector('.copytext') : null;
    if(!t) return;
    var old = b.textContent;
    var done = function(){ b.textContent = '已复制 ✓';
      setTimeout(function(){ b.textContent = old; }, 1600); };
    if(navigator.clipboard && navigator.clipboard.writeText){
      navigator.clipboard.writeText(t.innerText.trim()).then(done, done);
    } else {
      var r = document.createRange(); r.selectNodeContents(t);
      var s = getSelection(); s.removeAllRanges(); s.addRange(r);
      try{ document.execCommand('copy'); }catch(e){}
      s.removeAllRanges(); done();
    }
  });
});
</script>"""

STATUS_LABELS = {
    "unpaid": "待支付",
    "paid": "已支付 / 待充值",
    "completed": "已完成（已到账）",
    "failed": "已失败",
    "refunded": "已退款",
    "cancelled": "已取消",
}
# 「删除全部订单」的确认短语：店主必须在确认页逐字输入这六个字，
# 前端按钮才点亮、后端才放行（双保险，防手滑与误触）。
DELETE_ALL_PHRASE = "删除全部订单"
EMAIL_RE = re.compile(r"^[^@\s]{1,64}@[^@\s]+\.[^@\s]+$")

PBKDF2_ROUNDS = 200_000
SESSION_TTL = 7 * 24 * 3600

# ------------------------------------------------------------------ 失败限流
# 登录 / 免登录查单的失败计数（纯内存实现，进程重启清零，可接受）。
# 结构：key -> [连续失败次数, 锁定截止时间戳（0=未锁定）]。常量可按需调整。
LOGIN_MAX_FAILS = 5         # /login、/admin/login：同 IP+账号连续失败上限
LOGIN_LOCK_SECONDS = 600    # 登录锁定 10 分钟
TRACK_MAX_FAILS = 10        # /track：同 IP 查询失败上限
TRACK_LOCK_SECONDS = 600    # 查单锁定 10 分钟
_rate_lock = threading.Lock()
_login_fails = {}
_track_fails = {}


def _rate_locked_seconds(store, key):
    """key 处于锁定时返回剩余秒数，否则返回 0。"""
    now = time.time()
    with _rate_lock:
        ent = store.get(key)
        if ent and ent[1] > now:
            return int(ent[1] - now) + 1
        return 0


def _rate_record_fail(store, key, max_fails, lock_seconds):
    """记一次失败，达到上限即进入锁定；返回 True 表示已锁定。"""
    now = time.time()
    with _rate_lock:
        ent = store.get(key)
        if ent and ent[1] > now:
            return True
        if ent and ent[1]:
            ent = None  # 上一轮锁定已过期，计数重新开始
        count = (ent[0] if ent else 0) + 1
        locked = count >= max_fails
        store[key] = [count, now + lock_seconds if locked else 0]
        return locked


def _rate_clear(store, key):
    with _rate_lock:
        store.pop(key, None)


def _lock_message(seconds):
    minutes = max(1, -(-seconds // 60))
    return T("lock.msg", m=minutes)


# 订单状态大圈与提示文案：登录态订单详情页与免登录查单结果页共用
ORDER_HEROES = {
    "completed": ("", "✓", "订单已完成"),
    "paid": (" wait", "◷", "已支付，店主处理中"),
    "unpaid": (" grey", "!", "订单待支付"),
    "failed": (" bad", "✕", "订单已失败"),
    "refunded": (" grey", "↩", "订单已退款"),
    "cancelled": (" grey", "✕", "订单已取消"),
}

ORDER_TIPS = {
    "completed": "店主已处理完成，交付内容在下方（如有）。",
    "paid": "付款已确认，店主会按顺序处理，完成后交付内容会出现在本页。",
    "unpaid": "完成支付后，店主才会开始处理这一单。",
    "failed": "这一单处理失败，售后请联系店主 QQ 并提供订单号。",
    "refunded": "这一单已退款，如有疑问请联系店主。",
    "cancelled": "这一单已取消，不会被处理；如需购买请重新下单。",
}


def order_usage_html(product):
    """订单「使用说明」列表 HTML（详情页 / 查单结果页共用）。"""
    if cur_lang() != "zh" and product:
        if product["id"] == "gemini-pro-24m":
            kind = "usage_gemini"
        elif product["id"] == "gmail-old-account":
            kind = "usage_gmail"
        else:
            kind = f"usage_{product['cat']}"
        blob = i18n.blob(cur_lang(), kind)
        if blob:
            return blob
    if product and product["cat"] == "muse":
        return f"""<ol>
          <li>打开 muse.ai，使用交付内容中的<b>邮箱和密码</b>登录。</li>
          <li>交付格式一般为「邮箱 - 密码 - 接码链接」，
          登录需要验证码时，打开接码链接获取。</li>
          <li>若提示“你已加入等候名单”，多为地区限制，
          可切换<b>美国或加拿大</b>网络节点后重新登录。</li>
          <li>部分账号可能需要人脸照片验证，能否通过由 Muse 官方判定。</li>
          <li>账号异常或不会用，联系店主 QQ {SELLER_QQ}（备注订单号）。</li>
        </ol>"""
    elif product and product["id"] == "gemini-pro-24m":
        return f"""<ol>
          <li>确认下单时填的 Google 邮箱、辅助邮箱无误。</li>
          <li>添加店主 QQ {SELLER_QQ} 并备注订单号，配合店主完成代充。</li>
          <li>完成后在 Google 账号的订阅页面确认 Gemini Pro 已生效
          （时长 24 个月）。</li>
          <li>全程不需要提供 Google 账号密码，任何人索要都不要给。</li>
        </ol>"""
    elif product and product["cat"] == "grok":
        return f"""<ol>
          <li>打开 grok.com，使用交付内容中的<b>邮箱和密码</b>登录。</li>
          <li>邮箱和密码均可修改；<b>请勿解除与 X 的关联</b>，
          否则可能影响使用。</li>
          <li>Grok Plus 7天款质保 1 天，1 个月款无质保；
          登录检测服务不在保修范围内。</li>
          <li>账号异常或不会用，联系店主 QQ {SELLER_QQ}（备注订单号）。</li>
        </ol>"""
    elif product and product["id"] == "gmail-old-account":
        return f"""<ol>
          <li>使用交付内容中的<b>邮箱账号和登录密码</b>登录 Gmail，
          需要验证时用交付的辅助邮箱与 2FA。</li>
          <li>本商品 <b>24 小时内首次登录</b>才在质保内，
          收到后请尽快登录验证。</li>
          <li>登录时可能需要手机验证，请自备接码方式；
          建议使用稳定、可信的网络环境登录。</li>
          <li>账号异常或不会用，联系店主 QQ {SELLER_QQ}（备注订单号）。</li>
        </ol>"""
    elif product and product["cat"] == "openai":
        return f"""<ol>
          <li>打开 chatgpt.com，使用交付内容中的<b>邮箱和密码</b>登录。</li>
          <li>登录需要验证码时，打开 https://2fa.fun/ ，
          输入交付内容中的 <b>2FA 密钥</b>，点击“获取验证码”，
          验证码每 30 秒自动更新一次。</li>
          <li>ChatGPT Plus 1月款仅保障 <b>1 小时内首次登录</b>，
          收到后请尽快登录验证；ChatGPT Go 三个月款质保 3 天。</li>
          <li>账号异常或不会用，联系店主 QQ {SELLER_QQ}（备注订单号）。</li>
        </ol>"""
    return f"""<ul>
          <li>按上方交付内容使用即可。</li>
          <li>有任何问题，联系店主 QQ {SELLER_QQ} 并提供订单号。</li>
        </ul>"""


# ------------------------------------------------------------------ 数据库

def db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = db()
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        salt BLOB NOT NULL,
        pass_hash BLOB NOT NULL,
        is_admin INTEGER NOT NULL DEFAULT 0,
        balance_cents INTEGER NOT NULL DEFAULT 0,
        created_at TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS sessions (
        token TEXT PRIMARY KEY,
        user_id INTEGER NOT NULL,
        csrf TEXT NOT NULL,
        created_at INTEGER NOT NULL
    );
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_no TEXT UNIQUE NOT NULL,
        user_id INTEGER NOT NULL,
        product_name TEXT NOT NULL,
        amount_cents INTEGER NOT NULL,
        google_email TEXT NOT NULL,
        aux_email TEXT NOT NULL,
        contact TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'unpaid',
        pay_method TEXT DEFAULT '',
        trade_no TEXT DEFAULT '',
        admin_note TEXT DEFAULT '',
        product_id TEXT DEFAULT '',
        delivery TEXT DEFAULT '',
        created_at TEXT NOT NULL,
        updated_at TEXT NOT NULL,
        paid_at TEXT DEFAULT '',
        completed_at TEXT DEFAULT ''
    );
    CREATE TABLE IF NOT EXISTS recharges (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        recharge_no TEXT UNIQUE NOT NULL,
        user_id INTEGER NOT NULL,
        amount_cents INTEGER NOT NULL,
        status TEXT NOT NULL DEFAULT 'unpaid',
        pay_method TEXT DEFAULT '',
        trade_no TEXT DEFAULT '',
        bonus_cents INTEGER NOT NULL DEFAULT 0,
        created_at TEXT NOT NULL,
        paid_at TEXT DEFAULT ''
    );
    CREATE TABLE IF NOT EXISTS balance_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        change_cents INTEGER NOT NULL,
        balance_after INTEGER NOT NULL,
        kind TEXT NOT NULL,
        ref_no TEXT DEFAULT '',
        note TEXT DEFAULT '',
        created_at TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS support_messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        sender TEXT NOT NULL,
        body TEXT NOT NULL,
        is_read INTEGER NOT NULL DEFAULT 0,
        created_at TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS inventory (
        product_id TEXT PRIMARY KEY,
        stock INTEGER NOT NULL DEFAULT -1
    );
    CREATE TABLE IF NOT EXISTS products_admin (
        pid TEXT PRIMARY KEY,
        name TEXT NOT NULL DEFAULT '',
        price_cents INTEGER NOT NULL DEFAULT 0,
        sold_base INTEGER NOT NULL DEFAULT 0,
        sort INTEGER,
        active INTEGER NOT NULL DEFAULT 1,
        is_custom INTEGER NOT NULL DEFAULT 0,
        cat TEXT NOT NULL DEFAULT '',
        cat_label TEXT NOT NULL DEFAULT '',
        tint TEXT NOT NULL DEFAULT '',
        desc TEXT NOT NULL DEFAULT '',
        points TEXT NOT NULL DEFAULT '',
        first_label TEXT NOT NULL DEFAULT '',
        first_err TEXT NOT NULL DEFAULT '',
        password_hint TEXT NOT NULL DEFAULT '',
        needs_email INTEGER NOT NULL DEFAULT 0,
        price_suffix TEXT NOT NULL DEFAULT '',
        price_note TEXT NOT NULL DEFAULT '',
        created_at TEXT NOT NULL DEFAULT ''
    );
    """)
    conn.commit()
    # 老库迁移：补上后来新增的列
    cols = [r[1] for r in conn.execute("PRAGMA table_info(orders)")]
    for col in ("product_id", "delivery"):
        if col not in cols:
            conn.execute(
                f"ALTER TABLE orders ADD COLUMN {col} TEXT DEFAULT ''")
    if "cost_cents" not in cols:
        # 本单成本（分），店主在后台逐单填写，NULL = 未填
        conn.execute("ALTER TABLE orders ADD COLUMN cost_cents"
                     " INTEGER")
        conn.commit()
    ucols = [r[1] for r in conn.execute("PRAGMA table_info(users)")]
    if "balance_cents" not in ucols:
        conn.execute("ALTER TABLE users ADD COLUMN balance_cents"
                     " INTEGER NOT NULL DEFAULT 0")
    if "level" not in ucols:
        conn.execute("ALTER TABLE users ADD COLUMN level"
                     " INTEGER NOT NULL DEFAULT 0")
        conn.commit()
        # 首次加列：按历史订单 / 储值给老用户回填一次等级
        for u in conn.execute("SELECT id FROM users").fetchall():
            spend, recharge = user_totals(u["id"], conn)
            conn.execute(
                "UPDATE users SET level=? WHERE id=?",
                (level_for_totals(spend, recharge), u["id"]))
        conn.commit()
    if "level_manual" not in ucols:
        # 店主在储值管理里手动指定的等级（NULL = 按自动等级生效）
        conn.execute("ALTER TABLE users ADD COLUMN level_manual"
                     " INTEGER")
        conn.commit()
    rcols = [r[1] for r in conn.execute("PRAGMA table_info(recharges)")]
    if rcols and "bonus_cents" not in rcols:
        conn.execute("ALTER TABLE recharges ADD COLUMN bonus_cents"
                     " INTEGER NOT NULL DEFAULT 0")
    conn.commit()
    # 库存种子：首次出现该商品时按配置写入初始库存
    # （商品无 initial_stock 配置 = -1 不限量；已存在的行不覆盖，
    # 卖家在后台改过的库存不会被重启冲掉）
    for p in PRODUCTS:
        conn.execute(
            "INSERT OR IGNORE INTO inventory (product_id, stock)"
            " VALUES (?, ?)",
            (p["id"], p.get("initial_stock", -1)))
    conn.commit()
    # 首次启动：按环境变量创建管理员
    admin_email = os.environ.get("GEMINI_ADMIN_EMAIL", "").strip()
    admin_pw = os.environ.get("GEMINI_ADMIN_PASSWORD", "")
    if admin_email and admin_pw:
        row = conn.execute("SELECT id FROM users WHERE email=?",
                           (admin_email,)).fetchone()
        if row is None:
            salt, pw_hash = hash_password(admin_pw)
            conn.execute(
                "INSERT INTO users (email, salt, pass_hash, is_admin,"
                " created_at) VALUES (?,?,?,1,?)",
                (admin_email, salt, pw_hash, now_text()))
            conn.commit()
            print(f"[init] 已创建管理员账号：{admin_email}")
    conn.close()


def now_text():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def hash_password(password):
    salt = os.urandom(16)
    pw_hash = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, PBKDF2_ROUNDS)
    return salt, pw_hash


def check_password(user_row, password):
    pw_hash = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), user_row["salt"],
        PBKDF2_ROUNDS)
    return secrets.compare_digest(pw_hash, user_row["pass_hash"])


def valid_email(value):
    return bool(value) and len(value) <= 254 and bool(
        EMAIL_RE.match(value.strip()))


def make_order_no(conn):
    while True:
        no = "GM" + datetime.now().strftime("%Y%m%d%H%M%S") + \
            f"{secrets.randbelow(10000):04d}"
        row = conn.execute("SELECT id FROM orders WHERE order_no=?",
                           (no,)).fetchone()
        if row is None:
            return no


def make_recharge_no(conn):
    while True:
        no = "RC" + datetime.now().strftime("%Y%m%d%H%M%S") + \
            f"{secrets.randbelow(10000):04d}"
        row = conn.execute("SELECT id FROM recharges WHERE recharge_no=?",
                           (no,)).fetchone()
        if row is None:
            return no


def apply_balance_change(conn, user_id, delta_cents, kind, ref_no="",
                         note=""):
    """在调用方的事务里增减余额并记流水，返回变动后的余额。
    余额不足时抛 ValueError，调用方不要提交事务。"""
    row = conn.execute("SELECT balance_cents FROM users WHERE id=?",
                       (user_id,)).fetchone()
    if row is None:
        raise ValueError("用户不存在")
    new_balance = row["balance_cents"] + delta_cents
    if new_balance < 0:
        raise ValueError("余额不足")
    conn.execute("UPDATE users SET balance_cents=? WHERE id=?",
                 (new_balance, user_id))
    conn.execute(
        "INSERT INTO balance_logs (user_id, change_cents, balance_after,"
        " kind, ref_no, note, created_at) VALUES (?,?,?,?,?,?,?)",
        (user_id, delta_cents, new_balance, kind, ref_no, note, now_text()))
    return new_balance


def mark_recharge_paid(recharge_no, trade_no):
    """储值单标记已支付并给用户加余额（幂等：重复通知不重复加款）。"""
    conn = db()
    row = conn.execute("SELECT * FROM recharges WHERE recharge_no=?",
                       (recharge_no,)).fetchone()
    if row is None:
        conn.close()
        return False
    if row["status"] == "unpaid":
        ts = now_text()
        # 首充赠送必须在本笔标记 paid 之前判定（判定依据是此前
        # 有没有已到账记录），赠送与本金在同一事务里到账。
        bonus = first_recharge_bonus_cents(
            conn, row["user_id"], row["amount_cents"])
        try:
            conn.execute(
                "UPDATE recharges SET status='paid', trade_no=?,"
                " paid_at=?, bonus_cents=? WHERE recharge_no=?",
                (trade_no or "", ts, bonus, recharge_no))
        except Exception:
            # 老库还没跑过 init 迁移出 bonus_cents 列时退回旧写法
            conn.execute(
                "UPDATE recharges SET status='paid', trade_no=?, paid_at=?"
                " WHERE recharge_no=?", (trade_no or "", ts, recharge_no))
        apply_balance_change(conn, row["user_id"], row["amount_cents"],
                             "recharge", recharge_no, "在线储值")
        if bonus > 0:
            apply_balance_change(
                conn, row["user_id"], bonus, "bonus", recharge_no,
                "首充活动赠送（实付 ¥%.2f，到账 ¥%.2f）"
                % (row["amount_cents"] / 100,
                   (row["amount_cents"] + bonus) / 100))
        conn.commit()
    conn.close()
    try:
        refresh_user_level(row["user_id"])
    except Exception:
        pass  # 等级刷新失败不能影响储值主流程
    return True


def get_recharge(recharge_no):
    conn = db()
    row = conn.execute("SELECT * FROM recharges WHERE recharge_no=?",
                       (recharge_no,)).fetchone()
    conn.close()
    return row


def _deduct_stock(conn, product_id):
    """在调用方事务里扣 1 件库存：仅对已启用库存跟踪的商品
    （stock >= 0），且扣后不为负；不限量商品（-1）不动。"""
    if not product_id:
        return
    conn.execute(
        "UPDATE inventory SET stock=stock-1"
        " WHERE product_id=? AND stock>0", (product_id,))


def _restock(conn, product_id):
    """在调用方事务里回补 1 件库存（退款 / 失败时用）：
    仅对已启用库存跟踪的商品生效，不限量商品不动。"""
    if not product_id:
        return
    conn.execute(
        "UPDATE inventory SET stock=stock+1"
        " WHERE product_id=? AND stock>=0", (product_id,))


def get_stock(product_id):
    """查商品当前库存：-1 = 不限量；0 = 售罄；>0 = 剩余件数。"""
    conn = db()
    row = conn.execute("SELECT stock FROM inventory WHERE product_id=?",
                       (product_id,)).fetchone()
    conn.close()
    return row["stock"] if row else -1


def get_all_stock():
    """全部商品的库存字典 {product_id: stock}，无记录的商品视为不限量。"""
    conn = db()
    rows = conn.execute("SELECT product_id, stock FROM inventory").fetchall()
    conn.close()
    return {r["product_id"]: r["stock"] for r in rows}


def set_stock(product_id, stock):
    conn = db()
    conn.execute(
        "INSERT INTO inventory (product_id, stock) VALUES (?, ?)"
        " ON CONFLICT(product_id) DO UPDATE SET stock=excluded.stock",
        (product_id, int(stock)))
    conn.commit()
    conn.close()


def snapshot_db_before_delete_all():
    """「删除全部订单」执行前的强制备份：用 sqlite3 backup API 把
    当前数据库快照到数据库同目录的 backups/ 子目录，文件名
    pre-delete-all-YYYYMMDD-HHMM.db（实现同 backup_db.py：源库只读
    打开；同分钟重跑自动加 -2、-3 后缀）。成功返回备份文件名
    （不含目录）；失败抛异常，由调用方中止删除、订单一张不动。
    注意：这类备份不在 backup_db.py 的每日自动清理范围（它只清理
    store- 前缀），会一直保留，需人工清理。"""
    dest_dir = os.path.join(os.path.dirname(os.path.abspath(DB_PATH)),
                            "backups")
    os.makedirs(dest_dir, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M")
    dest = os.path.join(dest_dir, f"pre-delete-all-{stamp}.db")
    n = 2
    while os.path.exists(dest):
        dest = os.path.join(dest_dir, f"pre-delete-all-{stamp}-{n}.db")
        n += 1
    src = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    try:
        dst = sqlite3.connect(dest)
        try:
            src.backup(dst)
        finally:
            dst.close()
    finally:
        src.close()
    return os.path.basename(dest)


def profit_stats():
    """利润汇总（仅统计已付款订单 paid/completed）：
    orders/revenue = 已付款单数与总营业额；filled = 其中已填成本
    的单数；rev_filled/cost/profit = 已填成本单的营业额/成本/
    利润（利润 = 逐单 amount - cost）；missing = 未填成本单数。
    退款 / 失败 / 待支付订单不计入。"""
    conn = db()
    row = conn.execute(
        "SELECT COUNT(*) AS n,"
        " COALESCE(SUM(amount_cents), 0) AS rev,"
        " COALESCE(SUM(cost_cents), 0) AS cost,"
        " COALESCE(SUM(CASE WHEN cost_cents IS NOT NULL"
        " THEN 1 ELSE 0 END), 0) AS filled,"
        " COALESCE(SUM(CASE WHEN cost_cents IS NOT NULL"
        " THEN amount_cents ELSE 0 END), 0) AS rev_filled"
        " FROM orders WHERE status IN ('paid', 'completed')"
    ).fetchone()
    conn.close()
    n = int(row["n"])
    filled = int(row["filled"])
    rev_filled = int(row["rev_filled"])
    cost = int(row["cost"])
    return {"orders": n, "revenue": int(row["rev"]),
            "filled": filled, "missing": n - filled,
            "rev_filled": rev_filled, "cost": cost,
            "profit": rev_filled - cost}


def store_stats():
    """首页 / 下单页信任徽章数据：
    sold = 本站已付款订单数（paid + completed，订单表实时统计）；
    per_product = 每个商品的展示已售 = 配置 sold_base（开站前私域
    历史销量，店主提供）+ 本站该商品真实已付款单数；老订单无
    product_id / 对不上商品时归到默认商品，与 product_of 口径一致；
    display_sold = 各商品展示已售之和，与单品数字自洽；
    avg_minutes = 本站 completed 订单从付款到完成的平均分钟数，
    样本少于 3 单时为 None（页面不展示，避免数字不可信）。"""
    conn = db()
    sold = conn.execute(
        "SELECT COUNT(*) AS c FROM orders"
        " WHERE status IN ('paid', 'completed')").fetchone()["c"]
    cat_ids = set(catalog_by_id(include_inactive=True))
    real_by_pid = {}
    for r in conn.execute(
            "SELECT product_id, COUNT(*) AS c FROM orders"
            " WHERE status IN ('paid', 'completed')"
            " GROUP BY product_id"):
        pid = (r["product_id"] if r["product_id"] in cat_ids
               else DEFAULT_PRODUCT["id"])
        real_by_pid[pid] = real_by_pid.get(pid, 0) + r["c"]
    rows = conn.execute(
        "SELECT paid_at, completed_at FROM orders"
        " WHERE status='completed' AND paid_at<>'' AND completed_at<>''"
    ).fetchall()
    conn.close()
    minutes = []
    fmt = "%Y-%m-%d %H:%M:%S"
    for r in rows:
        try:
            delta = (datetime.strptime(r["completed_at"], fmt)
                     - datetime.strptime(r["paid_at"], fmt))
        except (ValueError, TypeError):
            continue
        secs = delta.total_seconds()
        if secs >= 0:
            minutes.append(secs / 60.0)
    avg = (sum(minutes) / len(minutes)) if len(minutes) >= 3 else None
    per_product = {}
    for p in catalog_products(include_inactive=True):
        base = p.get("sold_base", 0) or 0  # 老配置无此字段时按 0
        per_product[p["id"]] = int(base) + real_by_pid.get(p["id"], 0)
    return {"sold": sold,
            "display_sold": sum(per_product.values()),
            "per_product": per_product,
            "avg_minutes": avg}


def trust_line(stats=None):
    """把 store_stats 渲染成一行信任文案（无数据时只保留固定承诺）。"""
    stats = stats if stats is not None else store_stats()
    parts = []
    display_sold = stats.get("display_sold", stats["sold"])
    if display_sold > 0:
        parts.append(T("trust.sold", n=display_sold))
    if stats["avg_minutes"] is not None:
        avg = stats["avg_minutes"]
        if avg < 60:
            parts.append(T("trust.avg_min", n=max(1, round(avg))))
        else:
            parts.append(T("trust.avg_hour", n=f"{avg / 60:.1f}"))
    parts.append(T("trust.nopass"))
    return "🛡 " + " · ".join(parts)


def mark_order_paid(order_no, pay_method, trade_no, notify_seller=True):
    """把待支付订单标记为已支付（幂等：已非待支付状态不重复改）。
    订单不存在返回 False，否则 True。回调与查单轮询共用同一逻辑。
    首次转入已支付时：同事务扣 1 件库存，并给店主发推送通知。
    店主后台手动确认收款（平台账单漏单兜底）也走这里，传
    notify_seller=False：店主自己点的，不必再给自己发一遍推送。"""
    conn = db()
    row = conn.execute("SELECT * FROM orders WHERE order_no=?",
                       (order_no,)).fetchone()
    if row is None:
        conn.close()
        return False
    if row["status"] in ("unpaid", "cancelled"):
        ts = now_text()
        conn.execute(
            "UPDATE orders SET status='paid', pay_method=?,"
            " trade_no=?, paid_at=?, updated_at=? WHERE order_no=?",
            (pay_method, trade_no or "", ts, ts, order_no))
        try:
            pid = row["product_id"]
        except Exception:
            pid = ""
        _deduct_stock(conn, pid or "")
        conn.commit()
        conn.close()
        try:
            refresh_user_level(row["user_id"])
        except Exception:
            pass  # 等级刷新失败不能影响支付主流程
        if notify_seller:
            notify.push_async(
                "💰 新订单已支付",
                f"{row['product_name']}\n订单号：{order_no}\n"
                f"金额：¥{row['amount_cents'] / 100:.2f}\n"
                "请尽快在卖家后台处理。")
        return True
    conn.close()
    return True


# ------------------------------------------------------ 易支付查单兜底
# 网关异步通知可能因网络问题（实测网关服务器回调我方站点超时）
# 送达失败，故不能只依赖推送：后台线程定期向网关 api.php 主动
# 查单确认。只处理待支付、走易支付、24 小时内创建的订单；查单
# 返回已支付且金额数值一致时才改单。任何异常一律静默跳过，
# 绝不让轮询线程崩溃或影响主服务。
EPAY_POLL_ENABLED = True
EPAY_POLL_INTERVAL_SECONDS = 60


def epay_poll_once():
    """跑一轮易支付主动查单（供后台线程与测试调用）。"""
    try:
        conn = db()
        rows = conn.execute(
            "SELECT * FROM orders WHERE status='unpaid'"
            " AND pay_method LIKE 'epay%'"
            " AND created_at >= datetime('now','localtime','-24 hours')"
            " ORDER BY id ASC").fetchall()
        rc_rows = conn.execute(
            "SELECT * FROM recharges WHERE status='unpaid'"
            " AND pay_method LIKE 'epay%'"
            " AND created_at >= datetime('now','localtime','-24 hours')"
            " ORDER BY id ASC").fetchall()
        conn.close()
    except Exception:
        return
    for row in rows:
        try:
            result = payments.epay_query_order(row["order_no"])
        except payments.PaymentNotConfigured:
            return  # 易支付未配置：整轮静默跳过
        except Exception:
            continue  # 单笔查询失败：跳过这笔，下一轮再试
        try:
            if str(result.get("code")) != "1":
                continue
            if str(result.get("status")) != "1":
                continue
            if not payments.amount_equal(result.get("money"),
                                          row["amount_cents"]):
                continue
        except Exception:
            continue
        if mark_order_paid(row["order_no"], row["pay_method"],
                           result.get("trade_no", "")):
            print(f"[epay-poll] 订单 {row['order_no']} 查单确认已支付，"
                  "已标记为已支付")
    for row in rc_rows:
        try:
            result = payments.epay_query_order(row["recharge_no"])
        except payments.PaymentNotConfigured:
            return
        except Exception:
            continue
        try:
            if str(result.get("code")) != "1":
                continue
            if str(result.get("status")) != "1":
                continue
            if not payments.amount_equal(result.get("money"),
                                          row["amount_cents"]):
                continue
        except Exception:
            continue
        if mark_recharge_paid(row["recharge_no"],
                              result.get("trade_no", "")):
            print(f"[epay-poll] 储值单 {row['recharge_no']} 查单确认已支付，"
                  "余额已入账")


def _epay_poll_loop():
    while True:
        try:
            epay_poll_once()
        except Exception:
            pass
        time.sleep(EPAY_POLL_INTERVAL_SECONDS)


# ------------------------------------------------------------------ 页面骨架

CSS = """
:root{--bg:#EDE9FB;--ink:#191423;--sub:#655E7A;--line:#DED4F2;
--card:rgba(255,255,255,.62);--accent:#101014;--radius:18px}
.chips{display:flex;gap:8px;flex-wrap:wrap;margin:8px 0 4px}
.chips label{margin:0}
.chips input{display:none}
.chips span{display:inline-block;padding:8px 18px;border-radius:999px;
border:1px solid var(--line);background:rgba(255,255,255,.6);
cursor:pointer;font-size:14.5px}
.chips input:checked+span{background:var(--ink);color:#fff;
border-color:var(--ink)}
.tabs{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 16px}
.tabs a{padding:7px 16px;border-radius:999px;text-decoration:none;
border:1px solid rgba(255,255,255,.7);background:rgba(255,255,255,.5);
font-size:14px;color:var(--ink)}
.tabs a.on{background:var(--ink);color:#fff;border-color:var(--ink)}
.sup-badge{display:inline-block;background:#DC2626;color:#fff;
border-radius:999px;font-size:11px;line-height:1.5;padding:0 6px;
margin-left:5px;vertical-align:2px}
.wallet-bal{font-size:34px;font-weight:800;margin:2px 0 10px}
.linkbtn{background:none;border:none;padding:0;color:var(--ink);
font:inherit;cursor:pointer;text-decoration:underline}
.chat{display:flex;flex-direction:column;gap:10px;max-height:56vh;
overflow-y:auto;padding:8px 2px}
.msg{max-width:78%;padding:9px 13px;border-radius:16px;font-size:14.5px;
line-height:1.55;white-space:pre-wrap;word-break:break-word}
.msg.me{align-self:flex-end;color:#fff;border-bottom-right-radius:6px;
background:linear-gradient(135deg,#7C5CFF,#B04FE0)}
.msg.them{align-self:flex-start;background:rgba(255,255,255,.88);
border:1px solid var(--line);border-bottom-left-radius:6px}
.msg .who{display:block;font-size:11px;opacity:.65;margin-bottom:2px}
.msg .tm{display:block;font-size:11px;opacity:.6;margin-top:4px}
.chat-form{display:flex;gap:8px;margin-top:12px;align-items:flex-end}
.chat-form textarea{flex:1;margin:0}
*{box-sizing:border-box}
body{margin:0;color:var(--ink);position:relative;z-index:0;
background:
radial-gradient(95vmin 95vmin at 88% -6%,rgba(147,197,253,.30),rgba(147,197,253,0) 62%),
radial-gradient(85vmin 85vmin at -6% 88%,rgba(196,181,253,.26),rgba(196,181,253,0) 62%),
var(--bg);
background-repeat:no-repeat;
font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;
font-size:15px;line-height:1.65;overflow-x:clip}
body::before,body::after{content:"";position:fixed;border-radius:50%;
filter:blur(96px);z-index:-1;pointer-events:none}
body::before{width:62vmin;height:62vmin;top:-14vmin;left:-10vmin;
background:radial-gradient(circle at 35% 35%,rgba(183,156,255,.68),rgba(183,156,255,.18) 70%);
animation:drift1 24s ease-in-out infinite alternate}
body::after{width:56vmin;height:56vmin;bottom:-16vmin;right:-9vmin;
background:radial-gradient(circle at 60% 40%,rgba(245,184,230,.66),rgba(245,184,230,.16) 70%);
animation:drift2 30s ease-in-out infinite alternate}
@keyframes drift1{from{transform:translate(0,0) scale(1)}
to{transform:translate(9vmin,7vmin) scale(1.14)}}
@keyframes drift2{from{transform:translate(0,0) scale(1.08)}
to{transform:translate(-8vmin,-9vmin) scale(.94)}}
@keyframes fadeUp{from{opacity:0;transform:translateY(14px)}
to{opacity:1;transform:translateY(0)}}
a{color:var(--ink)}
.wrap{max-width:1160px;margin:0 auto;padding:0 20px 64px}
header.top{background:rgba(255,255,255,.58);
backdrop-filter:blur(16px) saturate(1.5);
-webkit-backdrop-filter:blur(16px) saturate(1.5);
border-bottom:1px solid rgba(255,255,255,.65);
position:sticky;top:0;z-index:20;transition:transform .32s ease}
header.top.hdr-hide{transform:translateY(-100%)}
header.top .inner{max-width:1160px;margin:0 auto;padding:13px 20px;
display:flex;justify-content:space-between;align-items:center;gap:12px;
flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:10px;font-size:19px;
letter-spacing:.3px;text-decoration:none;font-weight:800}
.brand .logo{width:32px;height:32px;border-radius:10px;flex:none;
background:linear-gradient(135deg,#3B82F6,#8B5CF6 55%,#EC4899);
display:inline-flex;align-items:center;justify-content:center;
color:#fff;font-size:17px;box-shadow:0 4px 10px rgba(99,102,241,.35)}
nav{display:flex;align-items:center;gap:4px;flex-wrap:wrap}
nav a{padding:6px 13px;border-radius:999px;text-decoration:none;
color:var(--sub);font-size:14px}
nav a:hover{background:rgba(255,255,255,.78);color:var(--ink)}
#langSel{width:auto;margin-left:8px;padding:4px 8px;font-size:13px;
border-radius:999px;background:rgba(255,255,255,.7);color:var(--sub)}
h1{font-weight:800;line-height:1.3;font-size:24px;margin:6px 0 12px}
.card{background:var(--card);border:1px solid rgba(255,255,255,.72);
border-radius:var(--radius);padding:28px;margin-bottom:20px;
backdrop-filter:blur(18px) saturate(1.45);
-webkit-backdrop-filter:blur(18px) saturate(1.45);
box-shadow:0 14px 34px rgba(109,72,214,.12),inset 0 1px 0 rgba(255,255,255,.65);
animation:fadeUp .5s ease both}
.price{font-size:32px;font-weight:800}
.price small{font-size:14px;color:var(--sub);font-weight:400}
.btn{display:inline-block;background:var(--accent);color:#fff;
border:1px solid var(--accent);border-radius:999px;padding:11px 26px;
font-size:15px;cursor:pointer;text-decoration:none;font-weight:600}
.btn:hover{opacity:.88}
.btn.secondary{background:rgba(255,255,255,.75);color:var(--ink);border-color:var(--line)}
.btn.danger{background:#B3261E;border-color:#B3261E;color:#fff}
.btnrow{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px}
.btn.xs{padding:6px 14px;font-size:13px}
.actgrid{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-top:8px}
.actgrid .btn{width:100%;text-align:center;padding-left:6px;padding-right:6px}
.delrow{margin-top:6px}
.delrow .btn{display:block;width:100%;text-align:center}
.lvrow{display:flex;gap:14px;align-items:center;padding:12px 14px;
border:1px solid var(--line);border-radius:14px;margin:8px 0;
background:rgba(255,255,255,.55)}
.lvrow.on{border-color:var(--accent);background:rgba(139,92,246,.10)}
.lvrow .no{font-weight:800;color:var(--sub);min-width:26px}
.lvrow .nm{font-weight:700;min-width:104px;line-height:1.35}
.lvrow .dc{font-weight:700;min-width:86px}
.lvrow .rq{color:var(--sub);font-size:13px;margin-left:auto;text-align:right}
label{display:block;margin:14px 0 6px;font-size:14px;color:var(--sub)}
label b{color:#B3261E;font-weight:400}
input[type=email],input[type=password],input[type=text],select,textarea{
width:100%;padding:11px 14px;border:1px solid var(--line);
border-radius:12px;background:rgba(255,255,255,.78);font-size:15px}
input:focus,select:focus,textarea:focus{outline:2px solid #D3C2FF;
border-color:#A78BFA}
.err{background:#FDECEC;border:1px solid #F3B8B8;color:#8C1D18;
padding:10px 14px;border-radius:12px;margin-bottom:16px}
.ok{background:#EAF6EC;border:1px solid #B7DFC0;color:#1E5C2E;
padding:10px 14px;border-radius:12px;margin-bottom:16px}
.hint{color:var(--sub);font-size:13px}
table{width:100%;border-collapse:collapse;font-size:14px}
th,td{border-bottom:1px solid var(--line);padding:10px 8px;
text-align:left;vertical-align:top}
.badge{display:inline-block;border:1px solid var(--line);background:rgba(255,255,255,.55);
border-radius:999px;padding:1px 10px;font-size:12px;white-space:nowrap}
.qr{text-align:center}
.qr img,.qr svg{max-width:240px;height:auto}
footer{color:var(--sub);font-size:13px;text-align:center;margin-top:40px}
/* ---- 店面首页 ---- */
.shop-tools{max-width:760px;margin:26px auto 6px}
.search{display:flex;align-items:center;gap:9px;
background:rgba(255,255,255,.55);
border:1px solid rgba(255,255,255,.7);border-radius:14px;padding:0 16px;
backdrop-filter:blur(14px) saturate(1.4);
-webkit-backdrop-filter:blur(14px) saturate(1.4);
box-shadow:0 8px 22px rgba(109,72,214,.10)}
.search span{color:#98A2B3;font-size:16px}
.search input{border:none;padding:13px 0;font-size:15px;background:transparent}
.search input:focus{outline:none}
.pills{display:flex;gap:8px;flex-wrap:wrap;justify-content:center;
margin:18px 0 24px}
.pill{border:1px solid rgba(255,255,255,.7);
background:rgba(255,255,255,.5);backdrop-filter:blur(10px);
-webkit-backdrop-filter:blur(10px);color:var(--ink);
transition:all .18s;
border-radius:999px;padding:7px 16px;font-size:14px;cursor:pointer;
display:inline-flex;align-items:center;gap:6px}
.pill:hover{border-color:#B7A6F5;transform:translateY(-1px)}
.pill.on{background:var(--ink);color:#fff;border-color:var(--ink)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));
gap:18px}
.pcard{border-radius:22px;overflow:hidden;position:relative;
border:1px solid rgba(255,255,255,.68);
background:rgba(255,255,255,.5);
backdrop-filter:blur(16px) saturate(1.45);
-webkit-backdrop-filter:blur(16px) saturate(1.45);
box-shadow:0 10px 26px rgba(109,72,214,.10),inset 0 1px 0 rgba(255,255,255,.6);
text-decoration:none;color:var(--ink);display:flex;
flex-direction:column;transition:transform .22s,box-shadow .22s}
.pcard::before{content:"";position:absolute;inset:0;z-index:2;
border-radius:22px;padding:1.5px;pointer-events:none;
background:conic-gradient(from 210deg,
rgba(147,197,253,.55),rgba(240,171,252,.55),rgba(253,230,138,.5),
rgba(167,243,208,.5),rgba(147,197,253,.55));
-webkit-mask:linear-gradient(#000 0 0) content-box,
linear-gradient(#000 0 0);-webkit-mask-composite:xor;
mask-composite:exclude}
html.fx .pcard{opacity:0}
html.fx .pcard.in{opacity:1;animation:fadeUp .6s ease backwards}
.pcard:hover{transform:translateY(-5px);
box-shadow:0 20px 40px rgba(109,72,214,.20),inset 0 1px 0 rgba(255,255,255,.7)}
.pcard .art{height:168px;display:flex;align-items:center;justify-content:center}
.pcard .tile{width:86px;height:86px;border-radius:50%;background:#fff;
display:flex;align-items:center;justify-content:center;
box-shadow:0 12px 26px rgba(109,72,214,.18);
transition:transform .25s}
.pcard .tile.sq{border-radius:26px}
.pcard .info{padding:16px 18px 18px;display:flex;flex-direction:column;
gap:5px;flex:1}
.pcard .cat{font-size:11px;letter-spacing:2.5px;color:#98A2B3;font-weight:600}
.pcard .name{font-size:18.5px;font-weight:700;line-height:1.35;flex:1}
.pcard .row{display:flex;align-items:center;justify-content:space-between;
margin-top:10px}
.pcard .amount{font-size:19px;font-weight:800}
.buy{background:var(--ink);color:#fff;border-radius:999px;
padding:8px 16px;font-size:13.5px;font-weight:600;white-space:nowrap}
.empty-tip{text-align:center;color:var(--sub);padding:34px 0;display:none}
@media(max-width:560px){.card{padding:20px}.price{font-size:27px}
table{font-size:13px}.pcard .art{height:140px}}

.buy{transition:all .2s}
.pcard:hover .buy{background:#6D28D9;
box-shadow:0 8px 18px rgba(109,40,217,.35)}
.pcard:hover .tile{transform:translateY(-4px) scale(1.05)}
.anchor{margin-top:8px;font-size:12.5px;color:var(--sub)}
.anchor s{color:#98A2B3}
.anchor .save{display:inline-block;margin-left:6px;padding:1px 8px;
border-radius:999px;background:#FDE8E8;color:#C81E1E;font-weight:700;
font-size:12px}
.trustbar{margin:14px 2px 2px;font-size:13.5px;color:#4A4360}
.pcard.soldout{opacity:.55;pointer-events:none}
.buy.off{background:#98A2B3}
.inv-form input[type=number]{width:90px}
@media (prefers-reduced-motion: reduce){
body::before,body::after,.pcard,.card{animation:none}
html.fx .pcard{opacity:1}
header.top{transition:none}
.pcard,.pill,.pcard .tile,.buy{transition:none}}
/* ---- 登录 / 注册 ---- */
.auth-wrap{max-width:428px;margin:6vh auto 0}
.auth{padding:38px 36px 30px;border-radius:24px}
.auth .mark{width:56px;height:56px;border-radius:17px;margin:0 auto 14px;
background:linear-gradient(135deg,#3B82F6,#8B5CF6 55%,#EC4899);
color:#fff;display:flex;align-items:center;justify-content:center;
font-size:27px;box-shadow:0 12px 24px rgba(139,92,246,.42)}
.auth h1{text-align:center;font-size:23px;margin:0 0 6px}
.auth .sub{text-align:center;color:var(--sub);font-size:13.5px;margin:0 0 8px}
.auth label{margin:16px 0 7px;font-weight:600;color:#4A4360;font-size:13.5px}
.auth input[type=email],.auth input[type=password]{
padding:13px 15px;border-radius:14px;
box-shadow:inset 0 1px 3px rgba(109,72,214,.06)}
.btn.grad{background:linear-gradient(135deg,#3B82F6,#8B5CF6 55%,#EC4899);
border:none;box-shadow:0 10px 22px rgba(139,92,246,.35);transition:all .2s}
.btn.grad:hover{opacity:1;transform:translateY(-1px);
box-shadow:0 14px 28px rgba(139,92,246,.45)}
.btn.block{display:block;width:100%;text-align:center;
padding:13px 26px;font-size:16px;margin-top:22px}
.auth .alt{text-align:center;margin-top:18px}
.auth .alt a{color:#6D28D9;font-weight:600;text-decoration:none}
.auth .alt a:hover{text-decoration:underline}
@media(max-width:560px){.auth{padding:30px 22px 24px}}
/* ---- 公告 / QQ / 交付 / 教程 ---- */
.notice{display:flex;gap:10px;align-items:center;justify-content:center;
flex-wrap:wrap;background:rgba(255,255,255,.6);
border:1px solid rgba(255,255,255,.7);border-radius:14px;
padding:11px 16px;margin:22px auto 0;max-width:920px;
backdrop-filter:blur(12px) saturate(1.4);
-webkit-backdrop-filter:blur(12px) saturate(1.4);
box-shadow:0 8px 22px rgba(109,72,214,.10);font-size:14px;
animation:fadeUp .5s ease both}
.notice a{color:#6D28D9;font-weight:700;text-decoration:none;white-space:nowrap}
.notice-x{margin-left:auto;background:none;border:none;font-size:18px;
cursor:pointer;color:var(--sub);line-height:1;padding:0 2px}
.news-rot{flex:1;text-align:center}
.news-item{display:none;color:inherit;font-weight:600;white-space:normal}
.news-item.on{display:block;animation:fadeUp .45s ease both}
.wbadge{display:inline-block;font-size:11px;line-height:1.5;
padding:1px 8px;border-radius:999px;background:#e8f7ee;color:#12703a;
border:1px solid #bfe6cd;margin:5px 0 1px}
.wbadge.off{background:#f1f1f4;color:#777;border-color:#ddd}
.qqbox{background:rgba(124,92,246,.08);border:1px solid rgba(124,92,246,.28);
border-radius:14px;padding:13px 15px;margin:14px 0;font-size:14px;line-height:1.65}
.qqbox .qqnum{font-size:17px;color:#6D28D9;letter-spacing:.5px}
.copybtn{margin-left:8px;background:#6D28D9;color:#fff;border:none;
border-radius:999px;padding:3px 12px;font-size:12.5px;cursor:pointer;
vertical-align:2px;white-space:nowrap}
.copybtn:hover{opacity:.88}
.delivery{background:rgba(30,140,70,.07);border:1px solid rgba(30,140,70,.30);
border-radius:12px;padding:10px 12px;margin-top:9px}
.delivery .dt{font-weight:700;font-size:13px;color:#1E7A3C;margin-bottom:6px}
.delivery pre{margin:0;white-space:pre-wrap;word-break:break-all;
font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13.5px;
background:rgba(255,255,255,.68);border-radius:8px;padding:8px 10px}
.guide h2{font-size:17.5px;margin:20px 0 8px}
.guide h2:first-of-type{margin-top:6px}
.guide ol,.guide ul{margin:0;padding-left:22px}
.guide li{margin:6px 0}
/* ---- 订单详情页 ---- */
.detail-wrap{max-width:780px;margin:0 auto}
.hero{text-align:center;padding:8px 0 2px}
.hero .ring{width:76px;height:76px;border-radius:50%;margin:0 auto 12px;
display:flex;align-items:center;justify-content:center;
font-size:38px;color:#fff;background:#22C55E;
box-shadow:0 14px 30px rgba(34,197,94,.38)}
.hero .ring.wait{background:#F59E0B;box-shadow:0 14px 30px rgba(245,158,11,.35)}
.hero .ring.bad{background:#DC2626;box-shadow:0 14px 30px rgba(220,38,38,.32)}
.hero .ring.grey{background:#94A3B8;box-shadow:0 14px 30px rgba(148,163,184,.35)}
.hero h1{font-size:23px;margin:0 0 4px}
.hero .ono{color:var(--sub);font-size:13.5px}
.sect{font-size:18px;font-weight:800;margin:2px 0 10px}
.chead{display:flex;align-items:center;justify-content:space-between;
gap:10px;flex-wrap:wrap}
.btn.sm{padding:8px 18px;font-size:14px}
.btnrow.center{justify-content:center}
.delivery.big pre{font-size:14.5px;padding:13px 14px}
"""


def tint_rgba(hex_color, alpha):
    h = str(hex_color).lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return f"rgba({r},{g},{b},{alpha})"




HDR_JS = """
<script>
(function(){
  if(window.matchMedia('(prefers-reduced-motion: reduce)').matches)
    return;
  var hdr = document.querySelector('header.top');
  if(!hdr) return;
  var lastY = window.scrollY || 0, ticking = false;
  function onScroll(){
    var y = window.scrollY || 0;
    if(y > 160 && y > lastY + 4) hdr.classList.add('hdr-hide');
    else if(y < lastY - 4 || y <= 160)
      hdr.classList.remove('hdr-hide');
    lastY = y; ticking = false;
  }
  window.addEventListener('scroll', function(){
    if(!ticking){
      ticking = true;
      requestAnimationFrame(onScroll);
    }
  }, {passive: true});
})();
</script>"""

REVEAL_JS = """
<script>
(function(){
  var cards = document.querySelectorAll('.pcard');
  if(!cards.length) return;
  if(window.matchMedia('(prefers-reduced-motion: reduce)').matches){
    cards.forEach(function(el){ el.classList.add('in'); });
    return;
  }
  if(!('IntersectionObserver' in window)){
    cards.forEach(function(el){ el.classList.add('in'); });
    return;
  }
  var io = new IntersectionObserver(function(es){
    es.forEach(function(e){
      if(e.isIntersecting){
        var el = e.target;
        var idx = Array.prototype.indexOf.call(cards, el);
        el.style.animationDelay = ((idx % 4) * 0.07) + 's';
        el.classList.add('in');
        io.unobserve(el);
      }
    });
  }, {threshold: 0.08});
  cards.forEach(function(el){ io.observe(el); });
})();
</script>"""


def esc(value):
    return html.escape(str(value if value is not None else ""), quote=True)


def page(title, body, user=None, flash_ok="", flash_err=""):
    lang_opts = "".join(
        f'<option value="{code}"'
        f'{" selected" if code == cur_lang() else ""}>{label}</option>'
        for code, label in i18n.LANGS)
    lang_sel = ('<select id="langSel" aria-label="Language" '
                'onchange="if(this.value)location.href='
                '\'/lang/\'+this.value">' + lang_opts + '</select>')
    if user:
        nav = (f'<a href="/">{T("nav.home")}</a>'
               f'<a href="/order">{T("nav.order")}</a>'
               f'<a href="/my-orders">{T("nav.my_orders")}</a>'
               f'<a href="/wallet">{T("nav.wallet")}</a>'
               f'<a href="/support">{T("nav.support")}'
               '<span class="sup-badge" id="supBadge" style="display:none"></span></a>'
               f'<a href="/guide">{T("nav.guide")}</a>'
               + ('<a href="/admin">卖家后台</a>' if user["is_admin"] else '')
               + f'<a href="/logout">{T("nav.logout")}</a>' + lang_sel)
    else:
        nav = (f'<a href="/">{T("nav.home")}</a>'
               f'<a href="/login">{T("nav.login")}</a>'
               f'<a href="/register">{T("nav.register")}</a>'
               f'<a href="/track">{T("nav.track")}</a>'
               f'<a href="/guide">{T("nav.guide")}</a>' + lang_sel)
    flashes = ""
    if flash_ok:
        flashes += f'<div class="ok">{esc(flash_ok)}</div>'
    if flash_err:
        flashes += f'<div class="err">{esc(flash_err)}</div>'
    badge_js = ""
    if user and not user["is_admin"]:
        badge_js = """<script>
(function(){
  var b = document.getElementById('supBadge');
  if(!b) return;
  function check(){
    fetch('/support/unread', {credentials:'same-origin'})
      .then(function(r){ return r.json(); })
      .then(function(d){
        if(d.count > 0){ b.textContent = d.count; b.style.display = ''; }
        else { b.style.display = 'none'; }
      }).catch(function(){});
  }
  check();
  setInterval(check, 30000);
})();
</script>"""
    base = config.site_base_url()
    og_url = (base + "/") if base else "/"
    og_image = (base + "/favicon.svg") if base else "/favicon.svg"
    return f"""<!DOCTYPE html>
<html lang="{cur_lang()}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{esc(SITE_DESC)}">
<meta property="og:title" content="{esc(title)} · {esc(SITE_NAME)}">
<meta property="og:description" content="{esc(SITE_DESC)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{esc(og_url)}">
<meta property="og:image" content="{esc(og_image)}">
<meta property="og:site_name" content="{esc(SITE_NAME)}">
<meta name="twitter:card" content="summary">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<title>{esc(title)} · {esc(SITE_NAME)}</title><style>{CSS}</style>
<script>if(!window.matchMedia('(prefers-reduced-motion: reduce)').matches)
document.documentElement.className += ' fx';</script></head>
<body><header class="top"><div class="inner">
<a class="brand" href="/"><span class="logo">✦</span>{esc(SITE_NAME)}</a><nav>{nav}</nav>
</div></header><div class="wrap">{flashes}{body}
<footer>{esc(SITE_NAME)} · {T('footer.tag')}<br>
<a href="/privacy">{T('footer.privacy')}</a> · <a href="/terms">{T('footer.terms')}</a> ·
<a href="/cookies">{T('footer.cookies')}</a> · <a href="/guide">{T('nav.guide')}</a></footer>
</div>{badge_js}{HDR_JS}</body></html>"""


# 全站安全响应头。不加 CSP：站内大量内联样式/脚本，避免误伤。
SECURITY_HEADERS = [
    ("Strict-Transport-Security", "max-age=31536000"),
    ("X-Content-Type-Options", "nosniff"),
    ("X-Frame-Options", "SAMEORIGIN"),
    ("Referrer-Policy", "strict-origin-when-cross-origin"),
]

ROBOTS_TXT = """User-agent: *
Allow: /
Disallow: /admin
Sitemap: https://muse798.com/sitemap.xml
"""

SITEMAP_XML = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://muse798.com/</loc></url>
  <url><loc>https://muse798.com/guide</loc></url>
  <url><loc>https://muse798.com/privacy</loc></url>
  <url><loc>https://muse798.com/terms</loc></url>
  <url><loc>https://muse798.com/cookies</loc></url>
</urlset>
"""


def csrf_field(session):
    return (f'<input type="hidden" name="csrf" '
            f'value="{esc(session["csrf"])}">')


# ------------------------------------------------------------------ 请求处理

class Handler(BaseHTTPRequestHandler):
    server_version = "GeminiStore/1.0"
    _head_only = False  # do_HEAD 时为 True：同状态同头、只抑制 body

    # ---------- 基础设施 ----------
    def log_message(self, fmt, *args):
        print(f"[{self.log_date_time_string()}] {fmt % args}")

    def _client_ip(self):
        """客户端 IP：站点在 Caddy 反代之后，优先取 X-Forwarded-For 首项。"""
        xff = self.headers.get("X-Forwarded-For") or ""
        if xff:
            return xff.split(",")[0].strip()
        return self.client_address[0]

    def _security_headers(self):
        for k, v in SECURITY_HEADERS:
            self.send_header(k, v)

    def _write_body(self, data):
        if not self._head_only:
            self.wfile.write(data)

    def send_html(self, text, status=200, extra_headers=None):
        data = text.encode("utf-8")
        self.send_response(status)
        self._security_headers()
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        for k, v in (extra_headers or []):
            self.send_header(k, v)
        self.end_headers()
        self._write_body(data)

    def send_text(self, text, status=200, content_type="text/plain"):
        data = text.encode("utf-8")
        self.send_response(status)
        self._security_headers()
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self._write_body(data)

    def redirect(self, location, extra_headers=None):
        self.send_response(302)
        self._security_headers()
        self.send_header("Location", location)
        for k, v in (extra_headers or []):
            self.send_header(k, v)
        self.end_headers()

    def read_form(self):
        length = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(length) if length else b""
        parsed = parse_qs(raw.decode("utf-8", "replace"))
        return {k: v[0] for k, v in parsed.items()}, raw

    def session(self):
        cookie = SimpleCookie(self.headers.get("Cookie") or "")
        morsel = cookie.get("sid")
        if not morsel:
            return None, None
        conn = db()
        row = conn.execute(
            "SELECT s.token, s.csrf, s.created_at, u.* FROM sessions s"
            " JOIN users u ON u.id = s.user_id WHERE s.token=?",
            (morsel.value,)).fetchone()
        conn.close()
        if row is None:
            return None, None
        if time.time() - row["created_at"] > SESSION_TTL:
            return None, None
        return row, row  # (session+user 合并行, user)

    def require_login(self):
        session, user = self.session()
        if user is None:
            self.redirect("/login")
            return None, None
        return session, user

    def check_csrf(self, session, form):
        return session is not None and secrets.compare_digest(
            form.get("csrf", ""), session["csrf"])

    def start_session(self, user_id):
        token = secrets.token_urlsafe(32)
        csrf = secrets.token_urlsafe(24)
        conn = db()
        conn.execute(
            "INSERT INTO sessions (token, user_id, csrf, created_at)"
            " VALUES (?,?,?,?)", (token, user_id, csrf, int(time.time())))
        conn.commit()
        conn.close()
        return (f"sid={token}; Path=/; HttpOnly; SameSite=Lax; "
                f"Max-Age={SESSION_TTL}")

    # ---------- 路由 ----------
    def _resolve_lang(self):
        """分发前设定当前请求语言：/admin* 强制中文（店主自用）；
        其余按 Cookie lang → Accept-Language → zh。"""
        path = urlparse(self.path).path
        if path.startswith("/admin"):
            set_cur_lang("zh")
            return
        cookie_lang = ""
        try:
            jar = SimpleCookie(self.headers.get("Cookie", ""))
            if "lang" in jar:
                cookie_lang = jar["lang"].value
        except Exception:
            cookie_lang = ""
        set_cur_lang(i18n.negotiate(
            cookie_lang, self.headers.get("Accept-Language", "")))

    def do_GET(self):
        self._head_only = False
        self._dispatch_get()

    def do_HEAD(self):
        # 与 GET 同路由、同状态、同响应头（含 Content-Length 原值），
        # 只是不输出 body —— 在 send_html/send_text 里统一抑制。
        self._head_only = True
        self._dispatch_get()

    def _dispatch_get(self):
        self._resolve_lang()
        path = urlparse(self.path).path
        query = {k: v[0] for k, v in
                 parse_qs(urlparse(self.path).query).items()}
        if path.startswith("/lang/"):
            code = path.split("/")[2] if path.count("/") >= 2 else ""
            if code in i18n.LANG_CODES:
                target = "/"
                ref = urlparse(self.headers.get("Referer", ""))
                if ref.path and ref.path.startswith("/") \
                        and not ref.path.startswith("/lang/"):
                    target = ref.path
                return self.redirect(target, [(
                    "Set-Cookie",
                    f"lang={code}; Path=/; Max-Age=31536000; "
                    "SameSite=Lax")])
            return self.redirect("/")
        routes = {
            "/": self.home,
            "/register": self.register_page,
            "/login": self.login_page,
            "/logout": self.logout,
            "/order": self.order_page,
            "/my-orders": self.my_orders_page,
            "/admin/login": self.admin_login_page,
            "/admin": self.admin_orders_page,
            "/admin/products": self.admin_products_page,
            "/guide": self.guide_page,
            "/wallet": self.wallet_page,
            "/admin/wallet": self.admin_wallet_page,
            "/support": self.support_page,
            "/support/poll": self.support_poll,
            "/support/unread": self.support_unread,
            "/admin/support": self.admin_support_page,
            "/admin/support/poll": self.admin_support_poll,
            "/track": self.track_page,
            "/forgot": self.forgot_page,
            "/privacy": self.privacy_page,
            "/terms": self.terms_page,
            "/cookies": self.cookies_page,
            "/admin/orders/delete-all": self.admin_delete_all_page,
        }
        if path in routes:
            routes[path](query)
        elif path == "/robots.txt":
            self.send_text(ROBOTS_TXT)
        elif path == "/sitemap.xml":
            self.send_text(SITEMAP_XML, content_type="application/xml")
        elif path == "/favicon.svg":
            self.send_text(FAVICON_SVG, content_type="image/svg+xml")
        elif path == "/favicon.ico":
            self.redirect("/favicon.svg")
        elif path == "/pay/notify/epay":
            self.notify_epay(query)
        elif path == "/pay/return/epay":
            self.pay_return_epay(query)
        elif path.startswith("/wallet/pay/") and path.count("/") == 3:
            self.wallet_pay_page(path.split("/")[3])
        elif path.startswith("/admin/support/") and path.count("/") == 3:
            self.admin_support_thread(path.split("/")[3])
        elif path.startswith("/orders/") and path.count("/") == 2:
            self.order_detail_page(path.split("/")[2])
        elif path.startswith("/pay/") and path.count("/") == 2:
            self.pay_page(path.split("/")[2])
        else:
            self.not_found()

    def not_found(self):
        """品牌 404：未知路径返回站内统一布局的中文页（状态码 404）。
        支付回调等接口路径都是显式路由，不会落到这里，行为不受影响。"""
        _, user = self.session()
        body = f"""<div class="card">
          <h1>{T('nf.title')}</h1>
          <p>{T('nf.body')}</p>
          <div class="btnrow"><a class="btn grad" href="/">{T('nf.home')}</a>
          <a class="btn secondary" href="/guide">{T('nf.guide')}</a></div>
        </div>"""
        self.send_html(page(T("nf.title"), body, user), 404)

    def do_POST(self):
        self._resolve_lang()
        path = urlparse(self.path).path
        form, raw = self.read_form()
        if path == "/register":
            self.register(form)
        elif path == "/login":
            self.login(form, admin_only=False)
        elif path == "/admin/login":
            self.login(form, admin_only=True)
        elif path == "/track":
            self.track_lookup(form)
        elif path == "/order":
            self.create_order(form)
        elif path == "/wallet/recharge":
            self.create_recharge(form)
        elif path == "/support/send":
            self.support_send(form)
        elif path.startswith("/orders/") and path.endswith("/cancel"):
            self.order_cancel(path.split("/")[2], form)
        elif path.startswith("/admin/support/") \
                and path.endswith("/send"):
            self.admin_support_send(path.split("/")[3], form)
        elif path.startswith("/wallet/pay/") \
                and path.endswith("/epay-alipay"):
            self.wallet_pay_epay(path.split("/")[3], form)
        elif path.startswith("/pay/") and path.endswith("/balance"):
            self.pay_balance(path.split("/")[2], form)
        elif path == "/admin/wallet/adjust":
            self.admin_wallet_adjust(form)
        elif path == "/admin/wallet/set-level":
            self.admin_wallet_set_level(form)
        elif path == "/admin/wallet/reset-password":
            self.admin_reset_password(form)
        elif path == "/admin/inventory":
            self.admin_inventory(form)
        elif path == "/admin/products/save":
            self.admin_product_save(form)
        elif path == "/admin/products/add":
            self.admin_product_add(form)
        elif path == "/admin/products/delete":
            self.admin_product_delete(form)
        elif path.startswith("/pay/notify/alipay"):
            self.notify_alipay(form)
        elif path.startswith("/pay/notify/wechat"):
            self.notify_wechat(raw)
        elif path == "/pay/notify/epay":
            self.notify_epay(form)
        elif path.startswith("/pay/") and path.endswith("/epay-alipay"):
            self.pay_epay(path.split("/")[2], form, "alipay")
        elif path == "/admin/orders/delete-all":
            self.admin_delete_all(form)
        elif path.startswith("/admin/orders/") and path.endswith("/action"):
            self.admin_action(path.split("/")[3], form)
        elif path.startswith("/admin/orders/") and path.endswith("/delete"):
            self.admin_delete_order(path.split("/")[3], form)
        else:
            self.not_found()

    # ---------- 公共页面 ----------
    def home(self, query):
        _, user = self.session()
        catalog = catalog_products()
        cats = []
        for p in catalog:
            if p["cat"] not in cats:
                cats.append(p["cat"])
        cat_label = {p["cat"]: {"openai": "OpenAI"}.get(
            p["cat"], p["cat"].capitalize()) for p in catalog}
        if cur_lang() != "zh":
            cmap = (i18n.CAT_I18N.get(cur_lang())
                    or i18n.CAT_I18N.get("en") or {})
            cat_label = {c: cmap.get(c, lbl)
                         for c, lbl in cat_label.items()}
        pills = [f'<button class="pill on" data-cat="all">'
                 f'{T("home.all")}</button>']
        for c in cats:
            pills.append(
                f'<button class="pill" data-cat="{esc(c)}">'
                f'{esc(cat_label[c])}</button>')
        stocks = get_all_stock()
        stats = store_stats()
        cards = []
        for p in catalog:
            tile_cls = "tile sq" if p["cat"] == "gemini" else "tile"
            stock = stocks.get(p["id"], -1)
            sold_n = stats["per_product"].get(p["id"], 0)
            sold_html = (f'<div class="anchor">'
                         f'{T("home.sold_n", n=sold_n)}</div>'
                         if sold_n > 0 else "")
            lname, _lpoints = loc_product(p)
            wb_html = warranty_html(p["id"])
            anchor = ""
            if p.get("official_price"):
                anchor = (f'<div class="anchor">{esc(p["official_note"])} '
                          f'<s>{esc(p["official_price"])}</s>'
                          f'<span class="save">{esc(p["save_text"])}</span>'
                          f'</div>')
            if stock == 0:
                cards.append(f"""
        <div class="pcard soldout"
           data-cat="{esc(p['cat'])}" data-name="{esc(lname)}">
          <div class="art" style="background:{tint_rgba(p['tint'], .55)}">
            <div class="{tile_cls}">{p['icon']}</div>
          </div>
          <div class="info" style="background:{tint_rgba(p['tint'], .30)}">
            <div class="cat">{esc(p['cat_label'])}</div>
            <div class="name">{esc(lname)}</div>{wb_html}
            <div class="row">
              <span class="amount">¥{p['price_cents'] / 100:.2f}</span>
              <span class="buy off">{T('home.soldout')}</span>
            </div>{anchor}{sold_html}
          </div>
        </div>""")
                continue
            if stock < 0:
                low = (f'<div class="anchor">'
                       f'{T("home.stock_plenty")}</div>')
            elif stock <= 9:
                low = (f'<div class="anchor">'
                       f'{T("home.stock_low", n=stock)}</div>')
            else:
                low = (f'<div class="anchor">'
                       f'{T("home.stock_n", n=stock)}</div>')
            cards.append(f"""
        <a class="pcard" href="/order?pid={p['id']}"
           data-cat="{esc(p['cat'])}" data-name="{esc(lname)}">
          <div class="art" style="background:{tint_rgba(p['tint'], .55)}">
            <div class="{tile_cls}">{p['icon']}</div>
          </div>
          <div class="info" style="background:{tint_rgba(p['tint'], .30)}">
            <div class="cat">{esc(p['cat_label'])}</div>
            <div class="name">{esc(lname)}</div>{wb_html}
            <div class="row">
              <span class="amount">¥{p['price_cents'] / 100:.2f}</span>
              <span class="buy">{T('home.buy')}</span>
            </div>{anchor}{low}{sold_html}
          </div>
        </a>""")
        trust = esc(trust_line(stats))
        anns = ANNOUNCEMENTS
        if cur_lang() != "zh":
            anns = (i18n.ANNOUNCEMENTS_I18N.get(cur_lang())
                    or i18n.ANNOUNCEMENTS_I18N.get("en")
                    or ANNOUNCEMENTS)
        news_items = "".join(
            f'<a class="news-item{" on" if i == 0 else ""}"'
            f' href="{esc(href)}">{esc(text)}</a>'
            for i, (text, href) in enumerate(anns))
        body = f"""
        <div class="notice" id="noticeBar" style="display:none">
          <div class="news-rot" id="newsRot">{news_items}</div>
          <button class="notice-x" id="noticeClose" type="button"
                  aria-label="关闭公告">×</button>
        </div>
        <script>
        (function(){{
          var bar = document.getElementById('noticeBar');
          try{{
            if(!localStorage.getItem('noticeClosed'))
              bar.style.display = 'flex';
            document.getElementById('noticeClose').onclick = function(){{
              localStorage.setItem('noticeClosed', '1');
              bar.style.display = 'none'; }};
          }}catch(e){{ bar.style.display = 'flex'; }}
          var items = document.querySelectorAll('#newsRot .news-item');
          if(items.length > 1){{
            var ni = 0;
            setInterval(function(){{
              items[ni].classList.remove('on');
              ni = (ni + 1) % items.length;
              items[ni].classList.add('on');
            }}, 4000);
          }}
        }})();
        </script>
        <div class="shop-tools">
          <div class="search"><span>⌕</span>
            <input id="q" type="text" placeholder="{T('home.search_ph')}"></div>
        </div>
        <div class="pills">{''.join(pills)}</div>
        <p class="trustbar">{trust}</p>
        <div class="grid" id="shopGrid">{''.join(cards)}</div>
        <div class="empty-tip" id="emptyTip">{T('home.no_match')}</div>
        <script>
        (function(){{
          var cur='all', q=document.getElementById('q'),
              tip=document.getElementById('emptyTip');
          function apply(){{
            var kw=q.value.trim().toLowerCase(), n=0;
            document.querySelectorAll('.pcard').forEach(function(el){{
              var ok=(cur==='all'||el.dataset.cat===cur)
                     &&(!kw||el.dataset.name.toLowerCase().indexOf(kw)>=0);
              el.style.display=ok?'':'none'; if(ok)n++;
            }});
            tip.style.display=n?'none':'block';
          }}
          document.querySelectorAll('.pill').forEach(function(b){{
            b.addEventListener('click',function(){{
              document.querySelectorAll('.pill').forEach(function(x){{
                x.classList.remove('on');}});
              b.classList.add('on'); cur=b.dataset.cat; apply();
            }});
          }});
          q.addEventListener('input',apply);
        }})();
        </script>""" + REVEAL_JS
        self.send_html(page(T("home.title"), body, user))

    def register_page(self, query, err=""):
        body = f"""
        <div class="auth-wrap"><div class="card auth">
        <div class="mark">✦</div>
        <h1>{T('auth.register')}</h1>
        <p class="sub">{T('auth.register_sub')}</p>
        <form method="post" action="/register">
          <label>{T('auth.email')}</label>
          <input type="email" name="email" required
                 placeholder="you@example.com">
          <label>{T('auth.password_rule')}</label>
          <input type="password" name="password" required minlength="8"
                 placeholder="{T('auth.password_set_ph')}">
          <button class="btn grad block" type="submit">{T('auth.register')}</button></form>
        <p class="hint alt">{T('auth.have_account')}<a href="/login">{T('auth.go_login')}</a></p>
        </div></div>"""
        self.send_html(page(T("auth.register"), body, flash_err=err))

    def login_page(self, query, err=""):
        self._login_form("/login", T("auth.login"), err)

    def admin_login_page(self, query, err=""):
        self._login_form("/admin/login", "卖家后台登录", err)

    def _login_form(self, action, title, err=""):
        if action == "/login":
            sub = T("auth.login_sub")
            alt = (f'<p class="hint alt">{T("auth.no_account")}'
                   f'<a href="/register">{T("auth.register_now")}</a> · '
                   f'<a href="/forgot">{T("auth.forgot")}</a></p>'
                   f'<p class="hint alt">{T("auth.track_hint")}'
                   f'<a href="/track">{T("auth.track_link")}</a></p>')
            email_label = T("auth.email")
            pw_label = T("auth.password")
            pw_ph = T("auth.password_ph")
            btn = T("auth.login")
        else:
            sub = "店主专用入口"
            alt = ""
            email_label = "邮箱"
            pw_label = "密码"
            pw_ph = "请输入密码"
            btn = "登录"
        body = f"""
        <div class="auth-wrap"><div class="card auth">
        <div class="mark">✦</div>
        <h1>{title}</h1>
        <p class="sub">{sub}</p>
        <form method="post" action="{action}">
          <label>{email_label}</label>
          <input type="email" name="email" required
                 placeholder="you@example.com">
          <label>{pw_label}</label>
          <input type="password" name="password" required
                 placeholder="{pw_ph}">
          <button class="btn grad block" type="submit">{btn}</button></form>
        {alt}</div></div>"""
        self.send_html(page(title, body, flash_err=err))

    def register(self, form):
        email = form.get("email", "").strip()
        password = form.get("password", "")
        if not valid_email(email):
            return self.register_page({}, T("auth.err_email"))
        if len(password) < 8:
            return self.register_page({}, T("auth.err_pw_short"))
        conn = db()
        if conn.execute("SELECT id FROM users WHERE email=?",
                        (email,)).fetchone():
            conn.close()
            return self.register_page({}, T("auth.err_email_taken"))
        salt, pw_hash = hash_password(password)
        cur = conn.execute(
            "INSERT INTO users (email, salt, pass_hash, is_admin, created_at)"
            " VALUES (?,?,?,0,?)", (email, salt, pw_hash, now_text()))
        conn.commit()
        user_id = cur.lastrowid
        conn.close()
        cookie = self.start_session(user_id)
        self.redirect("/order", [("Set-Cookie", cookie)])

    def login(self, form, admin_only):
        email = form.get("email", "").strip()
        password = form.get("password", "")
        fail_page = (self.admin_login_page if admin_only
                     else self.login_page)
        # 限流：同 IP + 账号连续失败 LOGIN_MAX_FAILS 次锁定一段时间，
        # 锁定期间直接拒绝（不查密码），成功登录则清零计数。
        key = (self._client_ip(), email.lower())
        locked = _rate_locked_seconds(_login_fails, key)
        if locked:
            return fail_page({}, _lock_message(locked))
        conn = db()
        row = conn.execute("SELECT * FROM users WHERE email=?",
                           (email,)).fetchone()
        conn.close()
        if row is None or not check_password(row, password):
            _rate_record_fail(_login_fails, key,
                              LOGIN_MAX_FAILS, LOGIN_LOCK_SECONDS)
            return fail_page({}, T("auth.err_login"))
        if admin_only and not row["is_admin"]:
            _rate_record_fail(_login_fails, key,
                              LOGIN_MAX_FAILS, LOGIN_LOCK_SECONDS)
            return fail_page({}, "这个账号不是管理员账号")
        _rate_clear(_login_fails, key)
        cookie = self.start_session(row["id"])
        self.redirect("/admin" if admin_only else "/my-orders",
                      [("Set-Cookie", cookie)])

    def logout(self, query):
        cookie = SimpleCookie(self.headers.get("Cookie") or "")
        morsel = cookie.get("sid")
        if morsel:
            conn = db()
            conn.execute("DELETE FROM sessions WHERE token=?",
                         (morsel.value,))
            conn.commit()
            conn.close()
        self.redirect("/", [("Set-Cookie",
                             "sid=; Path=/; Max-Age=0; HttpOnly")])

    # ---------- 下单 ----------
    def guide_page(self, query):
        _, user = self.session()
        if cur_lang() != "zh":
            gblob = i18n.blob(cur_lang(), "guide")
            if gblob:
                body = (gblob + f"""
        <div class="card guide"><h2>{T('guide.contact')}</h2>
        {qq_box()}
        <p class="hint">{T('guide.contact_hint')}</p>
        </div>{copy_script()}""")
                return self.send_html(
                    page(T("nav.guide"), body, user))
        body = f"""
        <div class="card guide"><h1>使用教程</h1>
        <h2>一、通用购买流程</h2>
        <ol>
          <li><b>注册 / 登录</b>：用邮箱注册一个账号（下单和查订单都要用它）。</li>
          <li><b>选商品下单</b>：在首页点商品的“立即购买”，按提示填写资料并提交。</li>
          <li><b>付款</b>：目前支持<b>支付宝</b>付款。付款成功后订单会在约 1 分钟内
          自动变为“已支付 / 待充值”。</li>
          <li><b>等店主处理</b>：店主按付款顺序逐单处理，进度随时在
          “我的订单”里查看。</li>
        </ol>
        <h2>二、Gemini Pro 代充（需要您配合）</h2>
        <ol>
          <li>下单时填<b>要充值的 Google 邮箱</b>和<b>辅助邮箱</b>，两个都要填对。</li>
          <li>付款后请<b>添加店主 QQ（见下方）</b>，加好友时备注您的订单号，
          代充需要店主与您实时配合。</li>
          <li>完成后会员会充到您自己的 Google 账号里，时长 24 个月。</li>
        </ol>
        <p class="hint">⚠️ 重要：全程<b>不需要提供 Google 账号密码</b>，
        店主不会向您索要密码；任何人向您索要密码都不要给。</p>
        <h2>三、Muse 成品号（等收货即可）</h2>
        <ol>
          <li>下单时只需填<b>联系方式</b>，方便店主联系您。</li>
          <li>付款后店主会把<b>账号和密码发到您的订单里</b>：
          打开“我的订单”，在订单下方“交付内容”处查看，可一键复制。</li>
          <li>收到后请尽快登录 muse.ai 确认账号可用，并妥善保管账号密码。</li>
          <li>“词元”≈ AI 读写的文字量：1 亿词元约合数千万汉字，
          10 亿词元日常聊天、写作能用很久（约数，实际消耗看每次对话长短）。</li>
        </ol>
        <h2>四、付款与售后</h2>
        <ul>
          <li>付款后状态长时间（超过 10 分钟）没有更新，请联系店主 QQ 并发订单号。</li>
          <li>所有订单状态以“我的订单”页面显示为准。</li>
        </ul>
        <h2>售后与退款规则（请放心下单）</h2>
        <ul>
          <li><b>未交付可退</b>：订单还没交付（未标记“已完成”）之前，
          随时联系店主可取消并<b>全额退款</b>。</li>
          <li><b>退款到账方式</b>：用余额支付的订单，退款即时自动返还到
          您的站内余额；用支付宝支付的订单，由店主在支付宝侧原路退回。</li>
          <li><b>Gemini 代充</b>：因店主原因没能充上的，全额退款；
          填写的邮箱有误导致充错的，请第一时间联系店主核对处理；
          已成功充值到账的会员不支持无理由退款。</li>
          <li><b>Muse 成品号</b>：保首登——交付后请尽快完成首次登录
          确认；首次登录不上的，请第一时间联系店主（带订单号），
          核实后补发或退款；首次登录成功后账号的后续问题
          （含自行改密、违规使用等）不在质保范围。</li>
          <li>售后统一走<b>在线客服</b>或店主 QQ（见下方），请带上订单号。</li>
        </ul>
        <h2>五、储值与在线客服</h2>
        <ul>
          <li><b>储值</b>：在“我的钱包”可用支付宝提前储值；之后下单
          可直接用余额付款，不用每次跳支付宝。</li>
          <li><b>在线客服</b>：顶部导航“在线客服”能直接给店主留言，
          店主人工回复后，导航会有红色数字提醒。</li>
          <li>用余额支付的订单如退款，金额会自动返还到您的余额。</li>
        </ul>
        </div>
        <div class="card guide"><h2>联系店主</h2>
        {qq_box()}
        <p class="hint">工作时间一般都会在，留言请带订单号，处理更快。</p>
        </div>{copy_script()}"""
        self.send_html(page(T("nav.guide"), body, user))

    def order_page(self, query, err="", values=None):
        session, user = self.require_login()
        if user is None:
            return
        values = values or {}
        product = get_product(values.get("pid") or query.get("pid"))
        stock = get_stock(product["id"])
        if stock == 0 or not product.get("active", True):
            lname0, _ = loc_product(product)
            body = f"""
        <div class="card"><h1>{T('order.title')} · {esc(lname0)}</h1>
        <p>{T('order.soldout_body')}</p>
        <p class="hint">{T('order.soldout_hint', qq=SELLER_QQ)}</p>
        <p><a href="/">{T('order.back_home')}</a></p></div>"""
            self.send_html(page(T("order.soldout_title"), body, user,
                                flash_err=err))
            return
        anchor = ""
        if product.get("official_price"):
            anchor = (f'<div class="anchor">{esc(product["official_note"])} '
                      f'<s>{esc(product["official_price"])}</s>'
                      f'<span class="save">{esc(product["save_text"])}</span>'
                      f'</div>')
        lname, lpoints = loc_product(product)
        points_html = "".join(
            f"<li>{esc(pt)}</li>" for pt in lpoints)
        intro = f"<p>{esc(loc_field(product, 'desc'))}</p>"
        if points_html:
            intro += f"<ul>{points_html}</ul>"
        stock_hint = (f'<p class="hint">'
                      f'{T("order.stock_hint", n=stock)}</p>'
                      if 0 < stock <= 9 else "")
        trust = esc(trust_line())
        email_fields = ""
        if product.get("needs_email", True):
            email_fields = f"""
          <label>{esc(loc_field(product, 'first_label'))} <b>{T('order.required')}</b></label>
          <input type="email" name="google_email" required
                 value="{esc(values.get('google_email', ''))}">
          <label>{T('order.aux_label')} <b>{T('order.required')}</b></label>
          <input type="email" name="aux_email" required
                 value="{esc(values.get('aux_email', ''))}">
          <p class="hint">{T('order.aux_hint')}</p>"""
        qq = qq_box() if product["id"] == "gemini-pro-24m" else ""
        lvl = user_level(user)
        if lvl > 0:
            mp = member_price_cents(product["price_cents"], lvl)
            lname_l, llabel_l = loc_level(lvl)
            price_html = (
                f'<p class="price"><s style="font-size:20px;'
                f'color:var(--sub)">¥{product["price_cents"]/100:.2f}</s> '
                f'¥{mp/100:.2f} <small>{T("order.one_time")}'
                f'</small></p>'
                f'<p class="hint">'
                f'{T("order.member_line", name=lname_l, label=llabel_l, off=f"{(product["price_cents"]-mp)/100:.2f}")}</p>')
        else:
            price_html = (
                f'<p class="price">¥{product["price_cents"] / 100:.2f} '
                f'<small>{T("order.one_time")}</small></p>')
        body = f"""
        <div class="card"><h1>{T('order.title')} · {esc(lname)}</h1>
        {price_html}
        {anchor}{intro}{stock_hint}
        <form method="post" action="/order">
          {csrf_field(session)}
          <input type="hidden" name="pid" value="{esc(product['id'])}">
          {email_fields}
          <label>{T('order.contact_label')} <b>{T('order.required')}</b></label>
          <input type="text" name="contact" required
                 value="{esc(values.get('contact', ''))}"
                 placeholder="{T('order.contact_ph')}">
          <p class="hint">{esc(loc_field(product, 'password_hint'))}</p>
          <div class="btnrow">
            <button class="btn" type="submit">{T('order.submit')}</button>
          </div></form>
        <p class="hint">{trust}<br>{T('order.after_sale_pre')}
        <a href="/guide">{T('nav.guide')}</a>{T('order.after_sale_post')}</p>{qq}</div>{copy_script() if qq else ''}"""
        self.send_html(page(T("order.title"), body, user, flash_err=err))

    def create_order(self, form):
        session, user = self.require_login()
        if user is None:
            return
        if not self.check_csrf(session, form):
            return self.order_page({}, T("order.err_expired"), form)
        product = get_product(form.get("pid"))
        if get_stock(product["id"]) == 0 \
                or not product.get("active", True):
            return self.order_page({}, T("order.err_soldout"), form)
        google_email = form.get("google_email", "").strip()
        aux_email = form.get("aux_email", "").strip()
        contact = form.get("contact", "").strip()
        if product.get("needs_email", True):
            if not valid_email(google_email):
                return self.order_page({}, loc_field(product, "first_err") if "first_err" in product else product["first_err"], form)
            if not aux_email:
                return self.order_page({}, T("order.err_aux_required"), form)
            if not valid_email(aux_email):
                return self.order_page({}, T("order.err_aux_format"), form)
        else:
            google_email = ""
            aux_email = ""
        if not contact:
            return self.order_page({}, T("order.err_contact_required"), form)
        conn = db()
        order_no = make_order_no(conn)
        ts = now_text()
        conn.execute(
            "INSERT INTO orders (order_no, user_id, product_name,"
            " product_id, amount_cents, google_email, aux_email, contact,"
            " status, created_at, updated_at)"
            " VALUES (?,?,?,?,?,?,?,?, 'unpaid', ?, ?)",
            (order_no, user["id"], product["name"], product["id"],
             member_price_cents(product["price_cents"],
                                user_level(user)),
             google_email, aux_email, contact, ts, ts))
        conn.commit()
        conn.close()
        self.redirect(f"/pay/{order_no}")

    def get_order(self, order_no):
        conn = db()
        row = conn.execute("SELECT * FROM orders WHERE order_no=?",
                           (order_no,)).fetchone()
        conn.close()
        return row

    def my_orders_page(self, query):
        session, user = self.require_login()
        if user is None:
            return
        conn = db()
        rows = conn.execute(
            "SELECT * FROM orders WHERE user_id=? ORDER BY id DESC",
            (user["id"],)).fetchall()
        conn.close()
        if not rows:
            body = (f'<div class="card"><h1>{T("orders.title")}</h1>'
                    f'<p>{T("orders.empty")}</p><div class="btnrow">'
                    f'<a class="btn" href="/order">{T("orders.go_order")}</a></div></div>')
        else:
            items = ""
            need_script = False
            for r in rows:
                action = (f'<a href="/orders/{esc(r["order_no"])}">'
                          f'{T("orders.detail")}</a>')
                if r["status"] == "unpaid":
                    action += (f' · <a href="/pay/{esc(r["order_no"])}">'
                               f'{T("orders.pay")}</a>')
                    cc = T("orders.cancel_confirm").replace("'", "\\'")
                    action += (
                        f" · <form method=\"post\""
                        f" style=\"display:inline\""
                        f" action=\"/orders/{esc(r['order_no'])}/cancel\""
                        f" onsubmit=\"return confirm('{cc}')\">"
                        + csrf_field(session)
                        + "<button class=\"linkbtn\" type=\"submit\">"
                        + T("orders.cancel") + "</button></form>")
                # 店主备注仅卖家后台可见，客户页不渲染
                # （2026-11-08 店主由「客户可见」改为内部备注）
                note = ""
                delivery_html = ""
                if r["delivery"]:
                    need_script = True
                    delivery_html = f"""
                <div class="delivery" data-copywrap>
                  <div class="dt">{T('orders.delivery_title')}
                    <button class="copybtn" type="button">{T('common.copy')}</button></div>
                  <pre class="copytext">{esc(r['delivery'])}</pre>
                </div>"""
                qq_html = ""
                prod = order_product(r)
                if (prod and prod["id"] == "gemini-pro-24m"
                        and r["status"] in ("unpaid", "paid")):
                    need_script = True
                    qq_html = f"""
                <div class="hint" data-copywrap>{T('orders.gemini_qq_pre')}
                  <b class="copytext">{SELLER_QQ}</b><button class="copybtn"
                    type="button">{T('common.copy')}</button>{T('orders.gemini_qq_note')}</div>"""
                disp_name = r['product_name']
                _prod = order_product(r)
                if _prod:
                    disp_name, _ = loc_product(_prod)
                items += f"""<tr><td>{esc(r['order_no'])}<br>
                <span class="hint">{esc(r['created_at'])}</span></td>
                <td>{esc(disp_name)}<br>¥{r['amount_cents']/100:.2f}</td>
                <td><span class="badge">{esc(SL(r['status']))}</span>
                {note}{delivery_html}{qq_html}</td><td>{action}</td></tr>"""
            body = f"""<div class="card"><h1>{T('orders.title')}</h1>
            <table><tr><th>{T('orders.no')}</th><th>{T('orders.product')}</th><th>{T('orders.status')}</th><th></th></tr>
            {items}</table></div>{copy_script() if need_script else ''}"""
        self.send_html(page(T("orders.title"), body, user))

    def order_detail_page(self, order_no):
        session, user = self.require_login()
        if user is None:
            return
        order = self.get_order(order_no)
        if order is None or order["user_id"] != user["id"]:
            return self.send_html(
                page(T("detail.not_found"),
                     f"<h1>{T('detail.not_found')}</h1>", user), 404)
        status = order["status"]
        product = order_product(order)
        ring_cls, ring_char, hero_title = ORDER_HEROES.get(
            status, (" grey", "?", STATUS_LABELS.get(status, status)))
        if cur_lang() != "zh":
            hero_title = T(f"hero.{status}")
        tips = ORDER_TIPS
        tip_text = (tips.get(status, "") if cur_lang() == "zh"
                    else T(f"tip.{status}"))
        paid_line = (f"<br>{T('detail.paid_at')}{esc(order['paid_at'])}"
                     if order["paid_at"] else "")
        note_line = ""  # 店主备注仅卖家后台可见，客户页不渲染
        qq = ""
        if (product and product["id"] == "gemini-pro-24m"
                and status in ("unpaid", "paid")):
            qq = qq_box()
        delivery_html = ""
        if order["delivery"]:
            delivery_html = f"""
        <div class="card">
          <div class="chead"><div class="sect">{T('detail.delivery')}</div>
            <button class="btn grad sm" type="button" id="dlBtn">
              {T('detail.download_all')}</button></div>
          <p class="hint">{T('detail.delivery_keep')}</p>
          <div class="delivery big" data-copywrap>
            <div class="dt">{T('detail.delivery_account')}
              <button class="copybtn" type="button">{T('detail.copy_all')}</button></div>
            <pre class="copytext">{esc(order['delivery'])}</pre>
          </div>
        </div>
        <script>
        document.getElementById('dlBtn').addEventListener('click',
          function(){{
            var t = document.querySelector('.delivery pre').innerText;
            var blob = new Blob([t], {{type: 'text/plain;charset=utf-8'}});
            var a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = '{esc(order_no)}-{T('detail.file_suffix')}.txt';
            a.click();
            setTimeout(function(){{ URL.revokeObjectURL(a.href); }}, 800);
          }});
        </script>"""
        usage_items = order_usage_html(product)
        cancel_html = ""
        if status == "unpaid":
            primary = (f'<a class="btn grad" href="/pay/{esc(order_no)}">'
                       f'{T("orders.pay")}</a>')
            cc2 = T("orders.cancel_confirm2").replace("'", "\\'")
            cancel_html = (
                f"<form method=\"post\""
                f" action=\"/orders/{esc(order_no)}/cancel\""
                " style=\"display:inline\""
                f" onsubmit=\"return confirm('{cc2}')\">"
                + csrf_field(session)
                + "<input type=\"hidden\" name=\"back\""
                " value=\"detail\">"
                "<button class=\"btn secondary\" type=\"submit\">"
                + T("orders.cancel") + "</button></form>")
        else:
            primary = (f'<a class="btn" href="/my-orders">'
                       f'{T("detail.view_orders")}</a>')
        disp_name = order['product_name']
        if product:
            disp_name, _ = loc_product(product)
        body = f"""
        <div class="detail-wrap">
        <div class="card">
          <div class="hero">
            <div class="ring{ring_cls}">{ring_char}</div>
            <h1>{hero_title}</h1>
            <div class="ono">{T('detail.order_no')} {esc(order['order_no'])}</div>
          </div>
          <p>{T('detail.product')}{esc(disp_name)}<br>
          {T('detail.amount')}¥{order['amount_cents']/100:.2f}<br>
          {T('detail.created')}{esc(order['created_at'])}{paid_line}<br>
          {T('detail.status')}<span class="badge">{esc(SL(status))}</span>
          {note_line}</p>
          <p class="hint">{esc(tip_text)}</p>
          {qq}
        </div>
        {delivery_html}
        <div class="card guide"><div class="sect">{T('detail.usage')}</div>
        {usage_items}</div>
        <div class="btnrow center">{primary}
          {cancel_html}
          <a class="btn secondary" href="/">{T('detail.continue')}</a></div>
        </div>{copy_script() if order['delivery'] or qq else ''}"""
        self.send_html(page(T("detail.title"), body, user))

    def order_cancel(self, order_no, form):
        session, user = self.require_login()
        if user is None:
            return
        if not self.check_csrf(session, form):
            return self.redirect("/my-orders")
        order = self.get_order(order_no)
        if order is None or order["user_id"] != user["id"]:
            return self.send_html(
                page(T("detail.not_found"),
                     f"<h1>{T('detail.not_found')}</h1>", user), 404)
        if order["status"] == "unpaid":
            conn = db()
            conn.execute(
                "UPDATE orders SET status='cancelled', updated_at=?"
                " WHERE order_no=?", (now_text(), order_no))
            conn.commit()
            conn.close()
        if form.get("back") == "detail":
            return self.redirect(f"/orders/{order_no}")
        self.redirect("/my-orders")

    # ---------- 免登录查单 / 忘记密码 ----------
    def track_page(self, query, err=""):
        _, user = self.session()
        body = f"""<div class="card">
          <h1>{T('track.title')}</h1>
          <p class="hint">{T('track.intro')}</p>
          <form method="post" action="/track">
            <label>{T('track.order_no')}<input name="order_no" required
              placeholder="{T('track.order_no_ph')}"></label>
            <label>{T('track.contact')}<input name="contact" required
              placeholder="{T('track.contact_ph')}"></label>
            <p><button class="btn grad" type="submit">{T('track.submit')}</button></p>
          </form>
          <p class="hint">{T('track.alt_pre')}
          <a href="/login">{T('track.alt_login')}</a>{T('track.alt_mid')}{SELLER_QQ}{T('track.alt_post')}</p>
        </div>"""
        self.send_html(page(T("track.title"), body, user, flash_err=err))

    def track_lookup(self, form):
        ip = self._client_ip()
        locked = _rate_locked_seconds(_track_fails, ip)
        if locked:
            return self.track_page({}, _lock_message(locked))
        order_no = (form.get("order_no") or "").strip()
        contact = (form.get("contact") or "").strip()
        order = None
        if order_no and contact:
            conn = db()
            order = conn.execute(
                "SELECT * FROM orders WHERE order_no=? AND contact=?",
                (order_no, contact)).fetchone()
            conn.close()
        if order is None:
            # 统一提示，不区分是订单号错还是联系方式错，防枚举
            _rate_record_fail(_track_fails, ip,
                              TRACK_MAX_FAILS, TRACK_LOCK_SECONDS)
            return self.track_page({}, T("track.err_notfound"))
        _rate_clear(_track_fails, ip)
        _, user = self.session()
        self.send_html(page(T("track.result_title"),
                            self._track_result_body(order), user))

    def _track_result_body(self, order):
        """查单结果（只读）：与登录态订单详情页同款展示——状态大圈、
        交付内容、使用说明；没有任何操作按钮。店主备注是内部
        备注，不在此展示。"""
        status = order["status"]
        product = order_product(order)
        ring_cls, ring_char, hero_title = ORDER_HEROES.get(
            status, (" grey", "?", STATUS_LABELS.get(status, status)))
        if cur_lang() != "zh":
            hero_title = T(f"hero.{status}")
        paid_line = (f"<br>{T('detail.paid_at')}{esc(order['paid_at'])}"
                     if order["paid_at"] else "")
        note_line = ""  # 店主备注仅卖家后台可见，客户页不渲染
        qq_line = ""
        if (product and product["id"] == "gemini-pro-24m"
                and status in ("unpaid", "paid")):
            qq_line = (f'<p class="hint">{T("orders.gemini_qq_pre")}'
                       f'<b>{SELLER_QQ}</b>'
                       f'{T("orders.gemini_qq_note")}</p>')
        delivery_html = ""
        if order["delivery"]:
            delivery_html = f"""
        <div class="card">
          <div class="sect">{T('detail.delivery')}</div>
          <p class="hint">{T('detail.delivery_keep')}</p>
          <div class="delivery big">
            <div class="dt">{T('detail.delivery_account')}</div>
            <pre>{esc(order['delivery'])}</pre>
          </div>
        </div>"""
        disp_name = order['product_name']
        if product:
            disp_name, _ = loc_product(product)
        tip_text = (ORDER_TIPS.get(status, "") if cur_lang() == "zh"
                    else T(f"tip.{status}"))
        body = f"""
        <div class="detail-wrap">
        <div class="card">
          <div class="hero">
            <div class="ring{ring_cls}">{ring_char}</div>
            <h1>{hero_title}</h1>
            <div class="ono">{T('detail.order_no')} {esc(order['order_no'])}</div>
          </div>
          <p>{T('detail.product')}{esc(disp_name)}<br>
          {T('detail.amount')}¥{order['amount_cents']/100:.2f}<br>
          {T('detail.created')}{esc(order['created_at'])}{paid_line}<br>
          {T('detail.status')}<span class="badge">{esc(SL(status))}</span>
          {note_line}</p>
          <p class="hint">{esc(tip_text)}</p>
          {qq_line}
        </div>
        {delivery_html}
        <div class="card guide"><div class="sect">{T('detail.usage')}</div>
        {order_usage_html(product)}</div>
        <div class="btnrow center">
          <a class="btn secondary" href="/track">{T('track.more')}</a>
          <a class="btn secondary" href="/">{T('nf.home')}</a></div>
        </div>"""
        return body

    def legal_page(self, kind):
        _, user = self.session()
        docs = {
            "privacy": ("隐私政策", f"""
        <h2>我们收集哪些信息</h2>
        <ul>
          <li><b>账号信息</b>：注册邮箱、登录密码（加盐哈希保存，
          我们看不到明文）。</li>
          <li><b>订单信息</b>：所购商品与金额，以及您下单时填写的
          充值邮箱、辅助邮箱、联系方式和交付内容。</li>
          <li><b>钱包与客服记录</b>：储值 / 消费流水、在线客服的
          聊天内容。</li>
          <li><b>安全记录</b>：为防盗号与防刷单，系统会记录登录
          失败次数等安全信息。</li>
        </ul>
        <h2>这些信息用来做什么</h2>
        <ul>
          <li>处理订单、完成交付、提供售后；</li>
          <li>保障账号与资金安全；</li>
          <li>不出售、不出租您的个人信息，不用于广告画像。</li>
        </ul>
        <h2>我们绝不会做的事</h2>
        <ul>
          <li>本站任何环节<b>不会向您索要 Google 账号或其他第三
          方账号的密码</b>，请勿向任何人提供。</li>
          <li>付款通过第三方支付平台完成，本站不接触、不保存您的
          银行卡信息与支付密码。</li>
        </ul>
        <h2>保存与删除</h2>
        <p>订单记录会为售后与对账保留一段时间。如需删除账号及
        个人信息，请通过在线客服或店主 QQ {SELLER_QQ} 联系，
        核验身份后处理。</p>"""),
            "terms": ("用户条款", f"""
        <h2>服务性质</h2>
        <p>本站销售数字商品（会员代充服务与成品账号），由店主
        人工交付，无实物发货。</p>
        <h2>下单与付款</h2>
        <ul>
          <li>商品价格、库存与质保以商品页展示为准。</li>
          <li>付款是否成功以订单状态为准；如遇支付系统确认延迟，
          凭付款凭证联系店主人工核对处理，不会让您重复付款。</li>
          <li>下单时请确保充值邮箱、联系方式等信息准确；因买家
          填写错误造成的损失由买家承担，发现填错请第一时间
          联系店主。</li>
        </ul>
        <h2>质保与退款</h2>
        <ul>
          <li>未交付的订单可随时联系店主全额退款。</li>
          <li>各商品质保范围与时限见商品卡徽章和
          <a href="/guide">《使用教程》售后规则</a>，以那里为准。</li>
          <li>已交付且超出质保范围的，不支持退款。</li>
        </ul>
        <h2>买家须知</h2>
        <ul>
          <li>成品号收到后请在质保期内尽快登录验证；</li>
          <li>买家自行改密、转借或违规使用（含违反目标平台规则）
          导致的封禁、失效不在质保范围。</li>
        </ul>
        <h2>条款变更</h2>
        <p>本条款更新后在本页公布，继续使用本站即视为接受。
        有疑问请通过在线客服或店主 QQ {SELLER_QQ} 联系。</p>"""),
            "cookies": ("Cookie 政策", """
        <h2>本站使用哪些 Cookie</h2>
        <ul>
          <li><b>登录会话 Cookie（必需）</b>：您登录后用来保持
          登录状态，并做表单安全校验；退出登录或过期后失效。</li>
          <li>首页公告的「已关闭」偏好保存在您浏览器本地
          （localStorage），不会上传服务器。</li>
        </ul>
        <h2>我们不做的事</h2>
        <ul>
          <li>不使用广告 Cookie，不做跨站追踪；</li>
          <li>不接入第三方统计或用户画像服务。</li>
        </ul>
        <h2>第三方页面</h2>
        <p>付款时会跳转到支付宝等第三方支付页面，那些页面使用
        的 Cookie 由第三方自己的政策管理，与本站无关。</p>
        <h2>您的选择</h2>
        <p>您可以在浏览器里清除或禁用 Cookie，但禁用后将无法
        保持登录状态，也就无法下单和查看订单。</p>"""),
        }
        title, inner = docs[kind]
        if cur_lang() != "zh":
            lblob = i18n.blob(cur_lang(), f"legal_{kind}")
            if lblob:
                title = T(f"legal.{kind}_title")
                inner = lblob
        body = f"""<div class="card guide"><h1>{title}</h1>
        <p class="hint">{T('legal.updated')}</p>{inner}
        <p class="hint">{T('legal.contact_pre')}<a href="/support">{T('nav.support')}</a>{T('legal.contact_post', qq=SELLER_QQ)}</p></div>"""
        self.send_html(page(title, body, user))

    def privacy_page(self, query):
        self.legal_page("privacy")

    def terms_page(self, query):
        self.legal_page("terms")

    def cookies_page(self, query):
        self.legal_page("cookies")

    def forgot_page(self, query):
        _, user = self.session()
        body = f"""<div class="card">
          <h1>{T('forgot.title')}</h1>
          <p>{T('forgot.p1')}</p>
          <ol>
            <li>{T('forgot.li1', qq=SELLER_QQ)}</li>
            <li>{T('forgot.li2')}</li>
            <li>{T('forgot.li3_pre')}
            <a href="/login">{T('auth.login')}</a>{T('forgot.li3_post')}</li>
          </ol>
          <p class="hint">{T('forgot.hint')}</p>
          <div class="btnrow"><a class="btn grad" href="/login">{T('forgot.back')}</a>
          <a class="btn secondary" href="/support">{T('nav.support')}</a></div>
        </div>"""
        self.send_html(page(T("forgot.title"), body, user))

    # ---------- 支付 ----------
    def pay_page(self, order_no, err="", ok=""):
        session, user = self.require_login()
        if user is None:
            return
        order = self.get_order(order_no)
        if order is None or order["user_id"] != user["id"]:
            return self.send_html(
                page(T("detail.not_found"),
                     f"<h1>{T('detail.not_found')}</h1>", user), 404)
        if order["status"] != "unpaid":
            return self.redirect(f"/orders/{order_no}")
        epay_ok, epay_reason = payments.configured("epay")
        warnings = ""
        if not epay_ok:
            warnings += (f'<p class="hint">易支付-支付宝：支付参数未配置'
                         f'（{esc(epay_reason)}）</p>')
        product = order_product(order)
        qq = (qq_box() if product and product["id"] == "gemini-pro-24m"
              else "")
        balance = user["balance_cents"]
        if balance >= order["amount_cents"]:
            balance_html = f"""
        <form method="post" action="/pay/{esc(order_no)}/balance"
              style="display:inline">{csrf_field(session)}
          <button class="btn grad" type="submit">
            {T('pay.balance_btn', b=f'{balance/100:.2f}')}</button>
        </form>"""
        elif balance > 0:
            balance_html = (
                f'<p class="hint">{T("pay.balance_low_pre", b=f"{balance/100:.2f}")}'
                f'<a href="/wallet">{T("pay.goto_recharge")}</a>'
                f'{T("pay.balance_low_post")}</p>')
        else:
            balance_html = (
                f'<p class="hint">{T("pay.balance_zero_pre")}'
                f'<a href="/wallet">{T("pay.recharge_word")}</a>'
                f'{T("pay.balance_zero_post")}</p>')
        disp_name = order['product_name']
        if product:
            disp_name, _ = loc_product(product)
        body = f"""
        <div class="card"><h1>{T('pay.title')}</h1>
        <p>{T('pay.order_no')}{esc(order['order_no'])}<br>
        {T('pay.product')}{esc(disp_name)}<br>
        {T('pay.amount')}<b>¥{order['amount_cents']/100:.2f}</b></p>
        {warnings}
        {qq}
        {balance_html}
        <form method="post" action="/pay/{esc(order_no)}/epay-alipay"
              style="display:inline">{csrf_field(session)}
          <button class="btn" type="submit">{T('pay.epay_btn')}</button>
        </form>
        <p class="hint">{T('pay.note')}</p>
        </div>{copy_script() if qq else ''}"""
        self.send_html(page(T("pay.title"), body, user,
                            flash_err=err, flash_ok=ok))

    def _pay_order_or_404(self, order_no, form):
        session, user = self.require_login()
        if user is None:
            return None, None, None
        if not self.check_csrf(session, form):
            self.pay_page(order_no, err=T("order.err_expired"))
            return None, None, None
        order = self.get_order(order_no)
        if order is None or order["user_id"] != user["id"] \
                or order["status"] != "unpaid":
            self.send_html(page(T("detail.not_found"),
                                f"<h1>{T('detail.not_found')}</h1>",
                                user), 404)
            return None, None, None
        return session, user, order

    def pay_alipay(self, order_no, form):
        _, _, order = self._pay_order_or_404(order_no, form)
        if order is None:
            return
        try:
            url = payments.alipay_create_payment(
                order["order_no"], order["amount_cents"],
                order["product_name"])
        except payments.PaymentNotConfigured as e:
            return self.pay_page(
                order_no, err=f"支付参数未配置，暂时无法支付。{e}")
        except payments.PaymentError as e:
            return self.pay_page(order_no, err=f"支付发起失败：{e}")
        conn = db()
        conn.execute(
            "UPDATE orders SET pay_method='alipay', updated_at=?"
            " WHERE order_no=?", (now_text(), order_no))
        conn.commit()
        conn.close()
        self.redirect(url)

    def pay_wechat(self, order_no, form):
        session, _, order = self._pay_order_or_404(order_no, form)
        if order is None:
            return
        try:
            code_url = payments.wechat_create_native(
                order["order_no"], order["amount_cents"],
                order["product_name"])
        except payments.PaymentNotConfigured as e:
            return self.pay_page(
                order_no, err=f"支付参数未配置，暂时无法支付。{e}")
        except payments.PaymentError as e:
            return self.pay_page(order_no, err=f"支付发起失败：{e}")
        conn = db()
        conn.execute(
            "UPDATE orders SET pay_method='wechat', updated_at=?"
            " WHERE order_no=?", (now_text(), order_no))
        conn.commit()
        conn.close()
        try:
            qr_svg = qrcode_gen.to_svg(code_url, scale=5)
        except ValueError as e:
            return self.pay_page(order_no, err=f"二维码生成失败：{e}")
        body = f"""
        <div class="card qr"><h1>微信扫码支付</h1>
        <p>订单号：{esc(order_no)} · 应付
        <b>¥{order['amount_cents']/100:.2f}</b></p>
        {qr_svg}
        <p class="hint">请使用微信扫描上方二维码完成支付。<br>
        支付成功后，回到 <a href="/my-orders">我的订单</a> 查看状态。</p>
        </div>"""
        _, user = self.session()
        self.send_html(page("微信扫码支付", body, user))

    def pay_epay(self, order_no, form, pay_type):
        _, _, order = self._pay_order_or_404(order_no, form)
        if order is None:
            return
        try:
            url = payments.epay_create_payment(
                order["order_no"], order["amount_cents"],
                order["product_name"], pay_type)
        except payments.PaymentNotConfigured as e:
            return self.pay_page(
                order_no, err=f"支付参数未配置，暂时无法支付。{e}")
        except payments.PaymentError as e:
            return self.pay_page(order_no, err=f"支付发起失败：{e}")
        conn = db()
        conn.execute(
            "UPDATE orders SET pay_method=?, updated_at=?"
            " WHERE order_no=?",
            (f"epay_{pay_type}", now_text(), order_no))
        conn.commit()
        conn.close()
        self.redirect(url)

    def pay_balance(self, order_no, form):
        _, user, order = self._pay_order_or_404(order_no, form)
        if order is None:
            return
        conn = db()
        try:
            apply_balance_change(conn, user["id"], -order["amount_cents"],
                                 "pay", order_no, order["product_name"])
        except ValueError:
            conn.close()
            return self.pay_page(
                order_no, err="余额不足，请先储值或改用支付宝支付。")
        ts = now_text()
        conn.execute(
            "UPDATE orders SET status='paid', pay_method='balance',"
            " paid_at=?, updated_at=? WHERE order_no=?",
            (ts, ts, order_no))
        _deduct_stock(conn, order["product_id"])
        conn.commit()
        conn.close()
        try:
            refresh_user_level(user["id"])
        except Exception:
            pass  # 等级刷新失败不能影响支付主流程
        notify.push_async(
            "💰 新订单已支付（余额）",
            f"{order['product_name']}\n订单号：{order_no}\n"
            f"金额：¥{order['amount_cents'] / 100:.2f}\n"
            "请尽快在卖家后台处理。")
        self.redirect(f"/orders/{order_no}")

    # ---------- 支付回调 ----------
    def mark_paid(self, order_no, pay_method, trade_no):
        return mark_order_paid(order_no, pay_method, trade_no)

    def notify_alipay(self, form):
        from payments import alipay_verify_notify, PaymentError, \
            PaymentNotConfigured
        try:
            params = alipay_verify_notify(form)
        except (PaymentError, PaymentNotConfigured) as e:
            print(f"[notify-alipay] 拒绝：{e}")
            return self.send_text("failure")
        order = self.get_order(params.get("out_trade_no", ""))
        if order is None:
            return self.send_text("failure")
        if not payments.amount_equal(params.get("total_amount"),
                                      order["amount_cents"]):
            print("[notify-alipay] 拒绝：金额不匹配")
            return self.send_text("failure")
        if params.get("trade_status") in ("TRADE_SUCCESS", "TRADE_FINISHED"):
            self.mark_paid(order["order_no"], "alipay",
                           params.get("trade_no", ""))
        self.send_text("success")

    def notify_wechat(self, raw):
        from payments import wechat_verify_and_decrypt_notify, \
            PaymentError, PaymentNotConfigured
        headers = {k.lower(): v for k, v in self.headers.items()}
        try:
            trade = wechat_verify_and_decrypt_notify(headers, raw)
        except (PaymentError, PaymentNotConfigured) as e:
            print(f"[notify-wechat] 拒绝：{e}")
            return self.send_text(
                '{"code":"FAIL","message":"验签或解密失败"}',
                status=401, content_type="application/json")
        order = self.get_order(trade.get("out_trade_no", ""))
        if order is None or \
                trade.get("amount", {}).get("total") != order["amount_cents"]:
            return self.send_text(
                '{"code":"FAIL","message":"订单或金额不匹配"}',
                status=400, content_type="application/json")
        if trade.get("trade_state") == "SUCCESS":
            self.mark_paid(order["order_no"], "wechat",
                           trade.get("transaction_id", ""))
        self.send_text('{"code":"SUCCESS","message":"成功"}',
                       content_type="application/json")

    def notify_epay(self, params):
        """易支付异步通知（GET 为主，兼容 POST）：验签 + 状态 + 金额
        全部通过后才改单；成功只回纯文本 success，其他一律 fail。"""
        from payments import epay_verify_notify, PaymentError, \
            PaymentNotConfigured
        try:
            params = epay_verify_notify(params)
        except (PaymentError, PaymentNotConfigured) as e:
            print(f"[notify-epay] 拒绝：{e}")
            return self.send_text("fail")
        order = self.get_order(params.get("out_trade_no", ""))
        if order is None:
            recharge = get_recharge(params.get("out_trade_no", ""))
            if recharge is None:
                print("[notify-epay] 拒绝：订单不存在")
                return self.send_text("fail")
            if params.get("trade_status") != "TRADE_SUCCESS":
                return self.send_text("fail")
            if not payments.amount_equal(params.get("money"),
                                          recharge["amount_cents"]):
                print("[notify-epay] 拒绝：储值金额不匹配")
                return self.send_text("fail")
            mark_recharge_paid(recharge["recharge_no"],
                               params.get("trade_no", ""))
            return self.send_text("success")
        if params.get("trade_status") != "TRADE_SUCCESS":
            print("[notify-epay] 拒绝：trade_status 不是 TRADE_SUCCESS")
            return self.send_text("fail")
        # 网关 money 格式不固定（实测会发 "5" 而非 "5.00"），按数值比
        if not payments.amount_equal(params.get("money"),
                                      order["amount_cents"]):
            print("[notify-epay] 拒绝：金额不匹配")
            return self.send_text("fail")
        pay_type = params.get("type", "")
        method = f"epay_{pay_type}" if pay_type in ("alipay", "wxpay") \
            else "epay"
        self.mark_paid(order["order_no"], method,
                       params.get("trade_no", ""))
        self.send_text("success")

    def pay_return_epay(self, query):
        """易支付同步返回页：只展示订单状态，绝不凭此页改单状态
        （是否已支付只认异步通知验签结果）。"""
        _, user = self.session()
        order_no = query.get("out_trade_no", "")
        order = self.get_order(order_no) if order_no else None
        if order is None and order_no:
            recharge = get_recharge(order_no)
            if user is not None and recharge is not None \
                    and recharge["user_id"] == user["id"]:
                rlabel = (T("rpay.credited")
                          if recharge["status"] == "paid"
                          else T("rpay.confirming"))
                rtip = (T("rpay.tip_credited")
                        if recharge["status"] == "paid" else
                        T("rpay.tip_confirming"))
                rbody = f"""
        <div class="card"><h1>{T('rpay.result_title')}</h1>
        <p>{T('rpay.no')}{esc(recharge['recharge_no'])}<br>
        {T('rpay.amount')}¥{recharge['amount_cents']/100:.2f}<br>
        {T('pay.status_now')}<span class="badge">{rlabel}</span></p>
        <p class="hint">{rtip}</p>
        <div class="btnrow">
        <a class="btn" href="/wallet">{T('wallet.title')}</a>
        <a class="btn secondary" href="/">{T('detail.continue')}</a>
        </div></div>"""
                return self.send_html(page(T("rpay.result_title"),
                                           rbody, user))
        if user is None or order is None \
                or order["user_id"] != user["id"]:
            return self.redirect("/my-orders")
        label = SL(order["status"])
        if order["status"] == "paid":
            tip = T("pay.tip_paid")
        elif order["status"] == "unpaid":
            tip = T("pay.tip_unpaid")
        else:
            tip = T("pay.tip_other")
        disp_name = order['product_name']
        _prod = order_product(order)
        if _prod:
            disp_name, _ = loc_product(_prod)
        body = f"""
        <div class="card"><h1>{T('pay.status_title')}</h1>
        <p>{T('pay.order_no')}{esc(order['order_no'])}<br>
        {T('pay.product')}{esc(disp_name)}<br>
        {T('pay.status_amount')}¥{order['amount_cents']/100:.2f}<br>
        {T('pay.status_now')}<span class="badge">{esc(label)}</span></p>
        <p class="hint">{esc(tip)}</p>
        <div class="btnrow">
        <a class="btn" href="/orders/{esc(order['order_no'])}">{T('pay.view_detail')}</a>
        <a class="btn secondary" href="/my-orders">{T('orders.title')}</a>
        </div></div>"""
        self.send_html(page(T("pay.status_title"), body, user))

    # ---------- 储值钱包 ----------
    def wallet_page(self, query, err=""):
        session, user = self.require_login()
        if user is None:
            return
        conn = db()
        recharges = conn.execute(
            "SELECT * FROM recharges WHERE user_id=? ORDER BY id DESC"
            " LIMIT 20", (user["id"],)).fetchall()
        logs = conn.execute(
            "SELECT * FROM balance_logs WHERE user_id=? ORDER BY id DESC"
            " LIMIT 30", (user["id"],)).fetchall()
        first_bonus_eligible = not has_paid_recharge(conn, user["id"])
        conn.close()
        chips = "".join(
            '<label><input type="radio" name="preset" value="%d"%s>'
            '<span>¥%d</span></label>'
            % (v, " checked" if v == 50 else "", v)
            for v in (10, 15, 20, 50, 100, 200, 500))
        rc_rows = ""
        for r in recharges:
            if r["status"] == "paid":
                st = ('<span class="badge st-paid">'
                      + T("wallet.paid_badge") + '</span>')
            else:
                st = ('<a href="/wallet/pay/' + esc(r["recharge_no"])
                      + '">' + T("wallet.unpaid_link") + '</a>')
            amt = '¥%.2f' % (r["amount_cents"] / 100)
            rbonus = (r["bonus_cents"]
                      if "bonus_cents" in r.keys() else 0)
            if rbonus:
                amt += ('<br><span class="hint">'
                        + T("wallet.bonus_incl",
                            b="%.2f" % (rbonus / 100),
                            t="%.2f" % ((r["amount_cents"] + rbonus)
                                        / 100))
                        + '</span>')
            rc_rows += ('<tr><td>' + esc(r["recharge_no"]) + '</td>'
                        + '<td>' + amt + '</td>'
                        + '<td>' + st + '</td><td>'
                        + esc(r["created_at"]) + '</td></tr>')
        if not rc_rows:
            rc_rows = ('<tr><td colspan="4" class="hint">'
               + T("wallet.no_recharges") + '</td></tr>')
        log_rows = ""
        for lg in logs:
            delta = lg["change_cents"]
            sign = "+" if delta >= 0 else "-"
            log_rows += (
                '<tr><td>' + esc(lg["created_at"]) + '</td>'
                + '<td>' + esc(
                    T("kind." + lg["kind"]) if cur_lang() != "zh"
                    else BALANCE_KIND_LABELS.get(
                        lg["kind"], lg["kind"])) + '</td>'
                + '<td>' + sign + '¥%.2f</td>' % (abs(delta) / 100)
                + '<td>¥%.2f</td>' % (lg["balance_after"] / 100)
                + '<td>' + esc(lg["note"] or lg["ref_no"]) + '</td></tr>')
        if not log_rows:
            log_rows = ('<tr><td colspan="5" class="hint">'
                + T("wallet.no_logs") + '</td></tr>')
        bonus_banner = ""
        if first_bonus_eligible:
            bonus_banner = (
                '<p class="hint" style="font-size:15px;color:#6D28D9">'
                + T("wallet.bonus_banner") + '</p>')
        try:
            refresh_user_level(user["id"])
        except Exception:
            pass
        conn = db()
        fresh = conn.execute("SELECT * FROM users WHERE id=?",
                             (user["id"],)).fetchone()
        conn.close()
        lvl = (user_level(fresh) if fresh is not None
               else user_level(user))
        manual = False
        if fresh is not None:
            try:
                manual = fresh["level_manual"] is not None
            except Exception:
                manual = False
        spend, recharge = user_totals(user["id"])
        lv_rows = ""
        for i, lv in enumerate(LEVELS):
            if i == lvl:
                state, cls = T("wallet.lv_current"), "lvrow on"
            elif i == lvl + 1:
                state, cls = T("wallet.lv_next"), "lvrow"
            else:
                state, cls = T("wallet.lv_member"), "lvrow"
            lname_i, llabel_i = loc_level(i)
            disc = (T("wallet.lv_disc_all", label=llabel_i)
                    if llabel_i else T("wallet.lv_disc_default"))
            req = ""
            if i > 0:
                req = T("wallet.lv_req",
                        s=f'{lv["spend_cents"]/100:,.2f}',
                        r=f'{lv["recharge_cents"]/100:,.2f}')
            lv_rows += (
                f'<div class="{cls}"><span class="no">{i+1:02d}</span>'
                f'<span class="nm">{esc(lname_i)}<br>'
                f'<span class="hint">{state}</span></span>'
                f'<span class="dc">{disc}</span>'
                f'<span class="rq">{req}</span></div>')
        if manual:
            progress = (
                '<p class="hint">'
                + T("wallet.lv_manual", s=f"{spend/100:.2f}",
                    r=f"{recharge/100:.2f}")
                + '</p>')
        elif lvl < len(LEVELS) - 1:
            nxt = LEVELS[lvl + 1]
            progress = (
                '<p class="hint">'
                + T("wallet.lv_progress", s=f"{spend/100:.2f}",
                    r=f"{recharge/100:.2f}",
                    name=loc_level(lvl + 1)[0],
                    ds=f"{max(0, nxt['spend_cents']-spend)/100:.2f}",
                    dr=f"{max(0, nxt['recharge_cents']-recharge)/100:.2f}")
                + '</p>')
        else:
            progress = (
                '<p class="hint">'
                + T("wallet.lv_max", s=f"{spend/100:.2f}",
                    r=f"{recharge/100:.2f}")
                + '</p>')
        member_card = f"""
        <div class="card"><h1>{T('wallet.member_title')}</h1>
        <p>{T('wallet.member_now', name=esc(loc_level(lvl)[0]), n=len(LEVELS))}</p>
        {lv_rows}{progress}</div>"""
        body = f"""
        <div class="card"><h1>{T('wallet.title')}</h1>
        <p>{T('wallet.balance_label')}</p>
        <p class="wallet-bal">¥{user['balance_cents']/100:.2f}</p>
        {bonus_banner}
        <form method="post" action="/wallet/recharge">
        {csrf_field(session)}
        <div class="chips">{chips}</div>
        <label>{T('wallet.custom_label')}
        <input name="amount" inputmode="decimal" placeholder="{T('wallet.custom_ph')}"></label>
        <p><button class="btn" type="submit">{T('wallet.recharge_btn')}</button></p>
        <p class="hint">{T('wallet.note')}</p>
        </form></div>{member_card}
        <div class="card"><h1>{T('wallet.records')}</h1>
        <table><tr><th>{T('wallet.rc_no')}</th><th>{T('wallet.amount')}</th><th>{T('wallet.status')}</th><th>{T('wallet.time')}</th></tr>
        {rc_rows}</table></div>
        <div class="card"><h1>{T('wallet.logs')}</h1>
        <table><tr><th>{T('wallet.time')}</th><th>{T('wallet.type')}</th><th>{T('wallet.change')}</th><th>{T('wallet.balance')}</th><th>{T('wallet.note_col')}</th></tr>
        {log_rows}</table></div>"""
        self.send_html(page(T("wallet.title"), body, user,
                            flash_err=err))

    def create_recharge(self, form):
        session, user = self.require_login()
        if user is None:
            return
        if not self.check_csrf(session, form):
            return self.wallet_page({}, err=T("wallet.err_expired"))
        cents = None
        raw = (form.get("amount") or "").strip()
        if raw:
            try:
                cents = int(round(float(raw) * 100))
            except ValueError:
                cents = None
        else:
            try:
                cents = int(form.get("preset", "50")) * 100
            except (TypeError, ValueError):
                cents = None
        if cents is None or cents < 100 or cents > 500000:
            return self.wallet_page(
                {}, err=T("wallet.err_amount"))
        conn = db()
        no = make_recharge_no(conn)
        conn.execute(
            "INSERT INTO recharges (recharge_no, user_id, amount_cents,"
            " created_at) VALUES (?,?,?,?)",
            (no, user["id"], cents, now_text()))
        conn.commit()
        conn.close()
        self.redirect(f"/wallet/pay/{no}")

    def wallet_pay_page(self, recharge_no, err="", ok=""):
        session, user = self.require_login()
        if user is None:
            return
        r = get_recharge(recharge_no)
        if r is None or r["user_id"] != user["id"]:
            return self.send_html(
                page(T("rpay.not_found"),
                     f"<h1>{T('rpay.not_found')}</h1>", user), 404)
        if r["status"] != "unpaid":
            return self.redirect("/wallet")
        epay_ok, epay_reason = payments.configured("epay")
        warnings = ""
        if not epay_ok:
            warnings = (f'<p class="hint">支付参数未配置'
                        f'（{esc(epay_reason)}）</p>')
        conn = db()
        exp_bonus = first_recharge_bonus_cents(
            conn, user["id"], r["amount_cents"])
        conn.close()
        bonus_hint = ""
        if exp_bonus > 0:
            bonus_hint = (
                '<p class="hint" style="font-size:15px;color:#6D28D9">'
                + T("rpay.bonus_hint", b=f"{exp_bonus/100:.2f}",
                    t=f"{(r['amount_cents'] + exp_bonus)/100:.2f}")
                + '</p>')
        body = f"""
        <div class="card"><h1>{T('rpay.title')}</h1>
        <p>{T('rpay.no')}{esc(r['recharge_no'])}<br>
        {T('rpay.amount')}<b>¥{r['amount_cents']/100:.2f}</b></p>
        {bonus_hint}
        {warnings}
        <form method="post"
              action="/wallet/pay/{esc(recharge_no)}/epay-alipay"
              style="display:inline">{csrf_field(session)}
          <button class="btn" type="submit">{T('pay.epay_btn')}</button>
        </form>
        <p class="hint">{T('rpay.note')}</p>
        </div>"""
        self.send_html(page(T("rpay.title"), body, user,
                            flash_err=err, flash_ok=ok))

    def wallet_pay_epay(self, recharge_no, form):
        session, user = self.require_login()
        if user is None:
            return
        if not self.check_csrf(session, form):
            return self.wallet_pay_page(recharge_no,
                                        err=T("wallet.err_expired"))
        r = get_recharge(recharge_no)
        if r is None or r["user_id"] != user["id"]:
            return self.send_html(
                page("储值单不存在", "<h1>储值单不存在</h1>", user), 404)
        if r["status"] != "unpaid":
            return self.redirect("/wallet")
        try:
            url = payments.epay_create_payment(
                r["recharge_no"], r["amount_cents"], "账户储值", "alipay")
        except payments.PaymentNotConfigured as e:
            return self.wallet_pay_page(
                recharge_no, err=f"支付参数未配置，暂时无法支付。{e}")
        except payments.PaymentError as e:
            return self.wallet_pay_page(recharge_no,
                                        err=f"支付发起失败：{e}")
        conn = db()
        conn.execute(
            "UPDATE recharges SET pay_method='epay_alipay'"
            " WHERE recharge_no=?", (recharge_no,))
        conn.commit()
        conn.close()
        self.redirect(url)

    # ---------- 在线客服（客户侧） ----------
    def support_page(self, query, err=""):
        session, user = self.require_login()
        if user is None:
            return
        conn = db()
        msgs = conn.execute(
            "SELECT * FROM support_messages WHERE user_id=?"
            " ORDER BY id ASC LIMIT 200", (user["id"],)).fetchall()
        conn.execute(
            "UPDATE support_messages SET is_read=1"
            " WHERE user_id=? AND sender='admin'", (user["id"],))
        conn.commit()
        conn.close()
        bubbles, last_id = chat_bubbles(msgs, "user")
        body = f"""
        <div class="card"><h1>{T('support.title')}</h1>
        <p class="hint">{T('support.intro', qq=SELLER_QQ)}</p>
        <div class="chat" id="chatBox" data-last="{last_id}"
             data-poll="/support/poll">{bubbles}</div>
        <form class="chat-form" method="post" action="/support/send">
        {csrf_field(session)}
        <textarea name="body" rows="2" maxlength="2000" required
        placeholder="{T('support.ph')}"></textarea>
        <button class="btn" type="submit">{T('support.send')}</button>
        </form></div>{CHAT_POLL_JS}"""
        self.send_html(page(T("support.title"), body, user,
                            flash_err=err))

    def support_send(self, form):
        session, user = self.require_login()
        if user is None:
            return
        if not self.check_csrf(session, form):
            return self.support_page({}, err=T("support.err_expired"))
        text = (form.get("body") or "").strip()
        if text:
            conn = db()
            conn.execute(
                "INSERT INTO support_messages (user_id, sender, body,"
                " created_at) VALUES (?, 'user', ?, ?)",
                (user["id"], text[:2000], now_text()))
            conn.commit()
            conn.close()
            notify.push_async(
                "💬 新的客服留言",
                f"客户 {user['email']}：{text[:80]}")
        self.redirect("/support")

    def support_poll(self, query):
        _, user = self.session()
        if user is None:
            return self.send_text('{"messages": []}',
                                  content_type="application/json")
        try:
            after = int(query.get("after", "0"))
        except ValueError:
            after = 0
        conn = db()
        rows = conn.execute(
            "SELECT * FROM support_messages WHERE user_id=? AND id>?"
            " ORDER BY id ASC LIMIT 50", (user["id"], after)).fetchall()
        if any(r["sender"] == "admin" for r in rows):
            conn.execute(
                "UPDATE support_messages SET is_read=1 WHERE user_id=?"
                " AND sender='admin' AND id<=?",
                (user["id"], rows[-1]["id"]))
            conn.commit()
        conn.close()
        msgs = [{"id": r["id"], "body": r["body"],
                 "created_at": r["created_at"],
                 "mine": r["sender"] == "user",
                 "who": "我" if r["sender"] == "user" else "店主"}
                for r in rows]
        self.send_text(json.dumps({"messages": msgs}, ensure_ascii=False),
                       content_type="application/json")

    def support_unread(self, query):
        _, user = self.session()
        if user is None:
            return self.send_text('{"count": 0}',
                                  content_type="application/json")
        conn = db()
        n = conn.execute(
            "SELECT COUNT(*) AS c FROM support_messages"
            " WHERE user_id=? AND sender='admin' AND is_read=0",
            (user["id"],)).fetchone()["c"]
        conn.close()
        self.send_text(json.dumps({"count": n}),
                       content_type="application/json")

    # ---------- 卖家后台 ----------
    def admin_orders_page(self, query):
        _, user = self.require_login()
        if user is None:
            return
        if not user["is_admin"]:
            return self.redirect("/admin/login")
        status = query.get("status", "")
        conn = db()
        if status in STATUS_LABELS:
            rows = conn.execute(
                "SELECT o.*, u.email AS user_email FROM orders o"
                " JOIN users u ON u.id=o.user_id WHERE o.status=?"
                " ORDER BY o.id DESC", (status,)).fetchall()
        else:
            rows = conn.execute(
                "SELECT o.*, u.email AS user_email FROM orders o"
                " JOIN users u ON u.id=o.user_id ORDER BY o.id DESC"
            ).fetchall()
        conn.close()
        filter_links = '<a href="/admin">全部</a> ' + " ".join(
            f'<a href="/admin?status={k}">{v}</a>'
            for k, v in STATUS_LABELS.items())
        session, _ = self.session()
        items = ""
        for r in rows:
            # 删除入口对全部状态渲染；确认文案按是否碰过钱区分：
            # 已付款类状态额外写明删记录的真实后果（不退款 / 不
            # 回补库存 / 已售统计减少），防店主误以为删了能退钱。
            if r["status"] in ("unpaid", "cancelled"):
                confirm_text = (f"确定要删除订单 {r['order_no']} 吗？"
                                "删除后不可恢复。")
            else:
                confirm_text = (
                    f"确定要删除订单 {r['order_no']} 吗？"
                    "该订单已付款，删除只清除记录：不会退款、"
                    "不会回补库存、已售统计会相应减少。"
                    "删除后不可恢复。")
            del_form = f"""<form method="post"
              action="/admin/orders/{esc(r['order_no'])}/delete"
              onsubmit="return confirm('{esc(confirm_text)}')">
              {csrf_field(session)}
              <div class="delrow">
                <button class="btn danger xs" type="submit">删除订单</button>
              </div></form>"""
            cost_val = (r["cost_cents"]
                        if "cost_cents" in r.keys() else None)
            cost_input = (f"{cost_val/100:.2f}"
                          if cost_val is not None else "")
            if r["status"] in ("paid", "completed"):
                if cost_val is not None:
                    p = r["amount_cents"] - cost_val
                    pcolor = "#15803d" if p >= 0 else "#B3261E"
                    profit_html = (
                        f'<br><span style="color:{pcolor};'
                        f'font-weight:700">利润 ¥{p/100:.2f}</span>')
                else:
                    profit_html = ('<br><span class="hint">'
                                   '利润：待填成本</span>')
            else:
                profit_html = ""
            if r["status"] in ("unpaid", "cancelled"):
                confirm_btn = f"""<button class="btn xs" name="action"
                  value="confirm_paid" type="submit"
                  style="width:100%;margin-top:8px;background:#1a9e54"
                  onclick="return confirm('确认已在支付宝收到这笔 ¥{r['amount_cents']/100:.2f} 吗？确认后订单变为已支付/待充值，并扣库存、计已售。')">✔ 确认已收款（平台漏单时用）</button>"""
            else:
                confirm_btn = ""
            items += f"""<tr>
            <td>{esc(r['order_no'])}<br>
            <span class="hint">{esc(r['created_at'])}</span></td>
            <td>{esc(r['user_email'])}<br>
            {('充值：' + esc(r['google_email']) + '<br>') if r['google_email'] else ''}
            {('辅助：' + esc(r['aux_email']) + '<br>') if r['aux_email'] else ''}
            联系：{esc(r['contact'])}</td>
            <td><b>{esc(r['product_name'])}</b></td>
            <td>¥{r['amount_cents']/100:.2f}<br>
            <span class="badge">{esc(STATUS_LABELS[r['status']])}</span>{profit_html}</td>
            <td><form method="post"
              action="/admin/orders/{esc(r['order_no'])}/action">
              {csrf_field(session)}
              <input type="text" name="note" placeholder="店主备注（仅店主可见）"
                     value="{esc(r['admin_note'])}">
              <textarea name="delivery" rows="3"
                placeholder="交付内容：账号 / 密码（Muse 成品号在这里发货，客户在“我的订单”里查看）">{esc(r['delivery'])}</textarea>
              <input type="hidden" name="cost_seen" value="1">
              <input type="text" name="cost" inputmode="decimal"
                     placeholder="本单成本（元）— 填了自动算利润，清空 = 未填"
                     value="{cost_input}">
              {confirm_btn}
              <div class="actgrid">
                <button class="btn xs" name="action" value="complete"
                  type="submit">标记完成</button>
                <button class="btn secondary xs" name="action" value="note"
                  type="submit">只存备注</button>
                <button class="btn secondary xs" name="action" value="fail"
                  type="submit">标记失败</button>
                <button class="btn danger xs" name="action" value="refund"
                  type="submit">标记退款</button>
              </div></form>{del_form}</td></tr>"""
        stocks = get_all_stock()
        inv_rows = ""
        for p in catalog_products(include_inactive=True):
            st = stocks.get(p["id"], -1)
            cur = "不限量" if st < 0 else f"剩余 {st} 件"
            inv_rows += f"""<tr><td>{esc(p['name'])}</td>
            <td>{cur}</td>
            <td><input type="number" name="stock_{esc(p['id'])}"
              value="{'' if st < 0 else st}" min="-1"
              placeholder="留空 / 填 -1 = 不限量"></td></tr>"""
        inv_card = f"""<div class="card"><h2>商品库存</h2>
        <form class="inv-form" method="post" action="/admin/inventory">
        {csrf_field(session)}
        <table><tr><th>商品</th><th>当前</th><th>设为（件）</th></tr>
        {inv_rows}</table>
        <div class="btnrow"><button class="btn" type="submit">保存库存</button></div>
        <p class="hint">库存为 0 时商品自动显示“售罄”且无法下单；
        付款成功扣 1 件，订单退款 / 失败自动回补 1 件。
        Gemini 代充是服务类商品，一般保持“不限量”。</p></form></div>"""
        danger_card = """<div class="card" style="border:2px solid #e5484d">
        <h2 style="color:#e5484d">危险区</h2>
        <p>一键清空本站<b>全部订单</b>（含已支付 / 已完成等所有状态）。
        删除前系统会先自动备份一份数据库，但删除后订单不可恢复。
        此功能主要用于正式营业前清理测试订单，点下方按钮进入确认页。</p>
        <div class="btnrow"><a class="btn danger"
          href="/admin/orders/delete-all">删除全部订单</a></div></div>"""
        ps = profit_stats()
        margin = (ps["profit"] / ps["rev_filled"] * 100
                  if ps["rev_filled"] else 0.0)
        miss_hint = (
            f'<p class="hint">还有 {ps["missing"]} 单已付款订单没填'
            '成本，利润未计入，在订单行里填「本单成本」即可补上。</p>'
            if ps["missing"] else
            '<p class="hint">已付款订单的成本已全部填好。</p>')
        profit_card = f"""<div class="card"><h1>💰 利润汇总</h1>
        <p>已付款订单共 <b>{ps['orders']}</b> 单 · 总营业额
        <b>¥{ps['revenue']/100:.2f}</b></p>
        <p>已填成本 <b>{ps['filled']}</b> 单：营业额
        ¥{ps['rev_filled']/100:.2f} · 成本 ¥{ps['cost']/100:.2f} ·
        <b>利润 ¥{ps['profit']/100:.2f}</b>（利润率 {margin:.1f}%）</p>
        {miss_hint}</div>"""
        body = inv_card + profit_card + f"""<div class="card"><h1>卖家后台 · 订单处理</h1>
        {admin_tabs("orders")}
        <p>{filter_links}</p>
        <table><tr><th>订单</th><th>客户信息</th><th>商品</th>
        <th>金额/状态</th><th>处理</th></tr>{items}</table>
        <p class="hint">说明：标记完成/失败/退款只改变订单状态，
        退款请同时在支付宝/微信商户后台完成实际退款操作。
        删除对所有状态开放，但删除只是清除记录：不会退款、
        不会回补库存，已付款订单删除后已售统计会相应减少。</p></div>""" \
            + danger_card
        oks = {"deleted": "订单已删除。"}
        ok = oks.get(query.get("ok", ""), "")
        if query.get("ok") == "deletedall":
            try:
                n_del = int(query.get("n", "0"))
            except ValueError:
                n_del = 0
            bak_name = os.path.basename(query.get("bak", ""))
            ok = (f"已删除全部订单共 {n_del} 单。"
                  f"删除前备份：backups/{bak_name}，"
                  "如需恢复请用该备份文件。")
        errs = {"delnotfound": "订单不存在，可能已被删除。"}
        err = errs.get(query.get("err", ""), "")
        self.send_html(page("卖家后台", body, user,
                            flash_ok=ok, flash_err=err))

    def admin_action(self, order_no, form):
        session, user = self.require_login()
        if user is None:
            return
        if not user["is_admin"]:
            return self.redirect("/admin/login")
        if not self.check_csrf(session, form):
            return self.redirect("/admin")
        action = form.get("action", "")
        note = form.get("note", "").strip()
        delivery = form.get("delivery", "").strip()
        order = self.get_order(order_no)
        if order is None:
            return self.redirect("/admin")
        conn = db()
        ts = now_text()
        # 成本随处理表单一并保存：以隐藏字段 cost_seen 判断新版
        # 表单（parse_qs 会丢弃空值，单看 cost 字段分不清没提交
        # 还是清空）；填空 = 清除成本；合法非负数 = 设置；非法
        # 输入保留原值、不拦操作。
        if form.get("cost_seen"):
            raw = (form.get("cost") or "").strip()
            new_cost = (order["cost_cents"]
                        if "cost_cents" in order.keys() else None)
            if raw == "":
                new_cost = None
            else:
                try:
                    v = int(round(float(raw) * 100))
                    if v >= 0:
                        new_cost = v
                except (TypeError, ValueError):
                    pass
            conn.execute(
                "UPDATE orders SET cost_cents=? WHERE order_no=?",
                (new_cost, order_no))
        if action == "confirm_paid" and order["status"] in (
                "unpaid", "cancelled"):
            # 店主手动确认收款：平台账单通道偶发漏匹配（钱已到店主
            # 支付宝、平台却把订单超时作废），店主核对到账后点此
            # 按钮兜底。先存备注 / 交付，再走正规 mark_order_paid
            # 流程：状态转已支付、扣库存、已售与会员消费累计同步
            # 生效；不重复扣（mark_order_paid 幂等）。
            conn.execute("UPDATE orders SET admin_note=?, delivery=?,"
                         " updated_at=? WHERE order_no=?",
                         (note, delivery, ts, order_no))
            conn.commit()
            conn.close()
            mark_order_paid(order_no, order["pay_method"], "manual",
                            notify_seller=False)
            self.redirect("/admin")
            return
        if action == "note":
            conn.execute("UPDATE orders SET admin_note=?, delivery=?,"
                         " updated_at=? WHERE order_no=?",
                         (note, delivery, ts, order_no))
        elif action == "complete" and order["status"] == "paid":
            conn.execute(
                "UPDATE orders SET status='completed', admin_note=?,"
                " delivery=?, completed_at=?, updated_at=?"
                " WHERE order_no=?",
                (note, delivery, ts, ts, order_no))
        elif action == "fail" and order["status"] in ("unpaid", "paid"):
            conn.execute(
                "UPDATE orders SET status='failed', admin_note=?,"
                " delivery=?, updated_at=? WHERE order_no=?",
                (note, delivery, ts, order_no))
            if order["status"] == "paid":
                _restock(conn, order["product_id"])
            if order["status"] == "paid" \
                    and order["pay_method"] == "balance":
                apply_balance_change(conn, order["user_id"],
                                     order["amount_cents"], "refund",
                                     order_no, "订单失败，余额返还")
        elif action == "refund" and order["status"] == "paid":
            conn.execute(
                "UPDATE orders SET status='refunded', admin_note=?,"
                " delivery=?, updated_at=? WHERE order_no=?",
                (note, delivery, ts, order_no))
            _restock(conn, order["product_id"])
            if order["pay_method"] == "balance":
                apply_balance_change(conn, order["user_id"],
                                     order["amount_cents"], "refund",
                                     order_no, "订单退款，余额返还")
        conn.commit()
        conn.close()
        self.redirect("/admin")

    def admin_delete_order(self, order_no, form):
        """卖家删除订单：全部状态都可删（2026-11-07 店主确认放开
        upgrade6 时的 unpaid/cancelled 白名单），存在即可删，真删
        行。删除是纯记录删除：不退款、不返余额、不回补库存；已
        付款订单删后已售统计会相应减少（页面确认文案已写明）。
        管理员 + CSRF 校验保持不变。删除后若该订单号再收到支付
        回调 / 查单确认，mark_order_paid 查不到订单会安全忽略，
        不会复活订单。"""
        session, user = self.require_login()
        if user is None:
            return
        if not user["is_admin"]:
            return self.redirect("/admin/login")
        if not self.check_csrf(session, form):
            return self.redirect("/admin")
        order = self.get_order(order_no)
        if order is None:
            return self.redirect("/admin?err=delnotfound")
        conn = db()
        conn.execute("DELETE FROM orders WHERE order_no=?",
                     (order_no,))
        conn.commit()
        conn.close()
        self.redirect("/admin?ok=deleted")

    def admin_delete_all_page(self, query):
        """「删除全部订单」独立确认页：展示订单总数与各状态分布、
        删后后果，并要求店主逐字输入确认短语才允许提交（页面 JS
        控制按钮禁用只是体验层，真正的短语校验在 POST 处理里）。"""
        _, user = self.require_login()
        if user is None:
            return
        if not user["is_admin"]:
            return self.redirect("/admin/login")
        conn = db()
        counts = {k: 0 for k in STATUS_LABELS}
        for r in conn.execute(
                "SELECT status, COUNT(*) AS c FROM orders"
                " GROUP BY status"):
            if r["status"] in counts:
                counts[r["status"]] = r["c"]
        conn.close()
        total = sum(counts.values())
        breakdown = " · ".join(
            f"{STATUS_LABELS[k]} {counts[k]} 单" for k in STATUS_LABELS)
        base_total = sum(p.get("sold_base", 0) or 0 for p in PRODUCTS)
        session, _ = self.session()
        body = f"""<div class="card" style="border:2px solid #e5484d">
        <h1 style="color:#e5484d">删除全部订单</h1>
        <p>当前共有 <b>{total}</b> 单订单：{esc(breakdown)}。</p>
        <p><b>删除后会发生什么：</b></p>
        <ul>
          <li>全部订单被永久删除，<b>不可恢复</b>。系统会在删除前
          先把当前数据库自动备份到服务器的 backups/ 目录
          （文件名 pre-delete-all-日期时间.db），万一删错只能靠
          这份备份人工恢复。</li>
          <li>首页与商品页的「已售」将只剩开站前的历史基础销量
          （合计 {base_total} 单），平均交付时长也会因本站没有
          已完成订单而自动隐藏。</li>
          <li><b>库存不会自动回补</b>：已卖出 / 测试单占用的成品号
          库存视为已消耗，删除订单不会把库存加回去。</li>
          <li>用户账号、账户余额、储值记录、客服消息都
          <b>不受影响</b>，只删订单本身。</li>
        </ul>
        <form method="post" action="/admin/orders/delete-all">
          {csrf_field(session)}
          <p>确认无误后，请在下面输入框里<b>逐字输入
          「{DELETE_ALL_PHRASE}」</b>（六个字），按钮才会点亮：</p>
          <input type="text" name="confirm_phrase" id="delAllPhrase"
                 autocomplete="off"
                 placeholder="请输入：{DELETE_ALL_PHRASE}">
          <div class="btnrow">
            <button class="btn danger" type="submit" id="delAllBtn"
              disabled>确认删除全部订单</button>
            <a class="btn secondary" href="/admin">取消，返回订单列表</a>
          </div>
        </form>
        <script>
        (function(){{
          var inp = document.getElementById('delAllPhrase');
          var btn = document.getElementById('delAllBtn');
          inp.addEventListener('input', function(){{
            btn.disabled = (inp.value !== '{DELETE_ALL_PHRASE}');
          }});
        }})();
        </script></div>"""
        errs = {
            "phrase": "确认短语不正确：必须逐字输入"
                      f"「{DELETE_ALL_PHRASE}」六个字，"
                      "订单未做任何改动。",
            "backup": "删除前自动备份失败，已取消本次删除，"
                      "订单未做任何改动。请检查服务器磁盘空间与"
                      "backups 目录权限后重试。",
        }
        err = errs.get(query.get("err", ""), "")
        self.send_html(page("删除全部订单", body, user,
                            flash_err=err))

    def admin_delete_all(self, form):
        """一键删除全部订单：管理员 + CSRF + 逐字确认短语三重
        校验，任一不过即拒绝。执行顺序固定为「先备份、后删除」：
        先 snapshot_db_before_delete_all() 把当前库快照到
        backups/pre-delete-all-*.db，备份失败直接中止、订单一张
        不动；备份成功才 DELETE 全部订单行。只动 orders 表，
        用户 / 余额 / 储值 / 客服 / 库存都不受影响，库存不回补。"""
        session, user = self.require_login()
        if user is None:
            return
        if not user["is_admin"]:
            return self.redirect("/admin/login")
        if not self.check_csrf(session, form):
            return self.redirect("/admin")
        if form.get("confirm_phrase", "") != DELETE_ALL_PHRASE:
            return self.redirect("/admin/orders/delete-all?err=phrase")
        try:
            bak_name = snapshot_db_before_delete_all()
        except Exception:
            return self.redirect("/admin/orders/delete-all?err=backup")
        conn = db()
        cur = conn.execute("DELETE FROM orders")
        deleted = cur.rowcount
        conn.commit()
        conn.close()
        self.redirect("/admin?ok=deletedall&n=%d&bak=%s"
                      % (deleted, quote(bak_name)))

    def admin_inventory(self, form):
        session, user = self.require_login()
        if user is None:
            return
        if not user["is_admin"]:
            return self.redirect("/admin/login")
        if not self.check_csrf(session, form):
            return self.redirect("/admin")
        # 通用解析 stock_<pid> 字段：内置与后台新增商品都覆盖
        for key, raw0 in form.items():
            if not key.startswith("stock_"):
                continue
            pid = key[len("stock_"):]
            raw = (raw0 or "").strip()
            if raw == "":
                set_stock(pid, -1)
                continue
            try:
                value = int(raw)
            except ValueError:
                continue
            set_stock(pid, max(-1, value))
        self.redirect("/admin")

    # ---------- 商品管理 ----------
    def admin_products_page(self, query):
        session, user = self.require_login()
        if user is None:
            return
        if not user["is_admin"]:
            return self.redirect("/admin/login")
        products = catalog_products(include_inactive=True)
        stocks = get_all_stock()
        conn = db()
        order_counts = {r["product_id"]: r["c"] for r in conn.execute(
            "SELECT product_id, COUNT(*) AS c FROM orders"
            " GROUP BY product_id")}
        conn.close()
        banner = ""
        if query.get("saved"):
            banner = '<div class="ok">✓ 已保存，网站已实时生效。</div>'
        if query.get("err"):
            banner = ('<div class="err">'
                      + esc(query.get("err")) + '</div>')
        cards = ""
        for p in products:
            pid = p["id"]
            st = stocks.get(pid, -1)
            oc = order_counts.get(pid, 0)
            badge = ('<span class="tag">后台新增</span>'
                     if p.get("is_custom") else
                     '<span class="tag">系统内置</span>')
            if p.get("is_custom") and oc == 0:
                del_html = f"""<form method="post"
                  action="/admin/products/delete"
                  onsubmit="return confirm('确定删除这个商品？删除后不可恢复。')">
                  {csrf_field(session)}
                  <input type="hidden" name="pid" value="{esc(pid)}">
                  <button class="btn danger xs" type="submit">删除商品</button>
                  </form>"""
            elif p.get("is_custom"):
                del_html = ('<span class="hint">已有订单的商品不能删除，'
                            '可以取消勾选「上架」将它下架。</span>')
            else:
                del_html = ('<span class="hint">系统内置商品不能删除，'
                            '可以取消勾选「上架」将它下架。</span>')
            points_text = esc("\n".join(p.get("points") or []))
            cards += f"""<div class="card">
            <h2 style="margin-top:0">{esc(p['name'])} {badge}</h2>
            <p class="hint">编号 {esc(pid)} · 分类
            {esc(p.get('cat_label', ''))} · 历史订单 {oc} 单 ·
            当前状态：{'上架中' if p.get('active', True) else '已下架'}</p>
            <form method="post" action="/admin/products/save">
            {csrf_field(session)}
            <input type="hidden" name="pid" value="{esc(pid)}">
            <label>商品名</label>
            <input type="text" name="name" value="{esc(p['name'])}">
            <label>售价（元）</label>
            <input type="text" name="price_yuan" inputmode="decimal"
              value="{p['price_cents'] / 100:.2f}">
            <label>库存（件）— 留空或填 -1 = 不限量，0 = 售罄</label>
            <input type="number" name="stock" min="-1"
              value="{'' if st < 0 else st}"
              placeholder="留空 = 不限量">
            <label>基础已售（展示用，真实销量在此之上累加）</label>
            <input type="number" name="sold_base" min="0"
              value="{int(p.get('sold_base', 0) or 0)}">
            <label>排序（数字越小越靠前）</label>
            <input type="number" name="sort" value="{int(p['_sort'])}">
            <label style="display:block;margin:10px 0 4px">
            <input type="checkbox" name="active" value="1"
              {'checked' if p.get('active', True) else ''}
              style="width:auto"> 上架（取消勾选 = 下架，首页隐藏、
              不能下单，老订单不受影响）</label>
            <label style="display:block;margin:4px 0">
            <input type="checkbox" name="needs_email" value="1"
              {'checked' if p.get('needs_email') else ''}
              style="width:auto"> 代充型（下单需填账号邮箱 + 辅助邮箱；
              不勾 = 成品号型，只填联系方式）</label>
            <label>下单页第一个输入框的标签</label>
            <input type="text" name="first_label"
              value="{esc(p.get('first_label', ''))}">
            <label>价格后缀（如：一次付清）</label>
            <input type="text" name="price_suffix"
              value="{esc(p.get('price_suffix', ''))}">
            <label>价格备注（如：/ 份 · 一次付清）</label>
            <input type="text" name="price_note"
              value="{esc(p.get('price_note', ''))}">
            <label>商品说明（下单页介绍段）</label>
            <textarea name="desc" rows="2">{esc(p.get('desc', ''))}</textarea>
            <label>卖点列表（一行一条）</label>
            <textarea name="points" rows="5">{points_text}</textarea>
            <label>下单页底部提示</label>
            <input type="text" name="password_hint"
              value="{esc(p.get('password_hint', ''))}">
            <div class="btnrow"><button class="btn" type="submit">
            保存这个商品</button></div>
            </form>
            <div style="margin-top:10px">{del_html}</div>
            </div>"""
        cat_opts = ""
        seen_cats = {}
        for p in PRODUCTS:
            seen_cats.setdefault(p["cat"], p["cat_label"])
        for cat, lbl in seen_cats.items():
            cat_opts += (f'<option value="{esc(cat)}">'
                         f'{esc(lbl)}（{esc(cat)}）</option>')
        add_card = f"""<div class="card"><h2 style="margin-top:0">
        ➕ 新增商品</h2>
        <form method="post" action="/admin/products/add">
        {csrf_field(session)}
        <label>商品名 <b>*</b></label>
        <input type="text" name="name" required
          placeholder="如：Claude Pro 1个月代充">
        <label>售价（元）<b>*</b></label>
        <input type="text" name="price_yuan" inputmode="decimal"
          required placeholder="如：39.90">
        <label>分类（决定卡片图标与配色）</label>
        <select name="cat">{cat_opts}</select>
        <label>库存（件）— 留空 = 不限量</label>
        <input type="number" name="stock" min="-1"
          placeholder="留空 = 不限量">
        <label style="display:block;margin:10px 0 4px">
        <input type="checkbox" name="needs_email" value="1"
          style="width:auto"> 代充型（下单需填账号邮箱 + 辅助邮箱；
          不勾 = 成品号型）</label>
        <label>下单页第一个输入框的标签（可留空，按类型自动生成）</label>
        <input type="text" name="first_label"
          placeholder="如：要充值的账号邮箱 / 接收邮箱">
        <label>商品说明</label>
        <textarea name="desc" rows="2"></textarea>
        <label>卖点列表（一行一条）</label>
        <textarea name="points" rows="4"
          placeholder="一行一条，如：&#10;付款后人工发货&#10;支持支付宝付款"></textarea>
        <label>下单页底部提示（可留空，自动生成）</label>
        <input type="text" name="password_hint">
        <div class="btnrow"><button class="btn" type="submit">
        添加商品</button></div>
        </form></div>"""
        body = f"""{admin_tabs("products")}
        <div class="card"><h1>卖家后台 · 商品管理</h1>
        <p class="hint">在这里改价、改库存、改名、上下架、加新商品，
        保存后立即生效，不用再发升级包。注意：①改名 / 改卖点后，
        中文页面立即生效，外语页面仍显示原译文（仅系统内置商品）；
        ②新商品暂时只显示中文名（各语言通用）；③价格改动只影响
        新订单，已下单的按原价。</p></div>
        {banner}{cards}{add_card}"""
        self.send_html(page("商品管理", body, user))

    def _yuan_to_cents(self, raw):
        try:
            cents = int(round(float((raw or "").strip()) * 100))
        except (TypeError, ValueError):
            return None
        return cents if cents > 0 else None

    def _parse_stock(self, raw, keep):
        raw = (raw or "").strip()
        if raw == "":
            return -1
        try:
            return max(-1, int(raw))
        except ValueError:
            return keep

    def admin_product_save(self, form):
        session, user = self.require_login()
        if user is None:
            return
        if not user["is_admin"]:
            return self.redirect("/admin/login")
        if not self.check_csrf(session, form):
            return self.redirect("/admin/products")
        pid = (form.get("pid") or "").strip()
        product = catalog_by_id(include_inactive=True).get(pid)
        if product is None:
            return self.redirect("/admin/products")
        name = (form.get("name") or "").strip()
        cents = self._yuan_to_cents(form.get("price_yuan"))
        if not name or cents is None:
            return self.redirect(
                "/admin/products?err=" + quote("商品名不能为空、"
                                               "价格必须是大于 0 的数字"))
        try:
            sold_base = max(0, int(form.get("sold_base") or 0))
        except ValueError:
            sold_base = int(product.get("sold_base", 0) or 0)
        try:
            sort_val = int(form.get("sort") or product["_sort"])
        except ValueError:
            sort_val = int(product["_sort"])
        first_label = (form.get("first_label") or "").strip() \
            or product.get("first_label", "")
        is_custom = 1 if product.get("is_custom") else 0
        conn = db()
        existing = conn.execute(
            "SELECT cat, cat_label, tint FROM products_admin"
            " WHERE pid=?", (pid,)).fetchone()
        conn.execute(
            "INSERT INTO products_admin (pid, name, price_cents,"
            " sold_base, sort, active, is_custom, cat, cat_label, tint,"
            " desc, points, first_label, first_err, password_hint,"
            " needs_email, price_suffix, price_note, created_at)"
            " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
            " ON CONFLICT(pid) DO UPDATE SET name=excluded.name,"
            " price_cents=excluded.price_cents,"
            " sold_base=excluded.sold_base, sort=excluded.sort,"
            " active=excluded.active, desc=excluded.desc,"
            " points=excluded.points,"
            " first_label=excluded.first_label,"
            " first_err=excluded.first_err,"
            " password_hint=excluded.password_hint,"
            " needs_email=excluded.needs_email,"
            " price_suffix=excluded.price_suffix,"
            " price_note=excluded.price_note",
            (pid, name, cents, sold_base, sort_val,
             1 if form.get("active") else 0, is_custom,
             existing["cat"] if existing else product.get("cat", ""),
             existing["cat_label"] if existing
             else product.get("cat_label", ""),
             existing["tint"] if existing else product.get("tint", ""),
             (form.get("desc") or "").strip(),
             _points_to_text(_points_from_text(form.get("points"))),
             first_label, first_label + "格式不正确",
             (form.get("password_hint") or "").strip(),
             1 if form.get("needs_email") else 0,
             (form.get("price_suffix") or "").strip(),
             (form.get("price_note") or "").strip(),
             now_text()))
        conn.commit()
        conn.close()
        set_stock(pid, self._parse_stock(
            form.get("stock"), get_stock(pid)))
        self.redirect("/admin/products?saved=1")

    def admin_product_add(self, form):
        session, user = self.require_login()
        if user is None:
            return
        if not user["is_admin"]:
            return self.redirect("/admin/login")
        if not self.check_csrf(session, form):
            return self.redirect("/admin/products")
        name = (form.get("name") or "").strip()
        cents = self._yuan_to_cents(form.get("price_yuan"))
        if not name or cents is None:
            return self.redirect(
                "/admin/products?err=" + quote("商品名不能为空、"
                                               "价格必须是大于 0 的数字"))
        valid_cats = {p["cat"] for p in PRODUCTS}
        cat = (form.get("cat") or "").strip()
        if cat not in valid_cats:
            cat = "muse"
        _icon, tint, cat_label = _cat_defaults(cat)
        needs_email = 1 if form.get("needs_email") else 0
        first_label = (form.get("first_label") or "").strip() or (
            "要充值的账号邮箱" if needs_email else "接收邮箱")
        password_hint = (form.get("password_hint") or "").strip() or (
            "我们不会在任何环节向您索要账号密码。" if needs_email else
            "付款后店主会通过您填写的联系方式交付，"
            "请确保联系方式准确无误。")
        catalog = catalog_products(include_inactive=True)
        pid = "custom-" + time.strftime("%Y%m%d%H%M%S")
        suffix = 1
        base_pid = pid
        existing_ids = {p["id"] for p in catalog}
        while pid in existing_ids:
            suffix += 1
            pid = f"{base_pid}-{suffix}"
        sort_val = max([p["_sort"] for p in catalog] or [0]) + 10
        conn = db()
        conn.execute(
            "INSERT INTO products_admin (pid, name, price_cents,"
            " sold_base, sort, active, is_custom, cat, cat_label, tint,"
            " desc, points, first_label, first_err, password_hint,"
            " needs_email, price_suffix, price_note, created_at)"
            " VALUES (?,?,?,?,?,1,1,?,?,?,?,?,?,?,?,?,"
            " '一次付清', '/ 份 · 一次付清', ?)",
            (pid, name, cents, 0, sort_val, cat, cat_label, tint,
             (form.get("desc") or "").strip(),
             _points_to_text(_points_from_text(form.get("points"))),
             first_label, first_label + "格式不正确", password_hint,
             needs_email, now_text()))
        conn.commit()
        conn.close()
        set_stock(pid, self._parse_stock(form.get("stock"), -1))
        self.redirect("/admin/products?saved=1")

    def admin_product_delete(self, form):
        session, user = self.require_login()
        if user is None:
            return
        if not user["is_admin"]:
            return self.redirect("/admin/login")
        if not self.check_csrf(session, form):
            return self.redirect("/admin/products")
        pid = (form.get("pid") or "").strip()
        conn = db()
        row = conn.execute(
            "SELECT is_custom FROM products_admin WHERE pid=?",
            (pid,)).fetchone()
        orders = conn.execute(
            "SELECT COUNT(*) AS c FROM orders WHERE product_id=?",
            (pid,)).fetchone()["c"]
        if row is not None and row["is_custom"] and orders == 0:
            conn.execute("DELETE FROM products_admin WHERE pid=?",
                         (pid,))
            conn.execute("DELETE FROM inventory WHERE product_id=?",
                         (pid,))
            conn.commit()
            conn.close()
            return self.redirect("/admin/products?saved=1")
        conn.close()
        self.redirect("/admin/products?err=" + quote(
            "只能删除「后台新增」且没有任何订单的商品，"
            "其他商品请用下架处理"))

    def admin_wallet_page(self, query):
        session, user = self.require_login()
        if user is None:
            return
        if not user["is_admin"]:
            return self.redirect("/admin/login")
        conn = db()
        users = conn.execute(
            "SELECT email, balance_cents, created_at, level,"
            " level_manual FROM users"
            " ORDER BY balance_cents DESC, id ASC LIMIT 100").fetchall()
        logs = conn.execute(
            "SELECT b.*, u.email FROM balance_logs b"
            " JOIN users u ON u.id = b.user_id"
            " ORDER BY b.id DESC LIMIT 50").fetchall()
        conn.close()
        urows = "".join(
            '<tr><td>' + esc(u["email"]) + '</td>'
            + '<td>¥%.2f</td>' % (u["balance_cents"] / 100)
            + '<td>' + esc(LEVELS[user_level(u)]["name"])
            + ('（手动）' if u["level_manual"] is not None else '')
            + '</td>'
            + '<td>' + esc(u["created_at"]) + '</td></tr>' for u in users)
        lrows = ""
        for l in logs:
            delta = l["change_cents"]
            lrows += (
                '<tr><td>' + esc(l["created_at"]) + '</td>'
                + '<td>' + esc(l["email"]) + '</td>'
                + '<td>' + esc(BALANCE_KIND_LABELS.get(
                    l["kind"], l["kind"])) + '</td>'
                + '<td>' + ("+" if delta >= 0 else "-")
                + '¥%.2f</td>' % (abs(delta) / 100)
                + '<td>¥%.2f</td>' % (l["balance_after"] / 100)
                + '<td>' + esc(l["note"] or l["ref_no"]) + '</td></tr>')
        lv_options = "".join(
            f'<option value="{i}">{esc(lv["name"])}'
            + (f'（{esc(lv["label"])}）' if lv["label"] else "")
            + "</option>"
            for i, lv in enumerate(LEVELS))
        oks = {"1": "调账完成。",
               "pw": "密码已重置，该用户可用新密码登录。",
               "lvl": "会员等级已更新。"}
        ok = oks.get(query.get("ok", ""), "")
        errs = {"nouser": "找不到这个邮箱对应的用户。",
                "badamount": "金额不正确。",
                "insufficient": "扣款金额超过该用户当前余额。",
                "pwshort": "新密码至少 8 位。",
                "pwmismatch": "两次输入的新密码不一致。",
                "badlevel": "等级不正确。"}
        err = errs.get(query.get("err", ""), "")
        body = f"""<div class="card"><h1>卖家后台 · 储值管理</h1>
        {admin_tabs("wallet")}
        <form method="post" action="/admin/wallet/adjust">
        {csrf_field(session)}
        <label>用户邮箱<input name="email" required></label>
        <label>方向<select name="direction">
        <option value="add">加款</option>
        <option value="sub">扣款</option></select></label>
        <label>金额（元）<input name="amount" required
        inputmode="decimal"></label>
        <label>备注（客户在收支明细可见）<input name="note"
        placeholder="如：线下收款补储值"></label>
        <p><button class="btn" type="submit">提交调账</button></p>
        </form>
        <p class="hint">调账立即生效并记入流水；扣款不能超过当前余额。</p>
        </div>
        <div class="card"><h1>重置用户密码</h1>
        <form method="post" action="/admin/wallet/reset-password">
        {csrf_field(session)}
        <label>用户邮箱<input name="email" required></label>
        <label>新密码（至少 8 位）<input type="password"
        name="password" required></label>
        <label>再输一次新密码<input type="password"
        name="password2" required></label>
        <p><button class="btn" type="submit">重置密码</button></p>
        </form>
        <p class="hint">客户忘记密码时用：先通过客服 / QQ 核验身份，
        在这里设置新密码后告知客户。重置后该用户已有的登录状态
        会全部失效，需要用新密码重新登录。</p>
        </div>
        <div class="card"><h1>修改会员等级</h1>
        <form method="post" action="/admin/wallet/set-level">
        {csrf_field(session)}
        <label>用户邮箱<input name="email" required></label>
        <label>设为等级<select name="level">
        <option value="-1">恢复自动（按消费 / 充值计算）</option>
        {lv_options}</select></label>
        <p><button class="btn" type="submit">保存等级</button></p>
        </form>
        <p class="hint">手动设置的等级立即生效，优先于按累计消费 /
        充值自动计算的等级（用户列表里会标注「手动」）；选「恢复
        自动」即交回系统计算。适合线下成交补等级、活动赠送等级等
        场景。</p>
        </div>
        <div class="card"><h1>用户余额</h1>
        <table><tr><th>用户</th><th>余额</th><th>会员等级</th><th>注册时间</th></tr>
        {urows}</table></div>
        <div class="card"><h1>最近流水</h1>
        <table><tr><th>时间</th><th>用户</th><th>类型</th><th>变动</th>
        <th>余额</th><th>说明</th></tr>
        {lrows}</table></div>"""
        self.send_html(page("储值管理", body, user,
                            flash_ok=ok, flash_err=err))

    def admin_wallet_adjust(self, form):
        session, user = self.require_login()
        if user is None:
            return
        if not user["is_admin"]:
            return self.redirect("/admin/login")
        if not self.check_csrf(session, form):
            return self.redirect("/admin/wallet?err=badamount")
        email = (form.get("email") or "").strip()
        conn = db()
        target = conn.execute("SELECT * FROM users WHERE email=?",
                              (email,)).fetchone()
        if target is None:
            conn.close()
            return self.redirect("/admin/wallet?err=nouser")
        try:
            cents = int(round(float(form.get("amount", "")) * 100))
        except (TypeError, ValueError):
            cents = 0
        if cents <= 0:
            conn.close()
            return self.redirect("/admin/wallet?err=badamount")
        delta = cents if form.get("direction") == "add" else -cents
        try:
            apply_balance_change(conn, target["id"], delta, "admin", "",
                                 (form.get("note") or "").strip()
                                 or "店主调账")
        except ValueError:
            conn.close()
            return self.redirect("/admin/wallet?err=insufficient")
        conn.commit()
        conn.close()
        self.redirect("/admin/wallet?ok=1")

    def admin_wallet_set_level(self, form):
        """店主手动给客户改会员等级：写入 users.level_manual，
        生效等级以手动值为准（优先于按消费/充值算的自动等级）；
        level=-1 表示清除手动值、恢复自动。"""
        session, user = self.require_login()
        if user is None:
            return
        if not user["is_admin"]:
            return self.redirect("/admin/login")
        if not self.check_csrf(session, form):
            return self.redirect("/admin/wallet?err=badlevel")
        email = (form.get("email") or "").strip()
        try:
            lvl = int(form.get("level", ""))
        except (TypeError, ValueError):
            lvl = -99
        if lvl != -1 and not (0 <= lvl < len(LEVELS)):
            return self.redirect("/admin/wallet?err=badlevel")
        conn = db()
        target = conn.execute("SELECT id FROM users WHERE email=?",
                              (email,)).fetchone()
        if target is None:
            conn.close()
            return self.redirect("/admin/wallet?err=nouser")
        if lvl == -1:
            conn.execute(
                "UPDATE users SET level_manual=NULL WHERE id=?",
                (target["id"],))
        else:
            conn.execute(
                "UPDATE users SET level_manual=? WHERE id=?",
                (lvl, target["id"]))
        conn.commit()
        conn.close()
        self.redirect("/admin/wallet?ok=lvl")

    def admin_reset_password(self, form):
        """店主人工重置用户密码（客户忘记密码时用）：按邮箱定位用户，
        用现有 PBKDF2 逻辑更新密码哈希，并删除该用户全部现有会话，
        强制其用新密码重新登录。用户不存在时只给反馈、不做任何修改。"""
        session, user = self.require_login()
        if user is None:
            return
        if not user["is_admin"]:
            return self.redirect("/admin/login")
        if not self.check_csrf(session, form):
            return self.redirect("/admin/wallet")
        email = (form.get("email") or "").strip()
        password = form.get("password") or ""
        if password != (form.get("password2") or ""):
            return self.redirect("/admin/wallet?err=pwmismatch")
        if len(password) < 8:
            return self.redirect("/admin/wallet?err=pwshort")
        conn = db()
        target = conn.execute("SELECT id FROM users WHERE email=?",
                              (email,)).fetchone()
        if target is None:
            conn.close()
            return self.redirect("/admin/wallet?err=nouser")
        salt, pw_hash = hash_password(password)
        conn.execute("UPDATE users SET salt=?, pass_hash=? WHERE id=?",
                     (salt, pw_hash, target["id"]))
        conn.execute("DELETE FROM sessions WHERE user_id=?",
                     (target["id"],))
        conn.commit()
        conn.close()
        self.redirect("/admin/wallet?ok=pw")

    def admin_support_page(self, query):
        _, user = self.require_login()
        if user is None:
            return
        if not user["is_admin"]:
            return self.redirect("/admin/login")
        conn = db()
        convs = conn.execute(
            "SELECT u.id AS uid, u.email,"
            " (SELECT body FROM support_messages m WHERE m.user_id=u.id"
            "   ORDER BY m.id DESC LIMIT 1) AS last_body,"
            " (SELECT created_at FROM support_messages m"
            "   WHERE m.user_id=u.id ORDER BY m.id DESC LIMIT 1) AS last_at,"
            " (SELECT COUNT(*) FROM support_messages m"
            "   WHERE m.user_id=u.id AND m.sender='user'"
            "   AND m.is_read=0) AS unread"
            " FROM users u"
            " WHERE EXISTS (SELECT 1 FROM support_messages m"
            "               WHERE m.user_id=u.id)"
            " ORDER BY last_at DESC").fetchall()
        conn.close()
        rows = ""
        for c in convs:
            badge = (f'<span class="sup-badge">{c["unread"]}</span>'
                     if c["unread"] else "")
            preview = (c["last_body"] or "")[:40]
            rows += (f'<tr><td><a href="/admin/support/{c["uid"]}">'
                     f'{esc(c["email"])}</a>{badge}</td>'
                     f'<td>{esc(preview)}</td>'
                     f'<td>{esc(c["last_at"] or "")}</td></tr>')
        if not rows:
            rows = '<tr><td colspan="3" class="hint">暂无客户消息</td></tr>'
        body = f"""<div class="card"><h1>卖家后台 · 客服消息</h1>
        {admin_tabs("support")}
        <table><tr><th>客户</th><th>最新消息</th><th>时间</th></tr>
        {rows}</table>
        <p class="hint">点客户邮箱进入会话回复；红角标是未读条数，
        打开会话即清零。</p>
        </div>"""
        self.send_html(page("客服消息", body, user))

    def admin_support_thread(self, uid_str, err=""):
        session, user = self.require_login()
        if user is None:
            return
        if not user["is_admin"]:
            return self.redirect("/admin/login")
        try:
            uid = int(uid_str)
        except ValueError:
            return self.redirect("/admin/support")
        conn = db()
        target = conn.execute("SELECT * FROM users WHERE id=?",
                              (uid,)).fetchone()
        if target is None:
            conn.close()
            return self.redirect("/admin/support")
        msgs = conn.execute(
            "SELECT * FROM support_messages WHERE user_id=?"
            " ORDER BY id ASC LIMIT 300", (uid,)).fetchall()
        conn.execute(
            "UPDATE support_messages SET is_read=1"
            " WHERE user_id=? AND sender='user'", (uid,))
        conn.commit()
        conn.close()
        bubbles, last_id = chat_bubbles(msgs, "admin")
        body = f"""
        <div class="card"><h1>客服会话 · {esc(target['email'])}</h1>
        {admin_tabs("support")}
        <div class="chat" id="chatBox" data-last="{last_id}"
             data-poll="/admin/support/poll?user={uid}">{bubbles}</div>
        <form class="chat-form" method="post"
              action="/admin/support/{uid}/send">
        {csrf_field(session)}
        <textarea name="body" rows="2" maxlength="2000" required
        placeholder="输入回复"></textarea>
        <button class="btn" type="submit">回复</button>
        </form>
        <p><a href="/admin/support">← 返回会话列表</a></p>
        </div>{CHAT_POLL_JS}"""
        self.send_html(page("客服会话", body, user, flash_err=err))

    def admin_support_send(self, uid_str, form):
        session, user = self.require_login()
        if user is None:
            return
        if not user["is_admin"]:
            return self.redirect("/admin/login")
        try:
            uid = int(uid_str)
        except ValueError:
            return self.redirect("/admin/support")
        if not self.check_csrf(session, form):
            return self.admin_support_thread(
                uid_str, err="页面已过期，请刷新后重试。")
        text = (form.get("body") or "").strip()
        if text:
            conn = db()
            conn.execute(
                "INSERT INTO support_messages (user_id, sender, body,"
                " created_at) VALUES (?, 'admin', ?, ?)",
                (uid, text[:2000], now_text()))
            conn.commit()
            conn.close()
        self.redirect(f"/admin/support/{uid}")

    def admin_support_poll(self, query):
        _, user = self.session()
        if user is None or not user["is_admin"]:
            return self.send_text('{"messages": []}',
                                  content_type="application/json")
        try:
            uid = int(query.get("user", "0"))
            after = int(query.get("after", "0"))
        except ValueError:
            uid, after = 0, 0
        conn = db()
        rows = conn.execute(
            "SELECT * FROM support_messages WHERE user_id=? AND id>?"
            " ORDER BY id ASC LIMIT 50", (uid, after)).fetchall()
        if any(r["sender"] == "user" for r in rows):
            conn.execute(
                "UPDATE support_messages SET is_read=1 WHERE user_id=?"
                " AND sender='user' AND id<=?", (uid, rows[-1]["id"]))
            conn.commit()
        conn.close()
        msgs = [{"id": r["id"], "body": r["body"],
                 "created_at": r["created_at"],
                 "mine": r["sender"] == "admin",
                 "who": "我" if r["sender"] == "admin" else "客户"}
                for r in rows]
        self.send_text(json.dumps({"messages": msgs}, ensure_ascii=False),
                       content_type="application/json")


def main():
    init_db()
    if EPAY_POLL_ENABLED:
        threading.Thread(target=_epay_poll_loop, name="epay-poll",
                         daemon=True).start()
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "8080"))
    server = ThreadingHTTPServer((host, port), Handler)
    print(f"曜石 AI · OBSIDIAN 已启动：http://{host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
