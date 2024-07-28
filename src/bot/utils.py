from typing import Callable

from aiogram.types import (
    CallbackQuery,
    Message,
)

HandlerFuncType = Callable[[Message | CallbackQuery], None]
MessageHandlerFuncType = Callable[[Message], None]


def callback_handler_wrapper(handler: HandlerFuncType) -> MessageHandlerFuncType:
    async def wrapper(event: Message | CallbackQuery):
        if isinstance(event, CallbackQuery):
            message = event.message

        if isinstance(event, Message):
            message = event

        await handler(message)

        if isinstance(event, CallbackQuery):
            await message.delete()

    return wrapper
