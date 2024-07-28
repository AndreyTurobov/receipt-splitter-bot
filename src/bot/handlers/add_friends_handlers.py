import logging

from aiogram.types import (
    CallbackQuery,
    Message,
)

from src.bot.messages.add_friend import AddFriendMessageBuilder

logger = logging.getLogger(__name__)


async def start_add_friend_handler(message: Message | CallbackQuery) -> None:
    if isinstance(message, CallbackQuery):
        message = message.message

    content = AddFriendMessageBuilder().build()
    await message.reply(**content)
