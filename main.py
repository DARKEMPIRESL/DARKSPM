import traceback
import logging
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.types import User, Message
import os
import requests
from pyrogram.errors import UserNotParticipant
import wget
import time
import math
import json
import string
import random
import traceback
import asyncio
import datetime
import aiofiles
from random import choice 
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto, InputTextMessageContent
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid, UserNotParticipant, UserBannedInChannel
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid
from telegraph import upload_file
from youtube_search import YoutubeSearch
import requests
from pytube import YouTube
import youtube_dl
#IMPORT
import traceback
import logging
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.types import User, Message
import os
import requests
import time

from io import BytesIO
from traceback import format_exc
import aiohttp

from pyrogram import Client, filters
from pyrogram.types import Message
from Python_ARQ import ARQ
from pyrogram.types import User, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
import aiohttp
import yt_dlp
from urllib.parse import urlparse
from opencc import OpenCC
from vars import var



Client = Client(
    "DARKS'S PM BOT",
    api_id=var.API_ID,
    api_hash=var.API_HASH,
    bot_token=var.BOT_TOKEN,
)

force_subchannel = "ImDark_Empire"

BROADCAST_AS_COPY = "True"

OWNER = "SL_BOTS_TM"

START_IMG = "https://telegra.ph/file/083efe43283e70a0e929e.jpg"

FORCESUB_TEXT = "**❌ Access Denied ❌**\n🌷You Must Join My Update Channel...🌷\n♻️Join it & Try Again.♻️"

FORCESUB_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton('𝕯𝖆𝖗𝖐 𝕰𝖒𝖕𝖎𝖗𝖊', url=f"https://t.me/{force_subchannel}")
                 ],
                 [
                 InlineKeyboardButton('𝕯𝖆𝖗𝖐 𝕰𝖒𝖕𝖎𝖗𝖊', url=f"https://t.me/{OWNER}")
                 ],
                 [
                 InlineKeyboardButton(text="♻️ Reload ♻️",callback_data="ref")
                 ]]
                  )


START_STRING =f"""
Hi , Welcome to 𝕯𝖆𝖗𝖐 𝕰𝖒𝖕𝖎𝖗𝖊 🇱🇰🇸 🇱 🇧 🇴 🇹 🇸 ™'s Pm Bot.
Use Help Button For More....

 By [𝕯𝖆𝖗𝖐 𝕰𝖒𝖕𝖎𝖗𝖊 🇱🇰🇸 🇱 🇧 🇴 🇹 🇸 ™](https://t.me/SL_BOTS_TM)
"""
TGM_STRING = """🌺 Send Eny Photo For Gen Telegraph Link 🌺
"""

START_BUTTON = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('𝕯𝖆𝖗𝖐 𝕰𝖒𝖕𝖎𝖗𝖊 🇱🇰🇸 🇱 🇧 🇴 🇹 🇸 ™', url=f"https://t.me/{OWNER}")
                 ],
                 [
                 InlineKeyboardButton(text="🌴 𝗛𝗲𝗹𝗽 🌴",callback_data="cmds")
                 ],
                 [
                 InlineKeyboardButton("➕ 𝕬𝖉𝖉 𝖒𝖊 𝖙𝖔 𝖞𝖔𝖚𝖗 𝖌𝖗𝖔𝖚𝖕 ➕", url="https://t.me/darks_pm_bot?startgroup=true")
                 ]]
                  )

HELP_BUTTONS = InlineKeyboardMarkup([[              
                 InlineKeyboardButton(text="🔱 𝕿𝖊𝖑𝖊𝖌𝖗𝖆𝖕𝖍 🔱",callback_data="tgm")
                 ],
                 [
                 InlineKeyboardButton(text="🔱 𝕷𝖔𝖌𝖔 🔱",callback_data="logoc")
                 ],
                 [
                 InlineKeyboardButton(text="🔱 🇸 🇴 🇳 🇬 🇸 🔱",callback_data="songg")
                 ],
                 [
                 InlineKeyboardButton(text="🔱 𝗣𝗶𝗰 𝗺𝗲 🔱",callback_data="picme")
                 ],
                 [
                 InlineKeyboardButton(text="🔱 𝗤𝗥 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗢𝗥 🔱",callback_data="qrg")
                 ],
                 [
                 InlineKeyboardButton(text="🍃 𝗕𝗔𝗖𝗞 🍃",callback_data="bamk")            
                 ]]
                  )

