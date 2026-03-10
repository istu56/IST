# =======================================================
# ISTKHAR_MUSIC Initialization
# =======================================================

import asyncio
from pyrogram import Client
from ISTKHAR_MUSIC.core.bot import ISTKHAR
from ISTKHAR_MUSIC.core.dir import dirr
from ISTKHAR_MUSIC.core.git import git
from ISTKHAR_MUSIC.core.userbot import run_userbots
from ISTKHAR_MUSIC.misc import dbb, heroku
from config import LOGGER_ID

# -------------------- INITIAL SETUP --------------------
dirr()       # Update directories
git()        # Initialize git
dbb()        # Database check
heroku()     # Heroku setup

# -------------------- START MAIN BOT --------------------
app = ISTKHAR  # Pyrogram Client object

# -------------------- START ALL USERBOTS --------------------
# This will start assistants from STRING sessions
run_userbots(log_chat_id=LOGGER_ID)

# -------------------- PLATFORMS --------------------
# Optional: your API wrappers (if used)
from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

print("[INFO] Main bot and all assistants started successfully!")

# =======================================================
# ©️ 2025-26 Purvi Bots
# =======================================================