# file: downloader_sim_compare.py
import time
import asyncio
import concurrent.futures

urlList = 5
delaySimulation = 5  # seconds per simulated download

# async simulated downloader (non-blocking)
async def file_downloader_async(id):
    await asyncio.sleep(delaySimulation)
    return f"async-{id}-done"

# blocking simulated downloader (used by thread pool)
def file_downloader_blocking(id):
    time.sleep(delaySimulation)
    return f"block-{id}-done"

async def run_asyncio_simulation():
    start = time.perf_counter()
    tasks = [file_downloader_async(i) for i in range(urlList)]
    results = await asyncio.gather(*tasks)
    elapsed = time.perf_counter() - start
    print(f"[asyncio] completed {len(results)} tasks in {elapsed:.4f} sec")
    return elapsed

def run_threadpool_simulation():
    start = time.perf_counter()
    # pass an iterable of IDs — not a string
    with concurrent.futures.ThreadPoolExecutor(max_workers=urlList) as executor:
        results = list(executor.map(file_downloader_blocking, range(urlList)))
    elapsed = time.perf_counter() - start
    print(f"[threadpool] completed {len(results)} tasks in {elapsed:.4f} sec")
    return elapsed

async def run_asyncio_with_to_thread():
    start = time.perf_counter()
    tasks = [asyncio.to_thread(file_downloader_blocking, i) for i in range(urlList)]
    results = await asyncio.gather(*tasks)
    elapsed = time.perf_counter() - start
    print(f"[asyncio + to_thread] completed {len(results)} tasks in {elapsed:.4f} sec")
    return elapsed

def main():
    print("Simulated download comparison — each task sleeps", delaySimulation, "seconds")
    # 1) pure asyncio
    asyncio.run(run_asyncio_simulation())

    # 2) thread pool
    run_threadpool_simulation()

    # 3) asyncio + to_thread (runs blocking functions concurrently in thread pool)
    asyncio.run(run_asyncio_with_to_thread())

if __name__ == "__main__":
    main()
