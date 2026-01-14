# bot.py - FotMob Mini App Telegram Bot (Aiogram)

import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://your-domain.com")  # Web App URL

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# =============================
# TILLAR
# =============================
MESSAGES = {
    "uz": {
        "welcome": "👋 Assalomu alaykum!\n\n⚽️ FotMob Mini App - futbol dunyosining barcha yangiliklarini kuzatib boring!\n\n📱 Ilovani ochish uchun quyidagi tugmani bosing:",
        "select_lang": "🌍 Tilni tanlang / Выберите язык:",
        "open_app": "📱 Ilovani ochish"
    },
    "ru": {
        "welcome": "👋 Здравствуйте!\n\n⚽️ FotMob Mini App - следите за всеми новостями мира футбола!\n\n📱 Нажмите кнопку ниже, чтобы открыть приложение:",
        "select_lang": "🌍 Tilni tanlang / Выберите язык:",
        "open_app": "📱 Открыть приложение"
    }
}


def get_language_keyboard():
    """Til tanlash klaviaturasi"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="lang_uz"),
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")
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

@dp.message(CommandStart())
async def start_command(message: types.Message):
    """Start buyrug'i - til tanlash"""
    await message.answer(
        MESSAGES["uz"]["select_lang"],
        reply_markup=get_language_keyboard()
    )


@dp.callback_query(F.data.startswith("lang_"))
async def language_selected(callback: types.CallbackQuery):
    """Til tanlanganda"""
    lang = callback.data.replace("lang_", "")
    msg = MESSAGES.get(lang, MESSAGES["uz"])
    
    await callback.message.edit_text(
        msg["welcome"],
        reply_markup=get_webapp_keyboard(lang)
    )
    await callback.answer()


@dp.callback_query(F.data == "change_lang")
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
    print("🤖 FotMob Bot ishga tushdi!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
