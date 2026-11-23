from aiogram import Router
from aiogram.filters import CommandObject, CommandStart
from aiogram.types import Message

start_router = Router(name=__name__)


@start_router.message(CommandStart(deep_link=True))
async def start_handler(message: Message, command: CommandObject):
    args = command.args
    if args:
        await message.answer(f"qq {args}")
    else:
        await message.answer("иди нахуй отсюда")
