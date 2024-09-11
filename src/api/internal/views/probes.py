from aiohttp import web

from src.domain.services.healthcheck import IHealthcheckService
from src.project.containers import get_container


async def healthcheck_view(request: web.Request) -> web.Response:
    container = get_container()
    healthcheck_service = container.resolve(IHealthcheckService)
    response_data = await healthcheck_service.check()
    return web.json_response(response_data)
