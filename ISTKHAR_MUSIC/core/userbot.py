# ISTKHAR_MUSIC/core/userbot.py
from pyrogram import Client
import config
from ..logging import LOGGER  # Make sure logging.py exists in ISTKHAR_MUSIC/core

assistants = []
assistant_ids = []


class Userbot:
    def __init__(self):
        # Create Pyrogram clients for each string session
        self.one = Client(
            name="ISTKHAR_Assistant1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="ISTKHAR_Assistant2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="ISTKHAR_Assistant3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="ISTKHAR_Assistant4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="ISTKHAR_Assistant5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info("» Starting ISTKHAR_MUSIC assistants...")

        # Start each assistant safely
        for idx, client in enumerate([self.one, self.two, self.three, self.four, self.five], start=1):
            string_attr = f"STRING{idx}"
            if getattr(config, string_attr, None):
                await client.start()
                assistants.append(idx)
                assistant_ids.append(client.me.id)
                LOGGER(__name__).info(f"✦ Assistant {idx} started as {client.me.mention}")

                # Join required chats
                try:
                    await client.join_chat("Vibe_Bots")
                    await client.join_chat("IamIstkhar")
                except:
                    pass

                # Send log message
                try:
                    await client.send_message(config.LOGGER_ID, f"» Assistant {idx} started successfully!")
                except:
                    LOGGER(__name__).error(
                        f"» Assistant {idx} failed to access log group. Make sure it is added and promoted!"
                    )

        LOGGER(__name__).info(f"» Total {len(assistants)} assistants started successfully.")

    async def stop(self):
        LOGGER(__name__).info("» Stopping all ISTKHAR_MUSIC assistants...")
        for client in [self.one, self.two, self.three, self.four, self.five]:
            try:
                await client.stop()
            except:
                pass
        LOGGER(__name__).info("» All assistants stopped successfully.")