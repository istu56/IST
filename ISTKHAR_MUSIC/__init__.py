# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (suraj08832) 🚀
# This source code is under MIT License 📜
# Unauthorized forking, importing, or using without credit will result in legal action ⚠️
# DM for permission : @brahix
# =======================================================

import asyncio
from pyrogram import Client
from ISTKHAR_MUSIC.core.bot import ISTKHAR
from ISTKHAR_MUSIC.core.userbot import run_userbots, Userbot
from ISTKHAR_MUSIC.core.dir import dirr
from ISTKHAR_MUSIC.core.git import git
from ISTKHAR_MUSIC.misc import dbb, heroku
from config import LOGGER_ID  # log channel/group ID from config

# -------------------- INITIAL SETUP --------------------
dirr()      # update directories
git()       # initialize git
dbb()       # load database
heroku()    # heroku config

# -------------------- START MAIN BOT --------------------
app = ISTKHAR  # Pyrogram Client object

# -------------------- START ALL USERBOTS --------------------
run_userbots(log_chat_id=LOGGER_ID)  # Start assistants
userbot = Userbot()                   # Initialize userbot object

# -------------------- ADDITIONAL PLATFORMS --------------------
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