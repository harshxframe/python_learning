import concurrent.futures
import time
from tracemalloc import take_snapshot

lis = [1,2,3]

def checkStock(stock):
    print("Stocking in progress...")
    time.sleep(3)
    print("\nStock operation done {quan: 34, ave:True}")



#Making request

with concurrent.futures.ThreadPoolExecutor(max_workers=len(lis)) as executor:
    task = executor.map(checkStock, lis)





print("Program finished")
