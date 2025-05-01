import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH, BOT_TOKEN, ALLOWED_USERS
from database.mongodb import db

async def main():
    # Sebelum start bot
    await db.connect()
    
    try:
        await bot.start()
        await asyncio.Event().wait()
    finally:
        await db.close()
        
# Bot untuk handle login
bot = Client(
    "login_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Handler untuk command start
@bot.on_message(filters.command("start") & filters.user(ALLOWED_USERS))
async def start_bot(client: Client, message: Message):
    await message.reply("🔥 **UserBot Started!**\nKirim /login untuk mulai setup")

# Handler untuk proses login
@bot.on_message(filters.command("login") & filters.user(ALLOWED_USERS))
async def login_userbot(client: Client, message: Message):
    # Minta nomor telepon
    await message.reply("📱 **Masukkan nomor telepon Telegram Anda**\n\nContoh: +628123456789")
    
    try:
        phone_number = await client.listen(message.chat.id, filters.text, timeout=300)
        
        # Init userbot client
        userbot = Client(
            "my_userbot",
            api_id=API_ID,
            api_hash=API_HASH,
            phone_number=phone_number.text,
            in_memory=True
        )
        
        # Proses login
        await userbot.connect()
        sent_code = await userbot.send_code(phone_number.text)
        
        # Minta kode OTP
        await message.reply("🔢 **Masukkan kode OTP**\n\nContoh: 12345")
        code = await client.listen(message.chat.id, filters.text, timeout=300)
        
        # Proses verifikasi
        await userbot.sign_in(
            phone_number.text,
            sent_code.phone_code_hash,
            code.text
        )
        
        # Cek jika 2FA diperlukan
        if await userbot.password.needs_2fa():
            await message.reply("🔑 **Masukkan password 2FA**")
            password = await client.listen(message.chat.id, filters.text, timeout=300)
            await userbot.check_password(password.text)
        
        await message.reply("✅ **Login Berhasil!**\nUserBot siap digunakan!")
        await userbot.disconnect()
        
    except Exception as e:
        await message.reply(f"❌ **Error:** {str(e)}")

# Handler untuk pesan lainnya
@bot.on_message(filters.user(ALLOWED_USERS) & filters.text)
async def handle_message(client: Client, message: Message):
    await message.reply("✨ **Aktif!**\nGunakan /login untuk setup userbot")

async def main():
    await bot.start()
    print("Bot login berjalan...")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())