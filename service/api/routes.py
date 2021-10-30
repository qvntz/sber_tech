from service.api.handlers import HANDLERS
import logging


def setup_routes(app) -> None:
    log = logging.getLogger(__name__)
    for handler in HANDLERS:
        log.debug('Registering handler %r as %r', handler, handler.URL_PATH[0])
        app.router.add_route('*', handler.URL_PATH[0], handler)
        app.router.add_route('*', handler.URL_PATH[1], handler)
