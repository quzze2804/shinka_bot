from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from keyboards import main_menu_keyboard  # теперь просто keyboards

router = Router()

@router.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer(
        "👋 Вітаємо у шиномонтажі!\nОберіть дію нижче 👇",
        reply_markup=main_menu_keyboard()
    )
