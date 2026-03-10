# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (suraj08832) 🚀
# Source under MIT License 📜
# =======================================================

import asyncio
from ISTKHAR_MUSIC.core.dir import dirr
from ISTKHAR_MUSIC.core.git import git
from ISTKHAR_MUSIC.misc import dbb, heroku
from .logging import LOGGER

# -------------------- INITIAL SETUP --------------------
dirr()
git()
dbb()
heroku()

# -------------------- IMPORT BOT --------------------
from ISTKHAR_MUSIC.core.bot import ISTKHAR
app = ISTKHAR()  # ← Create main bot after all setup

# -------------------- RUN USERBOTS --------------------
# Lazy import to avoid circular import
from ISTKHAR_MUSIC.core.userbot import run_userbots
run_userbots(log_chat_id=LOGGER.ID)

# -------------------- IMPORT PLUGINS / API --------------------
# Import plugins and API objects after bot is ready
from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()