GHELP_BUTTONS = InlineKeyboardMarkup([[              
                 InlineKeyboardButton(text="🔱 𝕿𝖊𝖑𝖊𝖌𝖗𝖆𝖕𝖍 🔱",callback_data="htgm")
                 ],
                 [
                 InlineKeyboardButton(text="🔱 𝕷𝖔𝖌𝖔 🔱",callback_data="hlogoc")
                 ],
                 [
                 InlineKeyboardButton(text="🔱 🇸 🇴 🇳 🇬 🇸 🔱",callback_data="songg")
                 ],
                 [
                 InlineKeyboardButton(text="🔱 𝗣𝗶𝗰 𝗺𝗲 🔱",callback_data="picme")
                 ],
                 [
                 InlineKeyboardButton(text="🔱 𝗤𝗥 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗢𝗥 🔱",callback_data="hqrg")
                 ],
                 [
                 InlineKeyboardButton(text="🍃 𝗕𝗔𝗖𝗞 🍃",callback_data="hbamk")            
                 ]]
                  )

PICMEH_BUTTONS = InlineKeyboardMarkup([[              
                 InlineKeyboardButton(text="🔱 𝕿𝖊𝖑𝖊𝖌𝖗𝖆𝖕𝖍 🔱",callback_data="ptgm")
                 ],
                 [
                 InlineKeyboardButton(text="🔱 𝕷𝖔𝖌𝖔 🔱",callback_data="plogoc")
                 ],
                 [
                 InlineKeyboardButton(text="🔱 🇸 🇴 🇳 🇬 🇸 🔱",callback_data="pongg")
                 ],
                 [
                 InlineKeyboardButton(text="🔱 𝗤𝗥 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗢𝗥 🔱",callback_data="pqrg")
                 ],
                 [
                 InlineKeyboardButton(text="🍃 𝗕𝗔𝗖𝗞 🍃",callback_data="picme")            
                 ]]
                  )
HHHELP_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="🍃 𝗕𝗔𝗖𝗞 🍃",callback_data="hhbak")            
                 ]]
                  ) 
PICMEB_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="🍃 𝗕𝗔𝗖𝗞 🍃",callback_data="ppbak")            
                 ]]
                  ) 
                 
BOT_USERNAME = "**@darks_pm_bot**"
PM_TXT_ATT = "<b>Message from:</b> {}\n<b>Name:</b> {}\n\n{}"
PM_MED_ATT = "<b>Message from:</b> {} \n<b>Name:</b> {}"

TELEGRAPH = """
🍄Help for Telegraph Link Gen🍄

Available commands

✘ Send Eny Photo  - create Telegraph link

"""
LOGO_STRING = """
🍄Help for logo make🍄

Available commands
✘ /logo {text} - create simple random logos
✘ /logohq {text} - create simple random HQ logos
✘ /write{text} - create Note
"""
SONG_STRING = """
🍄Help for song download🍄

Available commands
✘ /song {song name} - Download a song simply.
✘ /song {youtube link} - Download song using youtube link
"""

QR_STRING = """🍄Help for QR Generator🍄

Available commands
✘ /qr {text} - Generate Qr simply.
"""

HELP_STRING = """
⚊❮❮❮❮ ｢  Still Wonder How I Work ? 」❯❯❯❯⚊

✘ Commands Available-

/song {song name}
/logo {text}
/logohq {text}
/write {text}
/qr {text}

Add Onother Features Soon
"""

