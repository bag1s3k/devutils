import requests
import httpx
import asyncio
import time

import crcutils as crc

API_EXAMPLES = (
    {

    },
    {
        "base": "CZK"
    },
    {
        "symbols": ["USD", "GBP"]
    },
    {
        "base": "USD",
        "symbols": ["CZK", "JPY"]
    },
    {
        "date": "2024-12-24"
    },
    {
        "date": "2023-01-01",
        "base": "CHF"
    },
    {
        "date": "2022-10-01",
        "symbols": ["CZK", "PLN"]
    },
    {
        "date": "2025-10-01..2025-10-10"
    },
    {
        "date": "2024-06-01..2024-06-05",
        "base": "EUR",
        "symbols": ["CZK"]
    },
    {
        "date": "2023-11-01..2023-11-30",
        "base": "GBP",
        "symbols": ["USD", "CAD", "AUD"]
    }
)

async def get_currency(client, kwargs, index):
    response = await client.get(crc.get_url(**kwargs))
    if response.status_code == 200:
        print(f"Successful response with asyncio: {index}")
    else:
        raise Exception("Something failed")

async def main():
    async with httpx.AsyncClient() as client:
        async with asyncio.TaskGroup() as tg:
            for index, requirements in enumerate(API_EXAMPLES):
                tg.create_task(get_currency(client, requirements, index))

if "__main__" == __name__:
    # Sync usage
    t1_sync = time.time()
    for i, requirements_sync in enumerate(API_EXAMPLES):
        response_sync = requests.get(crc.get_url(**requirements_sync))
        if response_sync.status_code == 200:
            print(f"Successful response without asyncio: {i}")
        else:
            raise Exception("Something failed")
    time_sync = time.time() - t1_sync
    print()

    # Async usage
    t1_async = time.time()
    asyncio.run(main())
    time_async = time.time() - t1_async
    print(f"Without asyncio: {time_sync:.2f}")
    print(f"With asyncio: {time_async:.2f}\n")
    print(f"With asyncio is {round((time_async * time_sync * 100), 0)}% more faster")