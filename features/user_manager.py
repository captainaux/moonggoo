from database.mongodb import db

async def save_user_data(user_id: int, data: dict):
    await db.db.users.update_one(
        {"_id": user_id},
        {"$set": data},
        upsert=True
    )

async def get_user_data(user_id: int):
    return await db.db.users.find_one({"_id": user_id})