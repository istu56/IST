# __init__.py
import asyncio
import logging
from .core.dir import update_dirs
from .core.git import check_git
from .misc import load_database

# Logger setup
LOGGER_ID = -1001234567890  # yahan apna log chat ID daal do

# Step 1: Directories update
update_dirs()
logging.info("ᴅɪʀᴇᴄᴛᴏʀɪᴇs ᴜᴘᴅᴀᴛᴇᴅ.")

# Step 2: Git client check
check_git()
logging.info("ɢɪᴛ ᴄʟɪᴇɴᴛ ғᴏᴜɴᴅ [ᴠᴘs ᴅᴇᴘʟᴏʏᴇʀ]")

# Step 3: Load database
load_database()
logging.info("𝗗𝗔𝗧𝗔𝗕𝗔𝗦𝗘 𝗟𝗢𝗔𝗗𝗘𝗗 𝗕𝗔𝗕𝗬 🎀")

# Step 4: Run userbots safely
def start_userbots():
    from .userbot import run_userbots  # import yahan rakho circular import avoid karne ke liye
    asyncio.run(run_userbots(log_chat_id=LOGGER_ID))

# Call the function
start_userbots()