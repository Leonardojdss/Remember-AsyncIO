import asyncio

async def proces_order(order: list):
    print(f"Order {order["id"]} in processament")
    if order["payment_aproved"] == False:
        return print(f"Payment is reproved for order {order["id"]}")
    print(f"Payment aproved for order {order["id"]}")
        
    if order["available_stock"] == False:
        return print(f"Stock unavailable for order {order["id"]}")
    print(f"Stock available to order {order["id"]}")
    
    print(f"order {order["id"]} confirmed! Send for delivery")
    
async def main(list_orders: list):
    task = [asyncio.create_task(proces_order(n)) for n in list_orders]
    await asyncio.gather(*task)
    print("All orders has processed")
    
list_orders = [
    {"id": 101, "payment_aproved": True, "available_stock": True},
    {"id": 102, "payment_aproved": True, "available_stock": False},
    {"id": 103, "payment_aproved": False, "available_stock": True},
    {"id": 104, "payment_aproved": True, "available_stock": True},
    {"id": 105, "payment_aproved": False, "available_stock": False},
]

asyncio.run(main(list_orders))