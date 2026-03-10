# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (suraj08832) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @brahix
# =======================================================

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pymongo import MongoClient
import re, json, io, os
from ISTKHAR_MUSIC import app as ISTKHAR

mongo_url_pattern = re.compile(r"mongodb(?:\+srv)?:\/\/[^\s]+")


@ISTKHAR.on_message(filters.command("mongochk"))
async def mongo_command(client, message: Message):

    ADD_ME_BUTTON = InlineKeyboardMarkup(
        [[InlineKeyboardButton(f"✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙", url=f"https://t.me/{ISTKHAR.username}?startgroup=true")]]
    )

    if len(message.command) < 2:
        await message.reply(
            f"**⋟ ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴍᴏɴɢᴏ ᴜʀʟ ᴀꜰᴛᴇʀ ᴄᴏᴍᴍᴀɴᴅ.**\n\n**ᴇxᴀᴍᴘʟᴇ :-** /mongochk mongo_url`",
            reply_markup=ADD_ME_BUTTON
        )
        return

    mongo_url = message.command[1]
    if re.match(mongo_url_pattern, mongo_url):
        try:
            mongo_client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
            mongo_client.server_info()  # ⋟ ᴡɪʟʟ ᴄᴀᴜꜱᴇ ᴀɴ ᴇxᴄᴇᴘᴛɪᴏɴ ɪꜰ ᴄᴏɴɴᴇᴄᴛɪᴏɴ ꜰᴀɪʟꜱ
            await message.reply(
                f"**⋟ ᴍᴏɴɢᴏᴅʙ ᴜʀʟ ɪꜱ ᴠᴀʟɪᴅ ᴀɴᴅ ᴄᴏɴɴᴇᴄᴛɪᴏɴ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟ ✅**\n\n**⋟ ᴄʜᴇᴄᴋ ʙʏ :– {ISTKHAR.mention}**",
                reply_markup=ADD_ME_BUTTON
            )
        except Exception as e:
            await message.reply(
                f"**⋟ ꜰᴀɪʟᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ᴛᴏ ᴍᴏɴɢᴏᴅʙ :-** {e}\n\n**⋟ ᴄʜᴇᴄᴋ ʙʏ :– {ISTKHAR.mention}",
                reply_markup=ADD_ME_BUTTON
            )
    else:
        await message.reply(
            f"**⋟ ɪɴᴠᴀʟɪᴅ ᴍᴏɴɢᴏᴅʙ ᴜʀʟ ꜰᴏʀᴍᴀᴛ 💔**\n\n**⋟ ᴄʜᴇᴄᴋ ʙʏ :– {ISTKHAR.mention}**",
            reply_markup=ADD_ME_BUTTON
        )

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (suraj08832) 😎

# 🧑‍💻 Developer : t.me/brahix
# 🔗 Source link : GitHub.com/suraj08832/ISTKHARli-MusicV2
# 📢 Telegram channel : t.me/about_brahix
# =======================================================
