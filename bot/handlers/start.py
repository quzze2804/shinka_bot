from aiogram import Router, types
from aiogram.types import Message
from aiogram.filters import Command
from bot.keyboards.main_menu import main_menu_keyboard

router = Router()

@router.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer(
        "👋 Вітаємо у шиномонтажі!\nОберіть потрібну дію нижче 👇",
        reply_markup=main_menu_keyboard()
    )
