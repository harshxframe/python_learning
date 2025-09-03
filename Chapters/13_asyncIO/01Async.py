import asyncio
import time


async def main():
    print("Hello word!")
    await asyncio.sleep(2)
    print("Task done")




asyncio.run(main())