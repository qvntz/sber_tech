from aiohttp.abc import AbstractAccessLogger


class AccessLogger(AbstractAccessLogger):

    def _get_username(self, request):
        try:
            return request.cirrina.web_session.get('username')
        except Exception:
            return None

    def log(self, request, response, time):
        self.logger.info(
            f'{request.remote} '
            f'{request.method} {request.url} {response.status} '
            f'in {time:.6f}s')

