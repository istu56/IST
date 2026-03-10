# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (suraj08832) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @brahix
# =======================================================

from pyrogram import enums
from pyrogram.enums import ChatType
from pyrogram import filters, Client
from ISTKHAR_MUSIC import app
from config import OWNER_ID
from pyrogram.types import Message
from ISTKHAR_MUSIC.utils.ISTKHAR_BAN import admin_filter
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton



# ------------------------------------------------------------------------------- #


@app.on_message(filters.command("pin") & admin_filter)
async def pin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("**» ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋs ᴏɴʟʏ ᴏɴ ɢʀᴏᴜᴘs !**")
    elif not replied:
        await message.reply_text("**» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴘɪɴ ɪᴛ !**")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.pin()
                await message.reply_text(f"**» sᴜᴄᴄᴇssғᴜʟʟʏ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇ!**\n\n**» ᴄʜᴀᴛ :-** {chat_title}\n**» ᴀᴅᴍɪɴ :-** {name}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" 📝 ᴠɪᴇᴡs ᴍᴇssᴀɢᴇ ", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))


@app.on_message(filters.command("pinned"))
async def pinned(_, message):
    chat = await app.get_chat(message.chat.id)
    if not chat.pinned_message:
        return await message.reply_text("**» ɴᴏ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇ ғᴏᴜɴᴅ**")
    try:        
        await message.reply_text("» ʜᴇʀᴇ ɪs ᴛʜᴇ ʟᴀᴛᴇsᴛ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇ",reply_markup=
        InlineKeyboardMarkup([[InlineKeyboardButton(text="📝 ᴠɪᴇᴡ ᴍᴇssᴀɢᴇ",url=chat.pinned_message.link)]]))  
    except Exception as er:
        await message.reply_text(er)


# ------------------------------------------------------------------------------- #

@app.on_message(filters.command("unpin") & admin_filter)
async def unpin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("**» ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋs ᴏɴʟʏ ᴏɴ ɢʀᴏᴜᴘs !**")
    elif not replied:
        await message.reply_text("**» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴜɴᴘɪɴ ɪᴛ !**")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.unpin()
                await message.reply_text(f"**» sᴜᴄᴄᴇssғᴜʟʟʏ ᴜɴᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇ!**\n\n**» ᴄʜᴀᴛ :-** {chat_title}\n**» ᴀᴅᴍɪɴ :-** {name}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" 📝 ᴠɪᴇᴡs ᴍᴇssᴀɢᴇ ", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))




# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["removephoto", "rmphoto", "photoremove"]) & admin_filter)
async def deletechatphoto(_, message):
      
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("**» ᴘʀᴏᴄᴇssɪɴɢ....**")
      admin_check = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("**» ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋ ᴏɴ ɢʀᴏᴜᴘs !**") 
      try:
         if admin_check.privileges.can_change_info:
             await app.delete_chat_photo(chat_id)
             await msg.edit("**» sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇᴍᴏᴠᴇᴅ ᴘʀᴏғɪʟᴇ ᴘʜᴏᴛᴏ ғʀᴏᴍ ɢʀᴏᴜᴘ !**\n**» ʙʏ :- {}**".format(message.from_user.mention))    
      except:
          await msg.edit("**» ᴛʜᴇ ᴜsᴇʀ ᴍᴏsᴛ ɴᴇᴇᴅ ᴄʜᴀɴɢᴇ ɪɴғᴏ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ᴛᴏ ʀᴇᴍᴏᴠᴇ ɢʀᴏᴜᴘ ᴘʜᴏᴛᴏ !**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["setphoto", "setph", "photoset"]) & admin_filter)
async def setchatphoto(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("**» ᴘʀᴏᴄᴇssɪɴɢ...**")
      admin_check = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("**» ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋ ᴏɴ ɢʀᴏᴜᴘs !**") 
      elif not reply:
           await msg.edit("**» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴏʀ ᴅᴏᴄᴜᴍᴇɴᴛ.**")
      elif reply:
          try:
             if admin_check.privileges.can_change_info:
                photo = await reply.download()
                await message.chat.set_photo(photo=photo)
                await msg.edit_text("**» sᴜᴄᴄᴇssғᴜʟʟʏ ɴᴇᴡ ᴘʀᴏғɪʟᴇ ᴘʜᴏᴛᴏ ɪɴsᴇʀᴛ !**\n» ʙʏ :- {}**".format(message.from_user.mention))
             else:
                await msg.edit("**» sᴏᴍᴇᴛʜɪɴɢ ᴡʀᴏɴɢ ʜᴀᴘᴘᴇɴᴇᴅ ᴛʀʏ ᴀɴᴏᴛʜᴇʀ ᴘʜᴏᴛᴏ !**")
     
          except:
              await msg.edit("**» ᴛʜᴇ ᴜsᴇʀ ᴍᴏsᴛ ɴᴇᴇᴅ ᴄʜᴀɴɢᴇ ɪɴғᴏ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ᴛᴏ ᴄʜᴀɴɢᴇ ɢʀᴏᴜᴘ ᴘʜᴏᴛᴏ !**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["settitle","settit","setname"]) & admin_filter)
async def setgrouptitle(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("**» ᴘʀᴏᴄᴇssɪɴɢ...**")
    if message.chat.type == enums.ChatType.PRIVATE:
          await msg.edit("**» ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋ ᴏɴ ɢʀᴏᴜᴘs !**")
    elif reply:
          try:
            title = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("**» sᴜᴄᴄᴇssғᴜʟʟʏ ɴᴇᴡ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ɪɴsᴇʀᴛ !**\n» ʙʏ :- {}**".format(message.from_user.mention))
          except AttributeError:
                await msg.edit("**» ᴛʜᴇ ᴜsᴇʀ ᴍᴏsᴛ ɴᴇᴇᴅ ᴄʜᴀɴɢᴇ ɪɴғᴏ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ᴛᴏ ᴄʜᴀɴɢᴇ ɢʀᴏᴜᴘ ᴛɪᴛʟᴇ !**")   
    elif len(message.command) >1:
        try:
            title = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("**» sᴜᴄᴄᴇssғᴜʟʟʏ ɴᴇᴡ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ɪɴsᴇʀᴛ !**\n**» ʙʏ :- {}**".format(message.from_user.mention))
        except AttributeError:
               await msg.edit("**» ᴛʜᴇ ᴜsᴇʀ ᴍᴏsᴛ ɴᴇᴇᴅ ᴄʜᴀɴɢᴇ ɪɴғᴏ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ᴛᴏ ᴄʜᴀɴɢᴇ ɢʀᴏᴜᴘ ᴛɪᴛʟᴇ !**")
          

    else:
       await msg.edit("**» ʏᴏᴜ ɴᴇᴇᴅ ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴄʜᴀɴɢᴇ ɢʀᴏᴜᴘ ᴛɪᴛʟᴇ **")


# --------------------------------------------------------------------------------- #



@app.on_message(filters.command(["setdiscription","setdis","setbio"]) & admin_filter)
async def setg_discription(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("**» ᴘʀᴏᴄᴇssɪɴɢ...**")
    if message.chat.type == enums.ChatType.PRIVATE:
        await msg.edit("**» ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋs ᴏɴ ɢʀᴏᴜᴘs!**")
    elif reply:
        try:
            discription = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("**» sᴜᴄᴄᴇssғᴜʟʟʏ ɴᴇᴡ ɢʀᴏᴜᴘ ᴅɪsᴄʀɪᴘᴛɪᴏɴ ɪɴsᴇʀᴛ!**\n**» ʙʏ :- {}**".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("**» ᴛʜᴇ ᴜsᴇʀ ᴍᴜsᴛ ʜᴀᴠᴇ ᴄʜᴀɴɢᴇ ɪɴғᴏ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ᴛᴏ ᴄʜᴀɴɢᴇ ɢʀᴏᴜᴘ ᴅɪsᴄʀɪᴘᴛɪᴏɴ!**")   
    elif len(message.command) > 1:
        try:
            discription = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("**» sᴜᴄᴄᴇssғᴜʟʟʏ ɴᴇᴡ ɢʀᴏᴜᴘ ᴅɪsᴄʀɪᴘᴛɪᴏɴ ɪɴsᴇʀᴛ!**\n**» ʙʏ :- {}**".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("**» ᴛʜᴇ ᴜsᴇʀ ᴍᴜsᴛ ʜᴀᴠᴇ ᴄʜᴀɴɢᴇ ɪɴғᴏ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ᴛᴏ ᴄʜᴀɴɢᴇ ɢʀᴏᴜᴘ ᴅɪsᴄʀɪᴘᴛɪᴏɴ!**")
    else:
        await msg.edit("**» ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴄʜᴀɴɢᴇ ɢʀᴏᴜᴘ ᴅɪsᴄʀɪᴘᴛᴏɴ!**")


# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (suraj08832) 😎

# 🧑‍💻 Developer : t.me/brahix
# 🔗 Source link : GitHub.com/suraj08832/ISTKHARli-MusicV2
# 📢 Telegram channel : t.me/about_brahix
# =======================================================
