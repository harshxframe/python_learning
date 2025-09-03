import asyncio


async def main(name):
    print(f"Hello {name} is Coming...")
    await asyncio.sleep(2)
    print(f"{name} arrived")



async def featherIO():
    await asyncio.gather(
        main("Hey Ayushi"),
        main("Hey Harsh.."),
        main("Hey Arya...")
    )




asyncio.run(featherIO())
