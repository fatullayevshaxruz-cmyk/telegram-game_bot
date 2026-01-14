# bot.py - FotMob Mini App Telegram Bot (Aiogram)

import asyncio
import os
import json
from datetime import datetime
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://your-domain.com")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))  # Admin Telegram ID

bot = Bot(token=BOT_TOKEN)
dp = None  # Dispatcher async main ichida yaratiladi

# =============================
# DATABASE (JSON fayl)
# =============================
DB_FILE = "users.json"

def load_users():
    """Foydalanuvchilarni yuklash"""
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"users": {}}

def save_users(data):
    """Foydalanuvchilarni saqlash"""
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def add_user(user: types.User):
    """Yangi foydalanuvchini qo'shish"""
    data = load_users()
    user_id = str(user.id)
    
    if user_id not in data["users"]:
        data["users"][user_id] = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "joined_at": datetime.now().isoformat(),
            "last_active": datetime.now().isoformat()
        }
        save_users(data)
        return True  # Yangi foydalanuvchi
    else:
        # Mavjud foydalanuvchi - last_active yangilash
        data["users"][user_id]["last_active"] = datetime.now().isoformat()
        save_users(data)
        return False

def get_stats():
    """Statistika olish"""
    data = load_users()
    users = data.get("users", {})
    
    total = len(users)
    
    # So'nggi 24 soatda faol
    now = datetime.now()
    active_24h = 0
    active_7d = 0
    
    for user in users.values():
        try:
            last_active = datetime.fromisoformat(user.get("last_active", ""))
            diff = now - last_active
            if diff.days < 1:
                active_24h += 1
            if diff.days < 7:
                active_7d += 1
        except:
            pass
    
    return {
        "total": total,
        "active_24h": active_24h,
        "active_7d": active_7d
    }


# =============================
# TILLAR
# =============================
MESSAGES = {
    "uz": {
        "welcome": "👋 Assalomu alaykum!\n\n⚽️ FotMob Mini App - futbol dunyosining barcha yangiliklarini kuzatib boring!\n\n📱 Ilovani ochish uchun quyidagi tugmani bosing:",
        "select_lang": "🌍 Tilni tanlang:",
        "open_app": "📱 Ilovani ochish"
    },
    "ru": {
        "welcome": "👋 Здравствуйте!\n\n⚽️ FotMob Mini App - следите за всеми новостями мира футбола!\n\n📱 Нажмите кнопку ниже, чтобы открыть приложение:",
        "select_lang": "🌍 Выберите язык:",
        "open_app": "📱 Открыть приложение"
    },
    "en": {
        "welcome": "👋 Hello!\n\n⚽️ FotMob Mini App - Follow all football news from around the world!\n\n📱 Tap the button below to open the app:",
        "select_lang": "🌍 Select language:",
        "open_app": "📱 Open App"
    }
}


def get_language_keyboard():
    """Til tanlash klaviaturasi - 3 til"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="lang_uz"),
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"),
            InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")
        ]
    ])


def get_webapp_keyboard(lang: str):
    """Web App ochish klaviaturasi"""
    webapp_url = f"{WEBAPP_URL}?lang={lang}"
    msg = MESSAGES.get(lang, MESSAGES["uz"])
    
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=msg["open_app"],
                web_app=WebAppInfo(url=webapp_url)
            )
        ],
        [
            InlineKeyboardButton(text="🌍 Tilni o'zgartirish", callback_data="change_lang")
        ]
    ])


# =============================
# HANDLERS
# =============================

async def start_command(message: types.Message):
    """Start buyrug'i - til tanlash"""
    # Foydalanuvchini bazaga qo'shish
    is_new = add_user(message.from_user)
    
    await message.answer(
        MESSAGES["uz"]["select_lang"],
        reply_markup=get_language_keyboard()
    )


async def admin_command(message: types.Message):
    """Admin panel - statistika"""
    if message.from_user.id != ADMIN_ID:
        await message.answer("⛔️ Sizda admin huquqi yo'q!")
        return
    
    stats = get_stats()
    
    text = f"""
📊 <b>Admin Panel - Statistika</b>

👥 <b>Jami foydalanuvchilar:</b> {stats['total']}
🟢 <b>24 soatda faol:</b> {stats['active_24h']}
📅 <b>7 kunda faol:</b> {stats['active_7d']}

🕐 <i>Yangilangan: {datetime.now().strftime('%Y-%m-%d %H:%M')}</i>
"""
    
    await message.answer(text, parse_mode="HTML")


async def broadcast_command(message: types.Message):
    """Barcha foydalanuvchilarga xabar yuborish"""
    if message.from_user.id != ADMIN_ID:
        await message.answer("⛔️ Sizda admin huquqi yo'q!")
        return
    
    # Xabar matnini olish
    text = message.text.replace("/broadcast", "").strip()
    
    if not text:
        await message.answer("📝 Xabar matnini kiriting:\n\n<code>/broadcast Sizning xabaringiz</code>", parse_mode="HTML")
        return
    
    data = load_users()
    users = data.get("users", {})
    
    sent = 0
    failed = 0
    
    for user_id in users.keys():
        try:
            await bot.send_message(int(user_id), text)
            sent += 1
            await asyncio.sleep(0.05)  # Flood limitdan qochish
        except Exception:
            failed += 1
    
    await message.answer(f"✅ Xabar yuborildi!\n\n📤 Yuborildi: {sent}\n❌ Xatolik: {failed}")


async def language_selected(callback: types.CallbackQuery):
    """Til tanlanganda"""
    # Foydalanuvchini yangilash
    add_user(callback.from_user)
    
    lang = callback.data.replace("lang_", "")
    msg = MESSAGES.get(lang, MESSAGES["uz"])
    
    await callback.message.edit_text(
        msg["welcome"],
        reply_markup=get_webapp_keyboard(lang)
    )
    await callback.answer()


async def change_language(callback: types.CallbackQuery):
    """Tilni o'zgartirish"""
    await callback.message.edit_text(
        MESSAGES["uz"]["select_lang"],
        reply_markup=get_language_keyboard()
    )
    await callback.answer()


# =============================
# RUN BOT
# =============================

async def main():
    global dp
    dp = Dispatcher()
    
    # Handlerlarni ro'yxatdan o'tkazish
    dp.message.register(start_command, CommandStart())
    dp.message.register(admin_command, Command("admin"))
    dp.message.register(broadcast_command, Command("broadcast"))
    dp.callback_query.register(language_selected, F.data.startswith("lang_"))
    dp.callback_query.register(change_language, F.data == "change_lang")
    
    print("🤖 FotMob Bot ishga tushdi!")
    print(f"📊 Admin ID: {ADMIN_ID}")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
