import logging
from aiohttp import web
from service.logger.access import AccessLogger
from aiomisc.log import basic_config


def setup_routes(app: web.Application) -> None:
    from service.api.routes import setup_routes as sr
    sr(app)


def setup_middlewares(app: web.Application) -> None:
    from service.data.middleware import error_middleware
    app.middlewares.append(error_middleware)


def main() -> None:
    basic_config(level=logging.DEBUG, buffered=True)
    app = web.Application()
    setup_routes(app)
    setup_middlewares(app)
    web.run_app(app, port=80, access_log_class=AccessLogger)


if __name__ == '__main__':
    main()
