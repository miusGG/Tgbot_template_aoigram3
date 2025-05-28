from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from texts import hello_text

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    text = hello_text(message.from_user.first_name)
    await message.reply(text)
