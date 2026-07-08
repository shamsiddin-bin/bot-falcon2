# config.py
"""
Botning barcha sozlamalari: maxfiy ma'lumotlar (.env dan) va
maktabga oid ochiq ma'lumotlar (linklar, manzil, telefon va h.k.)
"""

import os
from dotenv import load_dotenv

load_dotenv()

# --- MAXFIY MA'LUMOTLAR (.env faylidan) ---
API_TOKEN: str = os.getenv("API_TOKEN")
ADMIN_ID: int = int(os.getenv("ADMIN_ID", "0"))

if not API_TOKEN:
    raise ValueError(
        "❌ API_TOKEN topilmadi! .env faylini yarating va "
        "unga API_TOKEN=... qatorini qo'shing."
    )

if ADMIN_ID == 0:
    raise ValueError(
        "❌ ADMIN_ID topilmadi! .env faylida ADMIN_ID=... "
        "qatorini to'g'ri kiriting."
    )

# --- MAKTAB HAQIDA OCHIQ MA'LUMOTLAR ---
SCHOOL_NAME = "Falcon IT Maktabi"

# Web App manzili (https bilan boshlanishi shart)
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://falcon-production-45f3.up.railway.app/")

# Ijtimoiy tarmoqlar
INSTAGRAM_URL = os.getenv("INSTAGRAM_URL", "https://instagram.com/your_school")
TELEGRAM_CHANNEL_URL = os.getenv("TELEGRAM_CHANNEL_URL", "https://t.me/your_channel")

# Aloqa ma'lumotlari
SCHOOL_ADDRESS = os.getenv("SCHOOL_ADDRESS", "Toshkent shahri, Chilonzor tumani, 25-uy")
SCHOOL_PHONE_1 = os.getenv("SCHOOL_PHONE_1", "+998 71 123 45 67")
SCHOOL_PHONE_2 = os.getenv("SCHOOL_PHONE_2", "+998 90 123 45 67")
SCHOOL_EMAIL = os.getenv("SCHOOL_EMAIL", "info@maktab-example.uz")
SCHOOL_WORKHOURS = os.getenv("SCHOOL_WORKHOURS", "Dushanba - Shanba, 08:00 - 17:00")

# --- TO'LOV TIZIMI (Click / Payme) ---
# DIQQAT: Haqiqiy to'lovni yoqish uchun tadbirkor/biznes hisobi, merchant ID
# va maxfiy kalitlar kerak, shuningdek webhook qabul qiladigan alohida
# HTTPS server (FastAPI/Flask) kerak bo'ladi. Hozircha bu bo'lim skeleton
# holida ishlaydi: foydalanuvchi summani kiritadi, so'rov "pending" holatda
# bazaga yoziladi va admin xabardor qilinadi. Merchant ma'lumotlari
# tayyor bo'lgach, payments.py (yoki alohida webhook_server.py) ga
# Click/Payme API chaqiruvlarini qo'shish kifoya.
PAYMENT_PROVIDER = os.getenv("PAYMENT_PROVIDER", "")  # "click" | "payme" | ""
CLICK_MERCHANT_ID = os.getenv("CLICK_MERCHANT_ID", "")
CLICK_SERVICE_ID = os.getenv("CLICK_SERVICE_ID", "")
CLICK_SECRET_KEY = os.getenv("CLICK_SECRET_KEY", "")
PAYME_MERCHANT_ID = os.getenv("PAYME_MERCHANT_ID", "")
PAYME_SECRET_KEY = os.getenv("PAYME_SECRET_KEY", "")

# Baza fayli nomi
DATABASE_NAME = "school_bot.db"
