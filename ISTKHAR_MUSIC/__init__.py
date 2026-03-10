# __init__.py
import asyncio
import logging as pylogging
from pyrogram import Client

# ------------------------------
# Logger setup
# ------------------------------
LOGGER = pylogging.getLogger("ISTKHAR_MUSIC")
LOGGER.setLevel(pylogging.INFO)
console = pylogging.StreamHandler()
formatter = pylogging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console.setFormatter(formatter)
LOGGER.addHandler(console)

# ------------------------------
# Telegram log chat ID (optional)
# ------------------------------
LOGGER_ID = -1003565819974  # yahan apna log chat ID daal do

# ------------------------------
# Pyrogram bot client
# ------------------------------
app = Client(
    "ISTKHAR_BOT",
    api_id=YOUR_API_ID,
    api_hash="YOUR_API_HASH",
    bot_token="YOUR_BOT_TOKEN"
)

# ------------------------------
# Optional functions
# ------------------------------
try:
    from .core.dir import update_dirs
    update_dirs()
    LOGGER.info("Directories updated.")
except ImportError:
    LOGGER.warning("update_dirs function not found, skipping.")
except Exception as e:
    LOGGER.error(f"Error updating dirs: {e}")

try:
    from .core.git import check_git
    check_git()
    LOGGER.info("Git client found.")
except ImportError:
    LOGGER.warning("check_git function not found, skipping.")
except Exception as e:
    LOGGER.error(f"Error in git check: {e}")

try:
    from .misc import load_database
    load_database()
    LOGGER.info("Database loaded.")
except ImportError:
    LOGGER.warning("load_database function not found, skipping.")
except Exception as e:
    LOGGER.error(f"Error loading database: {e}")

# ------------------------------
# Run userbots safely
# ------------------------------
def start_userbots():
    try:
        from .userbot import start as run_userbots
        asyncio.run(run_userbots(log_chat_id=LOGGER_ID))
    except ImportError:
        LOGGER.error("run_userbots function not found.")
    except Exception as e:
        LOGGER.error(f"Error running userbots: {e}")

start_userbots()