from aiohttp import web

from src.api.internal.router import router as internal_router
from src.bot.bot import init_bot
from src.bot.view import TelegramWebhookView
from src.core.configs import settings


async def init_app() -> web.Application:
    app = web.Application()

    bot, dp = await init_bot()
    app.router.add_route(
        '*',
        settings.TELEGRAM_WEBHOOK_PATH,
        TelegramWebhookView(dispatcher=dp, bot=bot),
        name='tg_webhook_handler',
    )

    app.router.add_routes(internal_router)

    return app
