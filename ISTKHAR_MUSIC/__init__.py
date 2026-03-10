# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (suraj08832) 🚀
# =======================================================

import asyncio
from pyrogram import Client

from ISTKHAR_MUSIC.core.bot import ISTKHAR
from ISTKHAR_MUSIC.core.dir import dirr
from ISTKHAR_MUSIC.core.git import git
from ISTKHAR_MUSIC.core.userbot import run_userbots
from ISTKHAR_MUSIC.misc import dbb, heroku
from .logging import LOGGER
from .platforms import *

# -------------------- INITIAL SETUP --------------------
dirr()
git()
dbb()
heroku()

# -------------------- START MAIN BOT --------------------
app = ISTKHAR()  # Pyrogram Client object

# -------------------- START ALL USERBOTS --------------------
# This replaces the old Userbot() import
run_userbots(log_chat_id=LOGGER.ID)  # Use your actual log channel id

# -------------------- API OBJECTS --------------------
Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()