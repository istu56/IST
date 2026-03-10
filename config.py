# ISTKHAR_MUSIC/config.py
import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# ---------------- LOAD ENV VARIABLES ----------------
load_dotenv()

# ---------------- BASIC BOT CONFIG ----------------
API_ID = int(getenv("API_ID", "28362125"))
API_HASH = getenv("API_HASH", "c750e5872a2af51801d9b449983f4c84")
BOT_TOKEN = getenv("BOT_TOKEN", "6784567812:YOUR_BOT_TOKEN_HERE")

# ---------------- OWNER & BOT INFO ----------------
OWNER_ID = int(getenv("OWNER_ID", 7980630836))
OWNER_USERNAME = getenv("OWNER_USERNAME", "brahix")

BOT_USERNAME = getenv("BOT_USERNAME", "saregama_musics_bot")
BOT_NAME = getenv("BOT_NAME", "𝐌𝛊𝛕ຮ𝛖𝐫𝛊 𝐌𝛖ຮ𝛊𝛓⚡️")
ASSUSERNAME = getenv("ASSUSERNAME", "ISTKHARli")

# ---------------- DATABASE / REPO ----------------
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://parth3435:candy.mo4029k.mongodb.net/?retryWrites=true&w=majority")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/istu56/IST")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

# ---------------- API CONFIG ----------------
API_URL = getenv("API_URL", "https://pytdbotapi.thequickearn.xyz")
VIDEO_API_URL = getenv("VIDEO_API_URL", "https://api.video.thequickearn.xyz")
API_KEY = getenv("API_KEY", "NxGBNexGenBotsc75140")

GIT_TOKEN = getenv("GIT_TOKEN", "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")

# ---------------- LOGGER & LINKS ----------------
LOGGER_ID = int(getenv("LOGGER_ID", -1003565819974))

PRIVACY_LINK = getenv("PRIVACY_LINK", "https://telegra.ph/Privacy-Policy-for-YukkiMusic-08-30")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Iamistkhar")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+yKqAivJnwbcwOWJl")

# ---------------- LIMITS & TIME ----------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
DURATION_LIMIT = 60 * DURATION_LIMIT_MIN  # seconds

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", 9000))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", 9999999))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", 9999999))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# ---------------- SPOTIFY CONFIG ----------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")

# ---------------- STRING SESSIONS ----------------
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)

# ---------------- IMAGE / THUMBNAILS ----------------
START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/x5lytj.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/leaexg.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/b0e4vk.jpg"
STATS_IMG_URL = "https://files.catbox.moe/psya34.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/2y5o3g.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/2y5o3g.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"

# ---------------- UTILITIES ----------------
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ---------------- FUNCTIONS ----------------
def time_to_seconds(time: str) -> int:
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

# ---------------- VALIDATIONS ----------------
if SUPPORT_CHANNEL and not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - SUPPORT_CHANNEL url is wrong. Must start with https://")

if SUPPORT_CHAT and not re.match(r"(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - SUPPORT_CHAT url is wrong. Must start with https://")
