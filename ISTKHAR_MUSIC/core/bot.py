import logging
from pyrogram import Client
from pyrogram.enums import ParseMode

from config import API_ID, API_HASH, BOT_TOKEN, LOGGER_ID

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
)

LOGGER = logging.getLogger("ISTKHAR_MUSIC.core.bot")

# Main Bot Client
ISTKHAR = Client(
    "ISTKHAR_MUSIC_BOT",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    parse_mode=ParseMode.HTML
)


async def start_bot():
    await ISTKHAR.start()
    LOGGER.info("🚀 ISTKHAR MUSIC BOT STARTED")

    # Log group message (error aaye to ignore karega)
    try:
        if LOGGER_ID:
            await ISTKHAR.send_message(
                LOGGER_ID,
                "✅ **ISTKHAR MUSIC BOT START HO GAYA**"
            )
    except Exception as e:
        LOGGER.error("Bot log group access nahi kar pa raha.")
        LOGGER.error(f"Reason: {type(e).__name__}")


async def stop_bot():
    await ISTKHAR.stop()
    LOGGER.info("❌ ISTKHAR MUSIC BOT STOPPED")