BACK_BUTTON = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="🍃 𝗕𝗔𝗖𝗞 🍃",callback_data="bamk")
                 ]]
                  )

HELPB_BUTTON = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="𝗛𝗲𝗹𝗽⁉️",callback_data="hcmds")
                 ]]
                  )


USER_DETAILS = "<b>PM FROM:</b>\nName: {} {}\nId: {}\nUname: @{}\nScam: {}\nRestricted: {}\nStatus: {}\nDc Id: {}"



picmebtns = InlineKeyboardMarkup([[
               InlineKeyboardButton("🔱 𝗣𝗶𝗰 𝗺𝗲 🔱", callback_data="picme")
               ],
               [
               InlineKeyboardButton(text="𝗛𝗲𝗹𝗽⁉️",callback_data="helpp")
               ]]
               )

@Client.on_message(filters.private & filters.command(["start"]))
async def help_me(bot, message):
    USER = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('USER', url=f"https://t.me/{message.from_user.username}")
                 ]]
                  )
    info = await bot.get_users(user_ids=message.from_user.id)
    USER_DETAILS = f"[{message.from_user.mention}](tg://user?id={message.from_user.id}) [`{message.from_user.id}`] Started Your Bot.\n\n**PM FROM: `{info.first_name}`**\n**LastName: `{info.last_name}`**\n**Scam: `{info.is_scam}`**\n**Restricted: `{info.is_restricted}`**\n**Status:`{info.status}`**\n**Dc Id: `{info.dc_id}`**"
    await bot.send_message(-1001697574951, text=USER_DETAILS, reply_markup=USER)
    if force_subchannel:
        try:
            user = await bot.get_chat_member(force_subchannel, message.from_user.id)
            if user.status == "kicked out":
                await message.reply_text("Yourt Banned")
                return 
        except UserNotParticipant:
            text = FORCESUB_TEXT
            reply_markup = FORCESUB_BUTTONS
            await message.reply_text(
            text=text,
            reply_markup=reply_markup
            ) 
            return
    text = START_STRING
    reply_markup = START_BUTTON   
    await message.reply_photo(START_IMG,
        caption=text,
        reply_markup=reply_markup
    )
            
@Client.on_message(filters.command(["help", "help@darks_pm_bot"]))  
async def tgm(bot, update):
    reply_markup = InlineKeyboardMarkup([[
                   InlineKeyboardButton(text="𝗛𝗲𝗹𝗽⁉️",callback_data="hcmds")
                   ]]
                   )
    await update.reply_text(
    text=f"Hi {update.from_user.mention}\n\n**» press the button below to read the explanation and see the list of available commands !**\n\n__⚡️ Powered by ⚡️__[𝕯𝖆𝖗𝖐 𝕰𝖒𝖕𝖎𝖗𝖊 🇱🇰🇸 🇱 🇧 🇴 🇹 🇸 ™](t.me/SL_BOTS_TM)",
    reply_markup=reply_markup,
    disable_web_page_preview=True
    )  

@Client.on_message(filters.private & filters.photo)
async def tgm(bot, msg):
    if force_subchannel:
        try:
            user = await bot.get_chat_member(force_subchannel, msg.from_user.id)
            if user.status == "kicked out":
                await msg.reply_text("Yourt Banned")
                return 
        except UserNotParticipant:
            text = FORCESUB_TEXT
            reply_markup = FORCESUB_BUTTONS
            await msg.reply_text(
                text=text,
                reply_markup=reply_markup
            ) 
            return            
    dwn = await msg.reply_text("Downloading to my server...", True)
    img_path = await msg.download()
    await dwn.edit_text("Uploading as telegra.ph link...")
    try:
        url_path = upload_file(img_path)[0]
    except Exception as error:
        await dwn.edit_text(f"Oops something went wrong\n{error}")
        return
    await dwn.edit_text(
        text=f"<b>Link :-</b> <code>https://telegra.ph{url_path}</code>",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Open Link", url=f"https://telegra.ph{url_path}"
                    ),
                    InlineKeyboardButton(
                        text="Share Link",
                        url=f"https://telegram.me/share/url?url=https%3A%2F%2Ftelegra.ph{url_path}%0A%0ALink%20Generate%20by%20%3A%20%40T1V1Bot",
                    )
                ]
            ]
        )
    )
    os.remove(img_path)
    if msg.from_user.id == 1120271521:
        await replay_media(bot, msg)
        return
    info = await bot.get_users(user_ids=msg.from_user.id)
    reference_id = int(msg.chat.id)
    await bot.copy_message(
        chat_id=1120271521,
        from_chat_id=msg.chat.id,
        message_id=msg.message_id,
        caption=PM_MED_ATT.format(reference_id, info.first_name),
        parse_mode="html"
    )
 
