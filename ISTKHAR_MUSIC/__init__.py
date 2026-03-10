.# __init__.py
import asyncio
import logging as pylogging

# ------------------------------
# Logger setup
# ------------------------------
LOGGER = pylogging.getLogger("ISTKHAR_MUSIC")
LOGGER.setLevel(pylogging.INFO)

# Console handler
console = pylogging.StreamHandler()
formatter = pylogging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console.setFormatter(formatter)
LOGGER.addHandler(console)

# ------------------------------
# Telegram log chat ID (optional)
# ------------------------------
LOGGER_ID = -1001234567890  # yahan apna log chat ID daal do

# ------------------------------
# Step 1: Directories update (optional)
# ------------------------------
try:
    from .core.dir import update_dirs
    update_dirs()
    LOGGER.info("ᴅɪʀᴇᴄᴛᴏʀɪᴇs ᴜᴘᴅᴀᴛᴇᴅ.")
except ImportError:
    LOGGER.warning("update_dirs function not found, skipping directory update.")
except Exception as e:
    LOGGER.error(f"Error in directory update: {e}")

# ------------------------------
# Step 2: Git client check (optional)
# ------------------------------
try:
    from .core.git import check_git
    check_git()
    LOGGER.info("ɢɪᴛ ᴄʟɪᴇɴᴛ ғᴏᴜɴᴅ [ᴠᴘs ᴅᴇᴘʟᴏʏᴇʀ]")
except ImportError:
    LOGGER.warning("check_git function not found, skipping git check.")
except Exception as e:
    LOGGER.error(f"Error in git check: {e}")

# ------------------------------
# Step 3: Load database (optional)
# ------------------------------
try:
    from .misc import load_database
    load_database()
    LOGGER.info("𝗗𝗔𝗧𝗔𝗕𝗔𝗦𝗘 𝗟𝗢𝗔𝗗𝗘𝗗 𝗕𝗔𝗕𝗬 🎀")
except ImportError:
    LOGGER.warning("load_database function not found, skipping database load.")
except Exception as e:
    LOGGER.error(f"Error loading database: {e}")

# ------------------------------
# Step 4: Run userbots safely
# ------------------------------
def start_userbots():
    try:
        from .userbot import start as run_userbots  # import inside function to avoid circular import
        asyncio.run(run_userbots(log_chat_id=LOGGER_ID))
    except ImportError:
        LOGGER.error("run_userbots function not found, userbots will not run.")
    except Exception as e:
        LOGGER.error(f"Error running userbots: {e}")

# Call the function
start_userbots()