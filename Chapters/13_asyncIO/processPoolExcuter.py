import concurrent.futures
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor
from tracemalloc import take_snapshot

lis = [1,2,3]

def checkStock(stock):
    print("Stocking in progress...")
    time.sleep(3)
    print("\nStock operation done {quan: 34, ave:True}")



#Making request

async def makeRequest():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor(max_workers=3) as executor:
        tasks = [loop.run_in_executor(executor, checkStock, i) for i in lis]
        await asyncio.gather(*tasks)
        print("\nStock operation done {quan: 34, ave:True}")



asyncio.run(makeRequest())


print("Program finished")
