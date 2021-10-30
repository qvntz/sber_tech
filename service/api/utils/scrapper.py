import asyncio
import aiohttp
from time import time


def write_image(data, prefix):
    filename = f"{prefix}-file-{int(time() * 1000)}.mp4"
    with open(filename, 'wb') as file:
        file.write(data)


async def fetch_content(url, session, prefix):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data, prefix)


async def get_video(url, prefix):
    async with aiohttp.ClientSession() as session:
        task = asyncio.create_task(fetch_content(url, session, prefix))
        await asyncio.gather(task)
