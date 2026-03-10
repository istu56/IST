# ISTKHAR_MUSIC/core/userbot.py
from pyrogram import Client
import asyncio
import config
import logging

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# List to hold all assistants
assistants = []
assistant_ids = []

class Userbot:
    def __init__(self):
        # List of all string sessions
        self.string_sessions = [
            config.STRING1,
            config.STRING2,
            config.STRING3,
            config.STRING4,
            config.STRING5,
            config.STRING6,
            config.STRING7
        ]
        # List to hold Pyrogram clients
        self.clients = []

        for i, string in enumerate(self.string_sessions, start=1):
            if string:
                client = Client(
                    name=f"Assistant{i}",
                    api_id=config.API_ID,
                    api_hash=config.API_HASH,
                    session_string=string,
                    no_updates=True
                )
                self.clients.append(client)

    async def start(self):
        LOGGER.info("» Starting all assistants...")
        for i, client in enumerate(self.clients, start=1):
            await client.start()
            assistants.append(client)
            assistant_ids.append(client.me.id)
            LOGGER.info(f"✦ Assistant {i} started as {client.me.mention}")

            # Join required chats
            try:
                await client.join_chat("Vibe_Bots")
                await client.join_chat("IamIstkhar")
            except Exception as e:
                LOGGER.warning(f"Assistant {i} couldn't join chats: {e}")

            # Send log message
            try:
                await client.send_message(config.LOGGER_ID, f"» Assistant {i} started successfully!")
            except Exception as e:
                LOGGER.error(f"Assistant {i} failed to access log group: {e}")

        LOGGER.info(f"» Total {len(self.clients)} assistants started successfully.")

    async def stop(self):
        LOGGER.info("» Stopping all assistants...")
        for client in self.clients:
            try:
                await client.stop()
            except Exception:
                pass
        LOGGER.info("» All assistants stopped.")