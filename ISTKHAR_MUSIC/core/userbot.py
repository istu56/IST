# ISTKHAR_MUSIC/core/userbot.py
import asyncio
from pyrogram import Client, filters
from config import STRING1, STRING2, STRING3, STRING4, STRING5, STRING6, STRING7, OWNER_ID
from pyrogram.types import Message

# ------------------- INITIALIZE USERBOTS -------------------
ASSISTANTS = []

STRING_SESSIONS = [STRING1, STRING2, STRING3, STRING4, STRING5, STRING6, STRING7]

for i, session in enumerate(STRING_SESSIONS, start=1):
    if session:
        client = Client(
            name=f"assistant{i}",
            session_string=session,
            api_id=28362125,       # apna API_ID ya config se le lo
            api_hash="c750e5872a2af51801d9b449983f4c84",  # config se le lo
        )
        ASSISTANTS.append(client)

# ------------------- START ALL ASSISTANTS -------------------
async def start_assistants():
    for client in ASSISTANTS:
        await client.start()
        # Ensure username is fetched after start
        client.me = await client.get_me()
        print(f"[✅] Assistant started: {client.me.username}")

# ------------------- CHECK LOG GROUP ACCESS -------------------
async def check_log_group(client: Client, log_chat_id: int):
    try:
        # Try to get chat info
        chat = await client.get_chat(log_chat_id)
        # Check if assistant is admin
        me = await client.get_me()
        member = await client.get_chat_member(chat.id, me.id)
        if member.status not in ["administrator", "creator"]:
            print(f"[❌] Assistant {me.username} is not admin in log group")
        else:
            print(f"[✅] Assistant {me.username} has admin access in log group")
    except Exception as e:
        print(f"[❌] Failed to access log group: {e}")

# ------------------- EXAMPLE MESSAGE HANDLER -------------------
# This is optional, can remove if not needed
async def assistant_example():
    for client in ASSISTANTS:
        @client.on_message(filters.command("ping") & filters.user(OWNER_ID))
        async def ping_handler(client, message: Message):
            await message.reply_text(f"Assistant {client.me.username} is alive!")

# ------------------- MAIN START -------------------
async def main_userbots(log_chat_id: int = None):
    await start_assistants()
    # Check log group if provided
    if log_chat_id:
        for client in ASSISTANTS:
            await check_log_group(client, log_chat_id)
    # Run example handler (optional)
    await assistant_example()

# ------------------- RUN FUNCTION -------------------
def run_userbots(log_chat_id: int = None):
    asyncio.get_event_loop().run_until_complete(main_userbots(log_chat_id))