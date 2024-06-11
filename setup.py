from aiohttp import web
from src.web import init_app


if __name__ == '__main__':
    app = init_app()
    web.run_app(app)
