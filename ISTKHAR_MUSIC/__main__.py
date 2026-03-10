import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from ISTKHAR_MUSIC import LOGGER, app, userbot
from ISTKHAR_MUSIC.core.call import ISTKHAR
from ISTKHAR_MUSIC.misc import sudo
from ISTKHAR_MUSIC.plugins import ALL_MODULES
from ISTKHAR_MUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()

    await sudo()

    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)

        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass

    # START BOT
    await app.start()

    # IMPORT PLUGINS
    for module in ALL_MODULES:
        importlib.import_module("ISTKHAR_MUSIC.plugins." + module)

    LOGGER("ISTKHAR_MUSIC.plugins").info("Successfully Imported Modules...")

    # START USERBOT
    await userbot.start()

    # START CALL CLIENT
    call = ISTKHAR()

    try:
        await call.stream_call(
            "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("ISTKHAR_MUSIC").error(
            "Please turn on the videochat of your log group/channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass

    await call.decorators()

    LOGGER("ISTKHAR_MUSIC").info(
        "ISTKHAR Music Bot Started Successfully."
    )

    await idle()

    # STOP
    await app.stop()
    await userbot.stop()

    LOGGER("ISTKHAR_MUSIC").info("Stopping ISTKHAR Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
