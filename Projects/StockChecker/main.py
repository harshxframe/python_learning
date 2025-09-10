import asyncio
import aiohttp
import threading

APIKey = "d30pta9r01qnu2qv4lrgd30pta9r01qnu2qv4ls0"

companies = [
    "AAPL",
]

stocksList = []

async def getStockPrice(session, companyName):
    print("Request started for", companyName)
    RequestUrl = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={companyName}&apikey={APIKey}"
    print("Fetching:", RequestUrl)
    try:
        # optional per-request timeout; you can also set ClientSession timeout globally
        async with session.get(RequestUrl) as response:
            if response.status != 200:
                print(f"Non-200 response for {companyName}: {response.status}")
                return
            data = await response.json()
    except Exception as e:
        print(f"Network/JSON error for {companyName}:", e)
        return

    # Debug: show raw response
    print("Data fetched for", companyName, "->", data)

    # Defensive checks: handle rate limit / errors / missing keys
    if "Note" in data:
        print("API Note (rate limit?) for", companyName, ":", data["Note"])
        return
    if "Error Message" in data:
        print("API Error for", companyName, ":", data["Error Message"])
        return

    gq = data.get("Global Quote") or data.get("globalQuote") or {}
    if not gq:
        print("No Global Quote for", companyName)
        return

    # Price key is "05. price"
    price_str = gq.get("05. price") or gq.get("5. price") or gq.get("price")
    if not price_str:
        print("No price field found for", companyName, "->", gq)
        return

    try:
        price = float(price_str.replace(',', ''))
    except Exception as e:
        print("Failed to convert price for", companyName, ":", price_str, e)
        return

    stocksList.append(price)
    print(f"Appended price for {companyName}:", price)


async def main():
    print("Programming request started...")
    timeout = aiohttp.ClientTimeout(total=15)  # avoid hanging forever
    async with aiohttp.ClientSession(timeout=timeout) as session:
        tasks = [getStockPrice(session, c) for c in companies]
        await asyncio.gather(*tasks)


def mainCall():
    # Option A: run in main thread (preferred)
    # asyncio.run(main())

    # Option B: if running inside a thread, create a new loop here (safer)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
    loop.close()


thr = threading.Thread(target=mainCall, args=[])
thr.start()
thr.join()

if len(stocksList) > 0:
    allSum = sum(stocksList)
    avg = allSum / len(stocksList)
    print("Average stock price of company:", avg)
else:
    print("No stock price data for companies")
