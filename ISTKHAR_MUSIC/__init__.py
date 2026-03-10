# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (suraj08832) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @brahix
# =======================================================

from ISTKHAR_MUSIC.core.bot import ISTKHAR
from ISTKHAR_MUSIC.core.dir import dirr
from ISTKHAR_MUSIC.core.git import git
from ISTKHAR_MUSIC.core.userbot import Userbot
from ISTKHAR_MUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = ISTKHAR
# ISTKHAR_MUSIC/__init__.py
import asyncio
from pyrogram import Client
from ISTKHAR_MUSIC.core.bot import ISTKHAR
from ISTKHAR_MUSIC.core.userbot import run_userbots
from config import LOGGER_ID  # apna log channel id yahan se le lo

# -------------------- START MAIN BOT --------------------
app = ISTKHAR()  # Pyrogram Client object

# -------------------- START ALL USERBOTS --------------------
# Run assistants and check log group access
# Replace LOGGER_ID with your actual log group/channel id
run_userbots(log_chat_id=LOGGER_ID)
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (suraj08832) 😎

# 🧑‍💻 Developer : t.me/brahix
# 🔗 Source link : GitHub.com/suraj08832/ISTKHARli-MusicV2
# 📢 Telegram channel : t.me/about_brahix
# =======================================================
