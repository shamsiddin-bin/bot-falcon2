# handlers.py
"""
Botning barcha /start, menyu tugmalari va admin panel handlerlari.
Faqat Reply Keyboard orqali ishlaydi (Web App tugmasidan tashqari inline yo'q).
"""

import uuid

from aiogram import Router, F, Bot
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import config
import database as db
import keyboards as kb
from locales import t, LANGUAGE_BUTTONS, DEFAULT_LANG
from states import AdminStates, PaymentStates

router = Router()


def is_admin(user_id: int) -> bool:
    return user_id == config.ADMIN_ID


async def get_lang(user_id: int) -> str:
    lang = await db.get_user_language(user_id)
    return lang or DEFAULT_LANG


# ==================== /start ====================

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    user = message.from_user

    await db.add_user(
        user_id=user.id,
        username=user.username or "—",
        full_name=user.full_name,
    )

    existing_lang = await db.get_user_language(user.id)

    if not existing_lang:
        await message.answer(
            t(DEFAULT_LANG, "choose_language"),
            reply_markup=kb.language_keyboard(),
        )
        return

    await send_welcome(message, existing_lang)


async def send_welcome(message: Message, lang: str):
    user = message.from_user
    await message.answer(
        t(lang, "welcome", name=user.full_name, school=config.SCHOOL_NAME),
        reply_markup=kb.main_menu_keyboard(lang, is_admin=is_admin(user.id)),
    )
    await message.answer(
        t(
            lang,
            "social_links",
            instagram=config.INSTAGRAM_URL,
            channel=config.TELEGRAM_CHANNEL_URL,
        )
    )


# ==================== TIL TANLASH (istalgan payt ishlaydi) ====================

@router.message(F.text.in_(LANGUAGE_BUTTONS.keys()))
async def handle_language_selection(message: Message, state: FSMContext):
    await state.clear()
    lang = LANGUAGE_BUTTONS[message.text]
    user = message.from_user

    await db.add_user(user_id=user.id, username=user.username or "—", full_name=user.full_name)
    await db.set_user_language(user.id, lang)

    await message.answer(t(lang, "language_set"))
    await send_welcome(message, lang)


# ==================== ADMIN: E'LON QO'SHISH HOLATI ====================

@router.message(AdminStates.waiting_announcement)
async def process_new_announcement(message: Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)

    if message.text == t(lang, "btn_back"):
        await state.clear()
        await message.answer(t(lang, "admin_panel_title"), reply_markup=kb.admin_menu_keyboard(lang))
        return

    text = message.caption or message.text
    file_id = None
    file_type = None

    if message.photo:
        file_id = message.photo[-1].file_id
        file_type = "photo"
    elif message.document:
        file_id = message.document.file_id
        file_type = "document"

    await db.add_announcement(text=text, file_id=file_id, file_type=file_type)
    await state.clear()
    await message.answer(t(lang, "announcement_saved"), reply_markup=kb.admin_menu_keyboard(lang))


# ==================== ADMIN: JADVAL YANGILASH HOLATI ====================

@router.message(AdminStates.waiting_schedule)
async def process_new_schedule(message: Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)

    if message.text == t(lang, "btn_back"):
        await state.clear()
        await message.answer(t(lang, "admin_panel_title"), reply_markup=kb.admin_menu_keyboard(lang))
        return

    caption = message.caption or message.text
    file_id = None
    file_type = None

    if message.photo:
        file_id = message.photo[-1].file_id
        file_type = "photo"
    elif message.document:
        file_id = message.document.file_id
        file_type = "document"

    await db.set_schedule(file_id=file_id, file_type=file_type, caption=caption)
    await state.clear()
    await message.answer(t(lang, "schedule_saved"), reply_markup=kb.admin_menu_keyboard(lang))


# ==================== TO'LOV: SUMMA KUTISH HOLATI ====================

@router.message(PaymentStates.waiting_amount)
async def process_payment_amount(message: Message, state: FSMContext, bot: Bot):
    user = message.from_user
    lang = await get_lang(user.id)

    if message.text == t(lang, "btn_back"):
        await state.clear()
        await message.answer(t(lang, "back_to_main"), reply_markup=kb.main_menu_keyboard(lang, is_admin=is_admin(user.id)))
        return

    amount_text = (message.text or "").replace(" ", "").replace(",", "")
    if not amount_text.isdigit():
        await message.answer(t(lang, "payment_invalid_amount"))
        return

    amount = int(amount_text)
    tx_id = uuid.uuid4().hex[:10]

    await db.create_payment(user_id=user.id, amount=amount, transaction_id=tx_id, status="pending")
    await state.clear()

    await message.answer(
        t(lang, "payment_pending", tx_id=tx_id, amount=amount),
        reply_markup=kb.main_menu_keyboard(lang, is_admin=is_admin(user.id)),
    )

    try:
        await bot.send_message(
            config.ADMIN_ID,
            t(lang, "payment_admin_notify", full_name=user.full_name, user_id=user.id, amount=amount, tx_id=tx_id),
        )
    except Exception:
        pass


