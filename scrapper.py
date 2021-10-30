import asyncio
import aiohttp
from time import time


def write_image(data):
    filename = f"file-{int(time() * 1000)}.mp4"
    with open(filename, 'wb') as file:
        file.write(data)


async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data)


async def main():
    url = r'http://hackaton.sber-zvuk.com/hackathon_part_1.mp4?'
    async with aiohttp.ClientSession() as session:
        task = asyncio.create_task(fetch_content(url, session))

        await asyncio.gather(task)

if __name__ == '__main__':
    t0 = time()
    asyncio.run(main())
    print(time() - t0)