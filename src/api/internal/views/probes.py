from aiohttp import web


async def healthcheck_view(request: web.Request) -> web.Response:
    return web.json_response({"status": "ok"})
