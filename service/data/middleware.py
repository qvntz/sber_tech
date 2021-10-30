from pydantic import ValidationError
from aiohttp import web, web_exceptions
import logging
log = logging.getLogger(__name__)


@web.middleware
async def error_middleware(request, handler):
    try:
        temp = await handler(request)
    except (ValidationError, web_exceptions.HTTPBadRequest):
        temp = web.json_response({'code': 400, "message": "bad-parameters"}, status=400)
    except Exception:
        log.exception("Something went wrong")
        # todo logging
        temp = web.json_response({'code': 405, "message": "Method Not Allowed"}, status=405)

    return temp
