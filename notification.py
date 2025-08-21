import asyncio

async def send_notification(user: list):
    if user["notification_actived"] == False:
        print(f"{user["name"]} desactived notification. nothing has send")
        return
    
    if user["vip"] == True:
        print(f"notification VIP for {user["name"]} sended")
        return
        
    print(f"notification normal for {user["name"]} sended")
    
async def main(list_user: list):
    print("Send notifications")
    task = [asyncio.create_task(send_notification(n)) for n in list_user]
    await asyncio.gather(*task)
    print("All notification has sended")

list_users = [
    {"name": "Ana", "vip": True, "notification_actived": True},
    {"name": "João", "vip": False, "notification_actived": True},
    {"name": "Carla", "vip": False, "notification_actived": False},
]

asyncio.run(main(list_users))
