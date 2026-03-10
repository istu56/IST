import asyncio
import logging
from pyrogram import Client
from pyrogram.enums import ParseMode

from config import API_ID, API_HASH, BOT_TOKEN, LOGGER_ID


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
)

LOGGER = logging.getLogger("ISTKHAR_MUSIC.core.bot")


class Bot:
    def __init__(self):
        self.app = Client(
            "ISTKHAR_MUSIC_BOT",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            parse_mode=ParseMode.HTML
        )

    async def start(self):
        await self.app.start()
        LOGGER.info("sᴛᴀʀᴛɪɴɢ ʙᴏᴛ...")

        # log group check
        try:
            if LOGGER_ID:
                await self.app.send_message(
                    LOGGER_ID,
                    "✅ **ISTKHAR MUSIC BOT STARTED SUCCESSFULLY**"
                )
        except Exception as e:
            LOGGER.error("ʙᴏᴛ ʜᴀs ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴇ ʟᴏɢ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ.")
            LOGGER.error(f"Reason :- {type(e).__name__}")

        LOGGER.info("✅ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ")

    async def stop(self):
        await self.app.stop()
        LOGGER.info("❌ ʙᴏᴛ sᴛᴏᴘᴘᴇᴅ")


bot = Bot()


async def start_bot():
    await bot.start()


async def stop_bot():
    await bot.stop()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
    loop.run_forever()