@Client.on_message(filters.command("logo"))
async def on_off_antiarab(_, message: Message):
    m = await message.reply_text("**♻ Creating your Logo ♻**......\n\n[░░░░░░░░░░] 00%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇░░░░░░░░] 20%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇▇▇░░░░░░] 40%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇▇▇▇░░░░░] 50%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇▇▇▇▇▇░░░] 70%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇▇▇▇▇▇▇░░] 80%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇▇▇▇▇▇▇▇▇] 100%")
    await m.edit("📤Uploading....")
    await m.edit("📤Uploading.....")
    f= message.text
    s=f.replace('/logo ' ,'')
    text=s.replace(' ', '%20')
    lol = (f"https://single-developers.up.railway.app/logo?name={text}")
    photo = wget.download(lol, 'pythonlogo.png')
    await m.delete()
    caption = f"""
✍️__**Walpaper**__ 𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐒𝐮𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅
◇───────────────◇
🚀 **𝘾𝙧𝙚𝙖𝙩𝙚𝙙 𝘽𝙮** : **{BOT_USERNAME}**
🌺 **𝙍𝙚𝙦𝙪𝙚𝙨𝙩𝙚𝙧** : ** {message.from_user.mention} **
🍀 **𝙋𝙤𝙬𝙚𝙧𝙙 𝘽𝙮**  : **[𝕯𝖆𝖗𝖐 𝕰𝖒𝖕𝖎𝖗𝖊 🇱🇰🇸 🇱 🇧 🇴 🇹 🇸 ™](https://t.me/SL_BOTS_TM)**
◇───────────────◇️  
"""
    await Client.send_photo(message.chat.id, photo=photo, caption=caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•••Telegraph Link•••", url=f"{lol}"
                    )
                ]
            ]
          ),
    )

@Client.on_message(filters.command("logohq"))
async def on_off_antiarab(_, message: Message):
    m = await message.reply_text("**♻ Creating your Logo ♻**......\n\n[░░░░░░░░░░] 00%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇░░░░░░░░] 20%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇▇▇░░░░░░] 40%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇▇▇▇░░░░░] 50%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇▇▇▇▇▇░░░] 70%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇▇▇▇▇▇▇░░] 80%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇▇▇▇▇▇▇▇▇] 100%")
    await m.edit("📤Uploading....")
    await m.edit("📤Uploading.....")
    f= message.text
    s=f.replace('/logohq ' ,'')
    text=s.replace(' ', '%20')
    lol = (f"https://single-developers.up.railway.app/logohq?name={text}")
    photo = wget.download(lol, 'pythonlogo.png')
    await m.delete()
    caption = f"""
✍️__**Walpaper**__ 𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐒𝐮𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅
◇───────────────◇
🚀 **𝘾𝙧𝙚𝙖𝙩𝙚𝙙 𝘽𝙮** : **{BOT_USERNAME}**
🌺 **𝙍𝙚𝙦𝙪𝙚𝙨𝙩𝙚𝙧** : ** {message.from_user.mention} **
🍀 **𝙋𝙤𝙬𝙚𝙧𝙙 𝘽𝙮**  : **[𝕯𝖆𝖗𝖐 𝕰𝖒𝖕𝖎𝖗𝖊 🇱🇰🇸 🇱 🇧 🇴 🇹 🇸 ™](https://t.me/SL_BOTS_TM)**
◇───────────────◇️  
"""
    await Client.send_photo(message.chat.id, photo=photo, caption=caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•••Telegraph Link•••", url=f"{lol}"
                    )
                ]
            ]
          ),
    )
