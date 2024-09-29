from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import Message

from create_bot import bot
from create_dispather import dp

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(text='Hello')