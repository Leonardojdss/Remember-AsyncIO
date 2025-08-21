import asyncio

async def manage_subscription(user: dict, courses: dict):
    print(f"signing up {user['name']} in course for {user['course']}")
    
    if courses[user["course"]]["available"] > 0:
        courses[user["course"]]["available"] -= 1
        courses[user["course"]]["registered"].append(user["name"])
        return print(f"Subscribe confirmed for {user['name']} in course of {user['course']}")
    else:
        return print(f"Class full! {user['name']} couldn't enroll in the {user['course']} course.")

async def main(list_user: list, courses: dict):
    task = [asyncio.create_task(manage_subscription(n, courses)) for n in list_user]
    await asyncio.gather(*task)
    print("All subscribe has processed")

courses = {
    "Python advanced": {"available": 2, "registered": []},
    "Java for beginners": {"available": 1, "registered": []},
    "Machine Learning": {"available": 0, "registered": []},
}
 
users = [
    {"name": "Alice", "course": "Python advanced"},
    {"name": "Bruno", "course": "Python advanced"},
    {"name": "Carlos", "course": "Java for beginners"},
    {"name": "Daniela", "course": "Machine Learning"},
    {"name": "Alice", "course": "Python advanced"},  # Tentativa de inscrição duplicada
]

asyncio.run(main(users, courses))