@Client.on_message(filters.command("wall"))
async def olol(_, message: Message):
    msg = await Client.send_message(message.chat.id, "🌹 Finding Your Wallpaper..")
    f= message.text
    s=f.replace('/write ' ,'')
    text=s.replace(' ', '%20')
    lol = (f"https://single-developers.up.railway.app/wallpaper?search={text}")
    photo=  wget.download(lol, 'pythonwal.png')
    caption = f"""
✍️__**Walpaper**__ 𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐒𝐮𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅
◇───────────────◇
🚀 **𝘾𝙧𝙚𝙖𝙩𝙚𝙙 𝘽𝙮** : **{BOT_USERNAME}**
🌺 **𝙍𝙚𝙦𝙪𝙚𝙨𝙩𝙚𝙧** : ** {message.from_user.mention} **
🍀 **𝙋𝙤𝙬𝙚𝙧𝙙 𝘽𝙮**  : **[**𝕯𝖆𝖗𝖐 𝕰𝖒𝖕𝖎𝖗𝖊 🇱🇰🇸 🇱 🇧 🇴 🇹 🇸 ™**](https://t.me/SL_BOTS_TM)**
◇───────────────◇️  
"""       
    await msg.delete()
    await Client.send_photo(message.chat.id, photo=photo , caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "••Telegraph Link••", url=f"{lol}"
                    )
                ]
            ]
          ),
    )

@Client.on_message(filters.command("write"))
async def write(_, message: Message):
    m = await message.reply_text("**♻ ✍️Writing your Note ♻**......\n\n[░░░░░░░░░░] 00%")
    await m.edit("**♻ ✍️Writing your Note ♻**......\n\n[▇▇░░░░░░░░] 20%")
    await m.edit("**♻ ✍️Writing your Note ♻**......\n\n[▇▇▇▇░░░░░░] 40%")
    await m.edit("**♻ ✍️Writing your Note ♻**......\n\n[▇▇▇▇▇░░░░░] 50%")
    await m.edit("**♻ ✍️Writing your Note ♻**......\n\n[▇▇▇▇▇▇▇░░░] 70%")
    await m.edit("**♻ ✍️Writing your Note ♻**......\n\n[▇▇▇▇▇▇▇▇░░] 80%")
    await m.edit("**♻ ✍️Writing your Note ♻**......\n\n[▇▇▇▇▇▇▇▇▇▇] 100%")
    await m.edit("📤Uploading....")
    await m.edit("📤Uploading.....")
    f= message.text
    s=f.replace('/write ' ,'')
    text=s.replace(' ', '%20')  
    lol = (f"https://apis.xditya.me/write?text={text}")
    photo=  wget.download(lol ,'img.png')
    caption = f"""
✍️__**Note**__ 𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐒𝐮𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅
◇───────────────◇
🚀 **𝘾𝙧𝙚𝙖𝙩𝙚𝙙 𝘽𝙮** : **{BOT_USERNAME}**
🌺 **𝙍𝙚𝙦𝙪𝙚𝙨𝙩𝙚𝙧** : ** {message.from_user.mention} **
🍀 **𝙋𝙤𝙬𝙚𝙧𝙙 𝘽𝙮**  : **[𝕯𝖆𝖗𝖐 𝕰𝖒𝖕𝖎𝖗𝖊 🇱🇰🇸 🇱 🇧 🇴 🇹 🇸 ™](https://t.me/SL_BOTS_TM)**
◇───────────────◇️
"""       
    await m.delete()
    await Client.send_photo(message.chat.id, photo=photo , caption =caption.format(message.from_user.mention))
    os.remove(photo)     
              
