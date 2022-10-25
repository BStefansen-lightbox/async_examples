import requests
import time
import asyncio
import aiohttp


async def get_r(session):
    async with session.get('http://google.com') as response:
        return response.status


async def main(num):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(num):
            tasks.append(get_r(session))
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        print(results)

start_time = time.time()
asyncio.run(main(6))
print(f"Duration: {time.time() - start_time}")







