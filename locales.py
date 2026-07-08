# locales.py
"""
Bot ichidagi barcha matnlar shu yerda, 3 til uchun: uz, ru, en.
t(lang, key, **kwargs) funksiyasi orqali kerakli tildagi matn olinadi.
"""

LOCALES = {
    "uz": {
        "choose_language": "🌐 Tilni tanlang:",
        "language_set": "✅ Til o'zbek tiliga o'rnatildi.",
        "welcome": (
            "👋 Assalomu alaykum, <b>{name}</b>!\n\n"
            "🏫 <b>{school}</b> rasmiy botiga xush kelibsiz!\n\n"
            "Quyidagi menyudan kerakli bo'limni tanlang 👇"
        ),
        "social_links": (
            "📱 Bizni ijtimoiy tarmoqlarda kuzatib boring:\n\n"
            "📸 Instagram: {instagram}\n"
            "📢 Telegram kanal: {channel}"
        ),
        "btn_webapp": "🏫 Web App",
        "btn_announcements": "📢 E'lonlar",
        "btn_schedule": "📅 Dars jadvali",
        "btn_payment": "💳 To'lov qilish",
        "btn_language": "🌐 Til",
        "btn_contact": "📞 Aloqa",
        "btn_admin": "⚙️ Admin Panel",
        "btn_back": "◀️ Orqaga",
        "btn_admin_add_announcement": "📢 E'lon qo'shish",
        "btn_admin_update_schedule": "📅 Jadval yangilash",
        "btn_admin_stats": "📊 Statistika",
        "no_announcement": "😔 Hozircha e'lonlar mavjud emas.",
        "no_schedule": "😔 Hozircha dars jadvali yuklanmagan.",
        "announcements_title": "📢 <b>So'nggi e'lonlar:</b>",
        "contact_text": (
            "📞 <b>Biz bilan bog'lanish</b>\n\n"
            "🏫 <b>{school}</b>\n\n"
            "📍 Manzil: {address}\n"
            "☎️ Telefon 1: {phone1}\n"
            "☎️ Telefon 2: {phone2}\n"
            "📧 Email: {email}\n"
            "🕘 Ish vaqti: {workhours}"
        ),
        "admin_only": "⛔ Sizda ushbu bo'limga ruxsat yo'q!",
        "admin_panel_title": "⚙️ <b>ADMIN PANEL</b>\n\nKerakli bo'limni tanlang 👇",
        "admin_send_announcement_prompt": (
            "📢 Yangi e'lon uchun matn, rasm yoki hujjat yuboring "
            "(rasm/hujjat bilan birga izoh ham qo'shishingiz mumkin).\n\n"
            "Bekor qilish uchun ◀️ Orqaga tugmasini bosing."
        ),
        "admin_send_schedule_prompt": (
            "📅 Yangi dars jadvali uchun rasm yoki hujjat yuboring "
            "(izoh ixtiyoriy).\n\n"
            "Bekor qilish uchun ◀️ Orqaga tugmasini bosing."
        ),
        "announcement_saved": "✅ E'lon muvaffaqiyatli saqlandi va foydalanuvchilarga ko'rinadi.",
        "schedule_saved": "✅ Dars jadvali muvaffaqiyatli yangilandi.",
        "admin_stats_text": (
            "📊 <b>Statistika</b>\n\n"
            "👥 Jami foydalanuvchilar: <b>{total}</b>\n"
            "🇺🇿 O'zbek tili: <b>{uz}</b>\n"
            "🇷🇺 Rus tili: <b>{ru}</b>\n"
            "🇬🇧 Ingliz tili: <b>{en}</b>"
        ),
        "payment_prompt_amount": "💳 To'lov summasini so'mda kiriting (masalan: 150000):",
        "payment_invalid_amount": "❌ Iltimos, summani faqat raqamlarda kiriting.",
        "payment_pending": (
            "🕓 So'rovingiz qabul qilindi (ID: <code>{tx_id}</code>, summa: {amount} so'm).\n\n"
            "⚠️ Onlayn to'lov tizimi (Click/Payme) hozircha ulanish jarayonida. "
            "Tez orada to'liq ishga tushiriladi. Hozircha to'lovni maktab kassasida "
            "amalga oshirishingiz mumkin. Admin sizning so'rovingiz haqida xabardor qilindi."
        ),
        "payment_admin_notify": (
            "💳 Yangi to'lov so'rovi!\n"
            "👤 {full_name} (ID: {user_id})\n"
            "💰 Summa: {amount} so'm\n"
            "🆔 Tranzaksiya: {tx_id}"
        ),
        "unknown_message": "🤔 Kechirasiz, bu buyruqni tushunmadim. Quyidagi menyudan foydalaning 👇",
        "back_to_main": "📋 Asosiy menyu:",
    },
    "ru": {
        "choose_language": "🌐 Выберите язык:",
        "language_set": "✅ Язык установлен: русский.",
        "welcome": (
            "👋 Здравствуйте, <b>{name}</b>!\n\n"
            "🏫 Добро пожаловать в официальный бот школы <b>{school}</b>!\n\n"
            "Выберите нужный раздел в меню ниже 👇"
        ),
        "social_links": (
            "📱 Следите за нами в соцсетях:\n\n"
            "📸 Instagram: {instagram}\n"
            "📢 Telegram канал: {channel}"
        ),
        "btn_webapp": "🏫 Web App",
        "btn_announcements": "📢 Объявления",
        "btn_schedule": "📅 Расписание",
        "btn_payment": "💳 Оплата",
        "btn_language": "🌐 Язык",
        "btn_contact": "📞 Контакты",
        "btn_admin": "⚙️ Админ панель",
        "btn_back": "◀️ Назад",
        "btn_admin_add_announcement": "📢 Добавить объявление",
        "btn_admin_update_schedule": "📅 Обновить расписание",
        "btn_admin_stats": "📊 Статистика",
        "no_announcement": "😔 Объявлений пока нет.",
        "no_schedule": "😔 Расписание пока не загружено.",
        "announcements_title": "📢 <b>Последние объявления:</b>",
        "contact_text": (
            "📞 <b>Связаться с нами</b>\n\n"
            "🏫 <b>{school}</b>\n\n"
            "📍 Адрес: {address}\n"
            "☎️ Телефон 1: {phone1}\n"
            "☎️ Телефон 2: {phone2}\n"
            "📧 Email: {email}\n"
            "🕘 Часы работы: {workhours}"
        ),
        "admin_only": "⛔ У вас нет доступа к этому разделу!",
        "admin_panel_title": "⚙️ <b>АДМИН ПАНЕЛЬ</b>\n\nВыберите раздел 👇",
        "admin_send_announcement_prompt": (
            "📢 Отправьте текст, фото или документ для нового объявления "
            "(к фото/документу можно добавить подпись).\n\n"
            "Чтобы отменить, нажмите ◀️ Назад."
        ),
        "admin_send_schedule_prompt": (
            "📅 Отправьте фото или документ с новым расписанием "
            "(подпись необязательна).\n\n"
            "Чтобы отменить, нажмите ◀️ Назад."
        ),
        "announcement_saved": "✅ Объявление успешно сохранено и видно пользователям.",
        "schedule_saved": "✅ Расписание успешно обновлено.",
        "admin_stats_text": (
            "📊 <b>Статистика</b>\n\n"
            "👥 Всего пользователей: <b>{total}</b>\n"
            "🇺🇿 Узбекский язык: <b>{uz}</b>\n"
            "🇷🇺 Русский язык: <b>{ru}</b>\n"
            "🇬🇧 Английский язык: <b>{en}</b>"
        ),
        "payment_prompt_amount": "💳 Введите сумму оплаты в сумах (например: 150000):",
        "payment_invalid_amount": "❌ Пожалуйста, введите сумму только цифрами.",
        "payment_pending": (
            "🕓 Ваш запрос принят (ID: <code>{tx_id}</code>, сумма: {amount} сум).\n\n"
            "⚠️ Онлайн-оплата (Click/Payme) пока находится в процессе подключения. "
            "Скоро будет запущена полностью. Пока вы можете оплатить в кассе школы. "
            "Администратор уведомлён о вашем запросе."
        ),
        "payment_admin_notify": (
            "💳 Новый запрос на оплату!\n"
            "👤 {full_name} (ID: {user_id})\n"
            "💰 Сумма: {amount} сум\n"
            "🆔 Транзакция: {tx_id}"
        ),
        "unknown_message": "🤔 Извините, я не понял эту команду. Используйте меню ниже 👇",
        "back_to_main": "📋 Главное меню:",
    },
    "en": {
        "choose_language": "🌐 Choose your language:",
        "language_set": "✅ Language set to English.",
        "welcome": (
            "👋 Hello, <b>{name}</b>!\n\n"
            "🏫 Welcome to the official bot of <b>{school}</b>!\n\n"
            "Choose a section from the menu below 👇"
        ),
        "social_links": (
            "📱 Follow us on social media:\n\n"
            "📸 Instagram: {instagram}\n"
            "📢 Telegram channel: {channel}"
        ),
        "btn_webapp": "🏫 Web App",
        "btn_announcements": "📢 Announcements",
        "btn_schedule": "📅 Class Schedule",
        "btn_payment": "💳 Make Payment",
        "btn_language": "🌐 Language",
        "btn_contact": "📞 Contact",
        "btn_admin": "⚙️ Admin Panel",
        "btn_back": "◀️ Back",
        "btn_admin_add_announcement": "📢 Add Announcement",
        "btn_admin_update_schedule": "📅 Update Schedule",
        "btn_admin_stats": "📊 Statistics",
        "no_announcement": "😔 No announcements yet.",
        "no_schedule": "😔 No schedule uploaded yet.",
        "announcements_title": "📢 <b>Latest announcements:</b>",
        "contact_text": (
            "📞 <b>Contact us</b>\n\n"
            "🏫 <b>{school}</b>\n\n"
            "📍 Address: {address}\n"
            "☎️ Phone 1: {phone1}\n"
            "☎️ Phone 2: {phone2}\n"
            "📧 Email: {email}\n"
            "🕘 Working hours: {workhours}"
        ),
        "admin_only": "⛔ You don't have access to this section!",
        "admin_panel_title": "⚙️ <b>ADMIN PANEL</b>\n\nChoose a section 👇",
        "admin_send_announcement_prompt": (
            "📢 Send text, a photo, or a document for the new announcement "
            "(you can add a caption to photo/document).\n\n"
            "Press ◀️ Back to cancel."
        ),
        "admin_send_schedule_prompt": (
            "📅 Send a photo or document with the new schedule "
            "(caption optional).\n\n"
            "Press ◀️ Back to cancel."
        ),
        "announcement_saved": "✅ Announcement saved successfully and is now visible to users.",
        "schedule_saved": "✅ Schedule updated successfully.",
        "admin_stats_text": (
            "📊 <b>Statistics</b>\n\n"
            "👥 Total users: <b>{total}</b>\n"
            "🇺🇿 Uzbek: <b>{uz}</b>\n"
            "🇷🇺 Russian: <b>{ru}</b>\n"
            "🇬🇧 English: <b>{en}</b>"
        ),
        "payment_prompt_amount": "💳 Enter the payment amount in UZS (e.g. 150000):",
        "payment_invalid_amount": "❌ Please enter the amount using digits only.",
        "payment_pending": (
            "🕓 Your request has been received (ID: <code>{tx_id}</code>, amount: {amount} UZS).\n\n"
            "⚠️ Online payment (Click/Payme) is still being connected and will be "
            "available soon. For now, you can pay at the school's office. "
            "The admin has been notified of your request."
        ),
        "payment_admin_notify": (
            "💳 New payment request!\n"
            "👤 {full_name} (ID: {user_id})\n"
            "💰 Amount: {amount} UZS\n"
            "🆔 Transaction: {tx_id}"
        ),
        "unknown_message": "🤔 Sorry, I didn't understand that. Please use the menu below 👇",
        "back_to_main": "📋 Main menu:",
    },
}

LANGUAGE_BUTTONS = {
    "🇺🇿 O'zbek": "uz",
    "🇷🇺 Русский": "ru",
    "🇬🇧 English": "en",
}

DEFAULT_LANG = "uz"


def t(lang: str, key: str, **kwargs) -> str:
    """Berilgan til va kalit bo'yicha matnni qaytaradi (mavjud bo'lmasa - uz)."""
    lang = lang if lang in LOCALES else DEFAULT_LANG
    text = LOCALES[lang].get(key, LOCALES[DEFAULT_LANG].get(key, key))
    return text.format(**kwargs) if kwargs else text
