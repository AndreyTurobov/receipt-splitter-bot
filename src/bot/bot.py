import logging

from aiogram import (
    Bot,
    Dispatcher,
    F,
)
from aiogram.filters import (
    Command,
    CommandStart,
)

from src.bot.handlers.add_friends_handlers import (
    add_friend_manually_handler,
    start_add_friend_handler,
)
from src.bot.handlers.start_handler import start_handler
from src.bot.middlewares import GetOrCreateUserMiddleware
from src.bot.view import TelegramWebhookView
from src.project.configs import settings

logger = logging.getLogger(__name__)


def add_middlewares(dp: Dispatcher) -> None:
    dp.message.middleware(GetOrCreateUserMiddleware())
    dp.callback_query.middleware(GetOrCreateUserMiddleware())


def add_handlers(dp: Dispatcher) -> None:
    dp.message.register(start_handler, CommandStart())
    dp.callback_query.register(start_handler, F.data == "start")

    dp.callback_query.register(start_add_friend_handler, F.data == "friend")
    dp.message.register(start_add_friend_handler, Command(commands="friend"))

    dp.callback_query.register(
        add_friend_manually_handler,
        F.data == "add_friend_manually",
    )
    dp.message.register(
        add_friend_manually_handler,
        Command(commands="add_friend_manually"),
    )


async def telegram_view_factory() -> TelegramWebhookView:
    bot: Bot = Bot(token=settings.TELEGRAM_API_KEY)
    await bot.set_webhook(settings.TELEGRAM_WEBHOOK_URL)

    dp = Dispatcher()

    add_middlewares(dp)
    add_handlers(dp)

    return TelegramWebhookView(dispatcher=dp, bot=bot)
