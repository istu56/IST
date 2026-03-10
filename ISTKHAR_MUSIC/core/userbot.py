# =======================================================
# Userbot launcher for ISTKHAR_MUSIC
# =======================================================

from pyrogram import Client
from config import STRING1, STRING2, STRING3, STRING4, STRING5, STRING6, STRING7

userbots = []

STRING_SESSIONS = [
    STRING1, STRING2, STRING3, STRING4, STRING5, STRING6, STRING7
]

def run_userbots(log_chat_id: int):
    """
    Launch all userbot assistants.
    Make sure each string session is valid.
    """
    from ISTKHAR_MUSIC.core.bot import app  # lazy import to avoid circular import
    for i, string in enumerate(STRING_SESSIONS, start=1):
        if string:
            ubot = Client(
                f"assistant{i}",
                api_id=app.API_ID,
                api_hash=app.API_HASH,
                session_string=string
            )
            ubot.start()
            userbots.append(ubot)
            print(f"[INFO] Assistant {i} started and ready!")
    print(f"[INFO] All {len(userbots)} userbots started successfully.")
    return userbots