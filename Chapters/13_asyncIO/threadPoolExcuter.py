import concurrent.futures
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

lis = [1,2,3]

def checkStock(stock):
    print("Stocking in progress...")
    time.sleep(3)
    print("\nStock operation done {quan: 34, ave:True}")



#Making request
if __name__ == "__main__":
     async def makeRequest():
          print("Started making request")
          loop = asyncio.get_event_loop()
          with ProcessPoolExecutor(max_workers=3) as executor:
                tasks = [loop.run_in_executor(executor, checkStock, i) for i in lis]
                await asyncio.gather(*tasks)
                print("Finished making request")


     asyncio.run(makeRequest())
     print("Program finished")






