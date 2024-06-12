from aiogram import (
    Bot,
    Dispatcher,
    types,
)
from aiogram.filters import CommandStart

from src.core.configs import settings


async def command_start_handler(message: types.Message) -> None:
    await message.answer(f'Hi, {message.from_user.full_name}!')


class CustomDispatcher(Dispatcher):
    async def process_update(
        self,
        update: types.Update,
    ):
        return await super().process_update(update)


async def init_bot() -> tuple[Bot, Dispatcher]:
    bot: Bot = Bot(token=settings.TELEGRAM_API_KEY)
    await bot.set_webhook(settings.TELEGRAM_WEBHOOK_URL)

    dp = Dispatcher()

    dp.message(CommandStart(), command_start_handler)

    return bot, dp
