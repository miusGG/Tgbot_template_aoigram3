from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from tgbot.filters.admin import AdminFilter
from texts import hello_text

admin_router = Router()
admin_router.message.filter(AdminFilter())


@admin_router.message(CommandStart())
async def admin_start(message: Message):
    await message.reply("[Only for Admins] Admin Mode: On")
    text = hello_text(message.from_user.first_name)
    await message.reply(text)
