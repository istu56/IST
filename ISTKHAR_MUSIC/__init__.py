# __init__.py
import asyncio
import logging

# Logger setup
LOGGER_ID = -1001234567890  # yahan apna log chat ID daal do

# ------------------------------
# Step 1: Directories update (optional)
# ------------------------------
try:
    from .core.dir import update_dirs
    update_dirs()
    logging.info("ᴅɪʀᴇᴄᴛᴏʀɪᴇs ᴜᴘᴅᴀᴛᴇᴅ.")
except ImportError:
    logging.warning("update_dirs function not found, skipping directory update.")

# ------------------------------
# Step 2: Git client check (optional)
# ------------------------------
try:
    from .core.git import check_git
    check_git()
    logging.info("ɢɪᴛ ᴄʟɪᴇɴᴛ ғᴏᴜɴᴅ [ᴠᴘs ᴅᴇᴘʟᴏʏᴇʀ]")
except ImportError:
    logging.warning("check_git function not found, skipping git check.")

# ------------------------------
# Step 3: Load database (optional)
# ------------------------------
try:
    from .misc import load_database
    load_database()
    logging.info("𝗗𝗔𝗧𝗔𝗕𝗔𝗦𝗘 𝗟𝗢𝗔𝗗𝗘𝗗 𝗕𝗔𝗕𝗬 🎀")
except ImportError:
    logging.warning("load_database function not found, skipping database load.")

# ------------------------------
# Step 4: Run userbots safely
# ------------------------------
def start_userbots():
    try:
        from .userbot import run_userbots  # import inside function to avoid circular import
        asyncio.run(run_userbots(log_chat_id=LOGGER_ID))
    except ImportError:
        logging.error("run_userbots function not found, userbots will not run.")
    except Exception as e:
        logging.error(f"Error running userbots: {e}")

# Call the function
start_userbots()