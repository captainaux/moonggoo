from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

class UserbotClient(Client):
    def __init__(self):
        super().__init__(
            name="userbot",
            api_id=API_ID,
            api_hash=API_HASH,
            plugins=dict(root="handlers"),
            in_memory=True
        )

class BotClient(Client):
    def __init__(self):
        super().__init__(
            name="login_bot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN
        )