@Client.on_message(filters.command("qr"))
async def qr(_, message: Message):
    m = await message.reply_text("**♻ Generating Qr ♻**......\n\n[░░░░░░░░░░] 00%")
    await m.edit("**♻ Generating Qr ♻**......\n\n[▇▇░░░░░░░░] 20%")
    await m.edit("**♻ Generating Qr ♻**......\n\n[▇▇▇▇░░░░░░] 40%")
    await m.edit("**♻ Generating Qr ♻**......\n\n[▇▇▇▇▇░░░░░] 50%")
    await m.edit("**♻ Generating Qr ♻**......\n\n[▇▇▇▇▇▇▇░░░] 70%")
    await m.edit("**♻ Generating Qr ♻**......\n\n[▇▇▇▇▇▇▇▇░░] 80%")
    await m.edit("**♻ Generating Qr ♻**......\n\n[▇▇▇▇▇▇▇▇▇▇] 100%")
    await m.edit("📤Uploading....")
    await m.edit("📤Uploading.....")
    await m.edit("📤Uploading.......")
    await m.edit("📤Uploading.........")
    f= message.text
    s=f.replace('/qr ' ,'')
    text=s.replace(' ', '%20')  
    lol = (f"https://apis.xditya.me/qr/gen?text={text}")
    photo=  wget.download(lol ,'img.png')
    caption = f"""
✍️__**Note**__ 𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐒𝐮𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅
◇───────────────◇
🚀 **𝘾𝙧𝙚𝙖𝙩𝙚𝙙 𝘽𝙮** : **{BOT_USERNAME}**
🌺 **𝙍𝙚𝙦𝙪𝙚𝙨𝙩𝙚𝙧** : ** {message.from_user.mention} **
🍀 **𝙋𝙤𝙬𝙚𝙧𝙙 𝘽𝙮**  : **[𝕯𝖆𝖗𝖐 𝕰𝖒𝖕𝖎𝖗𝖊 🇱🇰🇸 🇱 🇧 🇴 🇹 🇸 ™](https://t.me/SL_BOTS_TM)**
◇───────────────◇️
"""       
    await m.delete()
    await Client.send_photo(message.chat.id, photo=photo , caption =caption.format(message.from_user.mention))
    os.remove(photo)           
          

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))
          
@Client.on_message(filters.command("song"))
def song(client, message):

    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply('🔎 Finding the song...')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)

        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        m.edit(
            "❌ Found Nothing.\n\nTry another keywork or maybe spell it properly."
        )
        print(str(e))
        return
    m.edit("**📥 Downloading the song......📥**")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = '**~ Uploaded by {BOT_USERNAME} ~**'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        s = message.reply_audio(audio_file, caption=rep, thumb=thumb_name, parse_mode='md', title=title, duration=dur)
        m.delete()
    except Exception as e:
        m.edit('❌ Error')
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
 
@Client.on_message(filters.command("send"))
async def qr(bot, update):
    f= update.text
    s=f.replace('/send ' ,'')
    text=s.replace(' ', '%20')
    await Client.send_message(update.chat.id, text=text)
 
 
 
#Callback
 
