# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (suraj08832) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @brahix
# =======================================================

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ISTKHAR_MUSIC import app
import config
from ISTKHAR_MUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**<u>❃ brahix ʙᴏᴛs ʀєᴘσs ❃</u>

✼ ʀєᴘᴏ ɪs ηᴏᴡ ᴘʀɪᴠᴧᴛє ᴅᴜᴅє 😌
 
❉  ʏᴏᴜ ᴄᴧη мʏ ᴜsє ᴘᴜʙʟɪᴄ ʀєᴘσs !! 

✼ || ɢɪᴛ :-  [ᴧʟᴘʜᴧ-ʙᴧʙʏ](https://github.com/TEAMPURVI) ||
 
❊ ʀᴜη 24x7 ʟᴧɢ ϝʀєє ᴡɪᴛʜσᴜᴛ sᴛσᴘ**
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
    [
        InlineKeyboardButton("• brahix ᴍᴜsɪᴄ •", url="https://github.com/TEAMPURVI/PURVI_MUSIC"),
        InlineKeyboardButton("• sᴏɴᴀʟɪ ᴍᴜsɪᴄ •", url="https://github.com/TEAMPURVI/ISTKHAR_MUSIC")
    ],
    [
        InlineKeyboardButton("• sɪᴍᴘʟᴇ ᴍᴜsɪᴄ •", url="https://github.com/TEAMPURVI/ALPHA_MUSIC"),
        InlineKeyboardButton("• ᴄʜᴀᴛ ʙᴏᴛ •", url="https://github.com/TEAMPURVI/PURVI_CHAT")
    ],
    [
        InlineKeyboardButton("• ᴜsᴇʀ ʙᴏᴛ •", url="https://github.com/TEAMPURVI/ALPHA_USERBOT"),
        InlineKeyboardButton("• sᴘᴀᴍ ʙᴏᴛ •", url="https://github.com/TEAMPURVI/ALPHA_SPAM")
    ],
    [
        InlineKeyboardButton("• sᴇssɪᴏɴ ʙᴏᴛ •", url="https://github.com/TEAMPURVI/PURVI_STRING"),
        InlineKeyboardButton("• sᴇssɪᴏɴ ʜᴀᴄᴋ •", url="https://github.com/TEAMPURVI/STRING_HACK")
    ],
    [
        InlineKeyboardButton("• ʙᴀɴᴀʟʟ ʙᴏᴛ •", url="https://github.com/TEAMPURVIALPHA_BANALL"),
        InlineKeyboardButton("• ᴀɴʏ ɪssᴜᴇ •", user_id=config.OWNER_ID)
    ],
    [
        InlineKeyboardButton("✙ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✙", url=f"https://t.me/{app.username}?startgroup=true")
    ]
]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/kbi6t5.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (suraj08832) 😎

# 🧑‍💻 Developer : t.me/brahix
# 🔗 Source link : GitHub.com/suraj08832/ISTKHARli-MusicV2
# 📢 Telegram channel : t.me/about_brahix
# =======================================================
