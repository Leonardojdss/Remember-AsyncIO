import asyncio

async def factorial(input: int):
    total = 1
    for i in range(2, input+1):
        await asyncio.sleep(1)
        total *= i
    print(f"factorial of {input} = {total}")
    return total

async def main(list_input: list):
    task = [asyncio.create_task(factorial(n)) for n in list_input]
    await asyncio.gather(*task)

input = [5, 3, 7, 4, 6]

asyncio.run(main(input))