# ==================== ASOSIY MENYU VA ADMIN MENYU DISPATCHER ====================

@router.message(StateFilter(None), F.text)
async def main_menu_dispatcher(message: Message, state: FSMContext, bot: Bot):
    user = message.from_user
    lang = await get_lang(user.id)
    text = message.text
    admin = is_admin(user.id)

    # --- Asosiy menyu tugmalari ---
    if text == t(lang, "btn_announcements"):
        announcements = await db.get_recent_announcements(limit=5)
        if not announcements:
            await message.answer(t(lang, "no_announcement"))
            return
        await message.answer(t(lang, "announcements_title"))
        for ann in announcements:
            caption = ann["text"] or ""
            if ann["file_type"] == "photo" and ann["file_id"]:
                await message.answer_photo(ann["file_id"], caption=caption)
            elif ann["file_type"] == "document" and ann["file_id"]:
                await message.answer_document(ann["file_id"], caption=caption)
            else:
                await message.answer(caption or "—")
        return

    if text == t(lang, "btn_schedule"):
        schedule = await db.get_latest_schedule()
        if not schedule or not schedule.get("file_id"):
            if schedule and schedule.get("caption"):
                await message.answer(schedule["caption"])
            else:
                await message.answer(t(lang, "no_schedule"))
            return
        caption = schedule.get("caption") or ""
        if schedule["file_type"] == "photo":
            await message.answer_photo(schedule["file_id"], caption=caption)
        else:
            await message.answer_document(schedule["file_id"], caption=caption)
        return

    if text == t(lang, "btn_payment"):
        await state.set_state(PaymentStates.waiting_amount)
        await message.answer(t(lang, "payment_prompt_amount"), reply_markup=kb.back_keyboard(lang))
        return

    if text == t(lang, "btn_language"):
        await message.answer(t(lang, "choose_language"), reply_markup=kb.language_keyboard())
        return

    if text == t(lang, "btn_contact"):
        await message.answer(
            t(
                lang,
                "contact_text",
                school=config.SCHOOL_NAME,
                address=config.SCHOOL_ADDRESS,
                phone1=config.SCHOOL_PHONE_1,
                phone2=config.SCHOOL_PHONE_2,
                email=config.SCHOOL_EMAIL,
                workhours=config.SCHOOL_WORKHOURS,
            )
        )
        return

    if text == t(lang, "btn_admin"):
        if not admin:
            await message.answer(t(lang, "admin_only"))
            return
        await message.answer(t(lang, "admin_panel_title"), reply_markup=kb.admin_menu_keyboard(lang))
        return

    # --- Admin submenyu tugmalari (faqat admin uchun) ---
    if admin and text == t(lang, "btn_admin_add_announcement"):
        await state.set_state(AdminStates.waiting_announcement)
        await message.answer(t(lang, "admin_send_announcement_prompt"), reply_markup=kb.back_keyboard(lang))
        return

    if admin and text == t(lang, "btn_admin_update_schedule"):
        await state.set_state(AdminStates.waiting_schedule)
        await message.answer(t(lang, "admin_send_schedule_prompt"), reply_markup=kb.back_keyboard(lang))
        return

    if admin and text == t(lang, "btn_admin_stats"):
        stats = await db.get_stats()
        await message.answer(t(lang, "admin_stats_text", **stats), reply_markup=kb.admin_menu_keyboard(lang))
        return

    if text == t(lang, "btn_back"):
        await message.answer(t(lang, "back_to_main"), reply_markup=kb.main_menu_keyboard(lang, is_admin=admin))
        return

    # --- Hech biriga mos kelmasa ---
    await message.answer(t(lang, "unknown_message"))


# ==================== NOMA'LUM (matn bo'lmagan) XABARLAR ====================

@router.message(StateFilter(None))
async def handle_unknown_message(message: Message):
    lang = await get_lang(message.from_user.id)
    await message.answer(t(lang, "unknown_message"))
