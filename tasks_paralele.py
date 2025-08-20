import asyncio
from datetime import datetime

async def download():
    print(f"Download Started in {datetime.now().strftime("%H:%M:%S.%f")[:-3]}")
    await asyncio.sleep(2)
    print(f"Download Finish in {datetime.now().strftime("%H:%M:%S.%f")[:-3]}")

async def analytics():
    print(f"Analyze of data started in {datetime.now().strftime("%H:%M:%S.%f")[:-3]}")
    await asyncio.sleep(2)
    print(f"Analyze of data finish in {datetime.now().strftime("%H:%M:%S.%f")[:-3]}")

async def main():
    execute = await asyncio.gather(
        download(),
        analytics()
    )
    
asyncio.run(main())