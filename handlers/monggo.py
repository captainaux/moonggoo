from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

class MongoDB:
    def __init__(self):
        self.client = None
        self.db = None
    
    async def connect(self):
        self.client = AsyncIOMotorClient(MONGO_URI)
        self.db = self.client["userbot_db"]
        print("✅ Terhubung ke MongoDB")

    async def close(self):
        if self.client:
            await self.client.close()
            print("❌ Koneksi MongoDB ditutup")

# Instance global
db = MongoDB()