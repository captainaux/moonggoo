from pyrogram import filters
from core.client import BotClient
from features import broadcast

@BotClient.on_message(filters.command("broadcast"))
async def handle_broadcast(client: BotClient, message: Message):
    await broadcast_message(client.userbot, message)