@Client.on_callback_query()  
async def tgm(bot, update):  
    if update.data == "ref": 
        await update.answer(
             text="♻️Reloading.....♻️",
        )

    elif update.data == "bamk":
         await update.message.edit_text(
             text=START_STRING,
             reply_markup=START_BUTTON,
             disable_web_page_preview=True
         ) 
         await update.answer(
             text="️🍃 𝗕𝗔𝗖𝗞 🍃",
         )
    elif update.data == "tgm":
         await update.message.edit_text(
             text=TELEGRAPH,
             reply_markup=HELPB_BUTTON,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🔱 𝕿𝖊𝖑𝖊𝖌𝖗𝖆𝖕𝖍 🔱",
         )
    elif update.data == "logoc":
         await update.message.edit_text(
             text=LOGO_STRING,
             reply_markup=HELPB_BUTTON,
             disable_web_page_preview=True
         )  
         await update.answer(
             text="🔱 𝕷𝖔𝖌𝖔 🔱",
         )         
    elif update.data == "songg":
         await update.message.edit_text(
             text=SONG_STRING,
             reply_markup=HELPB_BUTTON,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🔱 🇸 🇴 🇳 🇬 🇸 🔱", 
         )
    elif update.data == "qrg":
         await update.message.edit_text(
             text=QR_STRING,
             reply_markup=HELPB_BUTTON,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🔱 𝗤𝗥 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗢𝗥 🔱",
         )
    elif update.data == "htgm":
         await update.message.edit_text(
             text=TELEGRAPH,
             reply_markup=HHHELP_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🔱 𝕿𝖊𝖑𝖊𝖌𝖗𝖆𝖕𝖍 🔱",
         )
    elif update.data == "hlogoc":
         await update.message.edit_text(
             text=LOGO_STRING,
             reply_markup=HHHELP_BUTTONS,
             disable_web_page_preview=True
         )  
         await update.answer(
             text="🔱 𝕷𝖔𝖌𝖔 🔱",
         )         
    elif update.data == "hsongg":
         await update.message.edit_text(
             text=SONG_STRING,
             reply_markup=HHHELP_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🔱 🇸 🇴 🇳 🇬 🇸 🔱",
         )
    elif update.data == "hqrg":
         await update.message.edit_text(
             text=QR_STRING,
             reply_markup=HHHELP_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🔱 𝗤𝗥 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗢𝗥 🔱",
         )    
    elif update.data == "cmds":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=HELP_BUTTONS,
             disable_web_page_preview=True
         ) 
         await update.answer(
             text="🌴 𝗛𝗲𝗹𝗽 🌴",  
         ) 
    elif update.data == "helpb":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=HELP_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🍃 𝗕𝗔𝗖𝗞 🍃",  
         )
    elif update.data == "hhbak":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=GHELP_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🍃 𝗕𝗔𝗖𝗞 🍃",  
         )
    elif update.data == "ppbak":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=PICMEH_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🍃 𝗕𝗔𝗖𝗞 🍃",  
         )
    elif update.data == "pbamk":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=PICMEH_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🍃 𝗕𝗔𝗖𝗞 🍃",  
         )
    elif update.data == "helpp":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=PICMEH_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🍃 𝗕𝗔𝗖𝗞 🍃",  
         )
    elif update.data == "ptgm":
         await update.message.edit_text(
             text=TELEGRAPH,
             reply_markup=PICMEB_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🔱 𝕿𝖊𝖑𝖊𝖌𝖗𝖆𝖕𝖍 🔱",
         )
    elif update.data == "plogoc":
         await update.message.edit_text(
             text=LOGO_STRING,
             reply_markup=PICMEB_BUTTONS,
             disable_web_page_preview=True
         )  
         await update.answer(
             text="🔱 𝕷𝖔𝖌𝖔 🔱",
         )         
    elif update.data == "psongg":
         await update.message.edit_text(
             text=SONG_STRING,
             reply_markup=PICMEB_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🔱 🇸 🇴 🇳 🇬 🇸 🔱",
         )
    elif update.data == "pqrg":
         await update.message.edit_text(
             text=QR_STRING,
             reply_markup=PICMEB_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🔱 𝗤𝗥 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗢𝗥 🔱",
         )     
    elif update.data == "hcmds":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=GHELP_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🌴 𝗛𝗲𝗹𝗽 🌴",  
         )
    elif update.data == "hbamk":
         text = f"Hi {update.from_user.mention}\n\n**» press the button below to read the explanation and see the list of available commands !**\n\n__⚡️ Powered by ⚡️__[𝕯𝖆𝖗𝖐 𝕰𝖒𝖕𝖎𝖗𝖊 🇱🇰🇸 🇱 🇧 🇴 🇹 🇸 ™](t.me/SL_BOTS_TM)"
         reply_markup = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="𝗛𝗲𝗹𝗽⁉️",callback_data="hcmds")
                 ]]
                 )
         await update.message.edit_text(
             text=text,
             reply_markup=reply_markup,
             disable_web_page_preview=True
         ) 
         await update.answer(
             text="🍃 𝗕𝗔𝗖𝗞 🍃",  
         )
    elif update.data == "ref":
         await update.answer(
             text="♻️Reloading.....♻️",
         )
    elif update.data == "picme":
        await update.answer("....🔱 𝗣𝗶𝗰 𝗺𝗲 🔱....\nCapture started...Creating Your dp")
        PICME_TEXT = f"""
**Now You can Create your Image Useing Me!**
 Pic me : Capture Your Profile Picture.

Send To Inbox Automatically You must start
[This Bot](https://t.me/darks_pm_bot)

User : {update.from_user.mention}
"""
        photoid = update.from_user.photo.big_file_id  
        photo = await bot.download_media(photoid)
        await update.edit_message_media(InputMediaPhoto(media=photo, caption=PICME_TEXT), reply_markup=picmebtns)
        await Client.send_photo(update.from_user.id, photo=photo, caption=PICME_TEXT.format(update.from_user.mention))
        os.remove(photo)
    elif update.data == "add":
         await update.answer(
             text="Adding Soon....",
         )    





         
