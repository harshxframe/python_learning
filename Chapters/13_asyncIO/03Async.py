import asyncio
import aiohttp


async def fetchUrl(session, url):
    print("Fetching....")
    async with session.get("https://jsonplaceholder.typicode.com/todos/1") as response:
        print(await response.text())


async def main():
    urls = ["https://jsonplaceholder.typicode.com/todos"] * 3
    async with aiohttp.ClientSession() as session:
        task = [fetchUrl(session, url) for url in urls]
        await asyncio.gather(*task)


# asyncio.run(main())

asyncio.run(main())
