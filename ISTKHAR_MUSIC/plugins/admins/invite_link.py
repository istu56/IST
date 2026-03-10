# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (suraj08832) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @brahix
# =======================================================

import os
import csv
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from ISTKHAR_MUSIC import app
from ISTKHAR_MUSIC.misc import SUDOERS
from ISTKHAR_MUSIC.utils.ISTKHAR_BAN import admin_filter


ADD_BUTTON = InlineKeyboardMarkup(
    [[InlineKeyboardButton("✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙", url="https://t.me/YourBotUsername?startgroup=true")]]
)


@app.on_message(filters.command("users") & admin_filter)
async def user_command(client: Client, message: Message):
    members_list = []
    async for member in client.get_chat_members(message.chat.id):
        members_list.append({
            "username": member.user.username,
            "userid": member.user.id
        })

    file_name = "members.txt"
    with open(file_name, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["username", "userid"])
        writer.writeheader()
        for member in members_list:
            writer.writerow(member)

    await client.send_document(
        message.chat.id,
        file_name,
        caption=f"**⋟ ᴇxᴘᴏʀᴛᴇᴅ ʙʏ :- {app.mention}**",
        reply_markup=ADD_BUTTON
    )

    if os.path.exists(file_name):
        os.remove(file_name)


@app.on_message(filters.command("givelink"))
async def give_link_command(client: Client, message: Message):
    link = await client.export_chat_invite_link(message.chat.id)
    await message.reply_text(
        f"**⋟ ᴄʜᴀᴛ ɪɴᴠɪᴛᴇ ʟɪɴᴋ :- [ʟɪɴᴋ]({link})**\n\n**⋟ ʙʏ :- {app.mention}**",
        reply_markup=ADD_BUTTON,
        disable_web_page_preview=True 
    )


@app.on_message(
    filters.command(
        ["link", "invitelink"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]
    ) & filters.user(list(SUDOERS))
)
async def link_command_handler(client: Client, message: Message):
    if len(message.command) != 2:
        await message.reply("**⋟ ɪɴᴠᴀʟɪᴅ ᴜsᴀɢᴇ :-** `/link group_id`", disable_web_page_preview=True)
        return

    group_id = message.command[1]
    file_name = f"group_info_{group_id}.txt"

    try:
        chat = await client.get_chat(int(group_id))
        if chat is None:
            await message.reply("**⋟ ᴜɴᴀʙʟᴇ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.**", disable_web_page_preview=True)
            return

        try:
            invite_link = await client.export_chat_invite_link(chat.id)
        except FloodWait as e:
            await message.reply(f"**⋟ ғʟᴏᴏᴅᴡᴀɪᴛ** `{e.x}` **sᴇᴄᴏɴᴅs**", disable_web_page_preview=True)
            return

        group_data = {
            "id": chat.id,
            "type": str(chat.type),
            "title": chat.title,
            "members_count": chat.members_count,
            "description": chat.description,
            "invite_link": invite_link,
            "is_verified": chat.is_verified,
            "is_restricted": chat.is_restricted,
            "is_creator": chat.is_creator,
            "is_scam": chat.is_scam,
            "is_fake": chat.is_fake,
            "dc_id": chat.dc_id,
            "has_protected_content": chat.has_protected_content,
        }

        with open(file_name, "w", encoding="utf-8") as file:
            for key, value in group_data.items():
                file.write(f"{key}: {value}\n")

        await client.send_document(
    chat_id=message.chat.id,
    document=file_name,
    caption=(
        f"**✦ ɢʀᴏᴜᴘ ɪɴғᴏʀᴍᴀᴛɪᴏɴ**\n\n"
        f"**✦ ᴛɪᴛʟᴇ :-** {chat.title}\n"
        f"**✦ ᴍᴇᴍʙᴇʀs :-** `{chat.members_count}`\n"
        f"**✦ ʟɪɴᴋ :-** [ᴄʟɪᴄᴋ ʜᴇʀᴇ]({invite_link})\n\n"
        f"**✦ ʙʏ :- {app.mention}**"
    ),
    reply_markup=ADD_BUTTON
)

    except Exception as e:
        await message.reply(f"**⋟ ᴇʀʀᴏʀ :-** {str(e)}", disable_web_page_preview=True)

    finally:
        if os.path.exists(file_name):
            os.remove(file_name)

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (suraj08832) 😎

# 🧑‍💻 Developer : t.me/brahix
# 🔗 Source link : GitHub.com/suraj08832/ISTKHARli-MusicV2
# 📢 Telegram channel : t.me/about_brahix
# =======================================================
