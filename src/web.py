from aiohttp import web

from src.api.internal.router import router as internal_router


async def init_app() -> web.Application:
    app = web.Application()
    app.router.add_routes(internal_router)
    return app
