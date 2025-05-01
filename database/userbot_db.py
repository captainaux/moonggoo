from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

class Database:
    def __init__(self):
        self.client = AsyncIOMotorClient(MONGO_URI)
        self.db = self.client["userbot_db"]

db = Database()