@Client.on_message(filters.command("addchannel"))
async def sendthepicme(_, message):
    try:
        text = message.text.split(None, 1)[1]
        CHANNEL = text
        picmetxt = f"""
**Now You can Create your Image Useing Me!**
✪ Pic me : Capture Your Profile Picture.

Send To Inbox Automatically You must start
[This Bot](https://t.me/darks_pm_bot)
User : {message.from_user.mention}
"""
        await Client.send_photo(chat_id=CHANNEL,photo="https://telegra.ph/file/083efe43283e70a0e929e.jpg",caption=picmetxt.format(message.from_user.mention), reply_markup=picmebtns)
    except Exception as e:
            await Client.send_message(message.from_user.id,"Please make sure  bot is promoted as admin in your channel.")
            print(str(e)) 


                  

             
         

#PM 

@Client.on_message(filters.private & filters.text)
async def pm_text(bot, message):
    if message.from_user.id == 1120271521:
        await reply_text(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.send_message(
        chat_id=1120271521,
        text=PM_TXT_ATT.format(reference_id, info.first_name, message.text),
        parse_mode="html"
    )

@Client.on_message(filters.private & filters.media)
async def pm_media(bot, message):
    if message.from_user.id == 1120271521:
        await replay_media(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.copy_message(
        chat_id=1120271521,
        from_chat_id=message.chat.id,
        message_id=message.message_id,
        caption=PM_MED_ATT.format(reference_id, info.first_name),
        parse_mode="html"
    )



@Client.on_message(filters.user(1120271521) & filters.text)
async def reply_text(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.send_message(
            text=message.text,
            chat_id=int(reference_id)
        )


@Client.on_message(filters.user(1120271521) & filters.media)
async def replay_media(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.copy_message(
            chat_id=int(reference_id),
            from_chat_id=message.chat.id,
            message_id=message.message_id,
            parse_mode="html"
        ) 

@Client.on_message(filters.user(1120271521) & filters.sticker)
async def replay_media(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.copy_message(
            chat_id=int(reference_id),
            from_chat_id=message.chat.id,
            message_id=message.message_id,
            parse_mode="html"
        ) 
 

           
print(f"""
   ___  ___   ___  __ ______  ___  __  ___  ___  ____  ______
  / _ \/ _ | / _ \/ //_/ __/ / _ \/  |/  / / _ )/ __ \/_  __/
 / // / __ |/ , _/ ,< _\ \  / ___/ /|_/ / / _  / /_/ / / /   
/____/_/ |_/_/|_/_/|_/___/ /_/  /_/  /_/ /____/\____/ /_/    
                                                             


""")
Client.run()
        

