from aiohttp import web, web_exceptions
from service.api.schema import RecognizeSchema
from service.api.utils.scrapper import get_video
import asyncio


class RecognizeVideo(web.View):
    URL_PATH = [r"/recognize", r"/recognize/", ]

    async def post(self):
        if not self.request.body_exists:
            raise web_exceptions.HTTPBadRequest(reason='body-doesnt-exits')
        temp = await self.request.json()
        schema = RecognizeSchema.parse_obj(temp)
        asyncio.create_task(asyncio.wait_for(get_video(schema.source, schema.prefix), timeout=600))
        return web.json_response({"code": 200, "message": "video is being processed"}, status=200)
