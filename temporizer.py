import asyncio

async def timer(time: int):
    print(f"Timer of {time} seconds started")
    await asyncio.sleep(time)
    print(f"Timer finish after {time} seconds")

asyncio.run(timer(3))