# =======================================================
# Core Imports
from ISTKHAR_MUSIC.core.dir import dirr
from ISTKHAR_MUSIC.core.git import git
from ISTKHAR_MUSIC.misc import dbb, heroku
from .logging import LOGGER

# -------------------- INITIAL SETUP --------------------
dirr()
git()
dbb()
heroku()

# -------------------- MAIN BOT --------------------
from ISTKHAR_MUSIC.core.bot import ISTKHAR
app = ISTKHAR()  # ← Sirf yahan banao, imports ke baad

# -------------------- USERBOTS --------------------
# Lazy import to avoid circular issues
from ISTKHAR_MUSIC.core.userbot import run_userbots
run_userbots(log_chat_id=LOGGER.ID)

# -------------------- API OBJECTS --------------------
# Import APIs after app is ready
from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()