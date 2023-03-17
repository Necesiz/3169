import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon import events, Button
from telethon.tl.custom import Button
import random # pip install random
from random import randint
import configparser
from asyncio import sleep
from telethon import events
from telethon import __version__ as s
import asyncio
import os
from Config import Config 
import os, logging, asyncio
from telethon import events, Button
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from asyncio import sleep 
from telethon import Button, events
import speedtest
# Pyrogram----------------------------------------------------------------------------------------------------
from pyrogram import Client, filters
import asyncio
import time
import datetime
import shutil, psutil, traceback, os
import random
import string
import traceback
import json
import aiofiles
from pyrogram import Client, filters, __version__
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os, youtube_dl, requests, time
from Config import Config
from youtube_search import YoutubeSearch
from pyrogram.handlers import MessageHandler
from pyrogram import Client, filters
import yt_dlp
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery 
from yt_dlp import YoutubeDL
from pyrogram import Client, filters
from pyrogram.types import Message
import wget
import asyncio
import random, re
import pyrogram
import os
import asyncio
from telegraph import upload_file
import pyrogram
import asyncio 
from collections import deque
from random import randint
from pyrogram import filters, Client
from pyrogram.types import Message
from platform import python_version as y
from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import secrets
import string 
import aiohttp
from pyrogram import filters
from cryptography.fernet import Fernet
from AykhanPro.komekci import random_line
from sorular import D_LİST, C_LİST
from pyrogram import Client, idle, filters
import random
from random import choice
from pyrogram.types import Message
from pyrogram import idle, filters
from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from helper.fotnt_string import Fonts
import asyncio
from asyncio import gather
from io import BytesIO
from math import atan2, cos, radians, sin, sqrt
from os import execvp
from random import randint
from re import findall
from re import sub as re_sub
from sys import executable
import speedtest
from PIL import Image
from pyrogram.types import Message
from telegraph import upload_file
from aiohttp import ClientSession
from pyrogram.errors import (
    FloodWait,
    InputUserDeactivated,
    PeerIdInvalid,
    UserIsBlocked,
)



logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN
bot_username = Config.BOT_USERNAME
support = Config.SUPPORT_CHAT
owner = Config.OWNER_USERNAME
bot_name = Config.BOT_NAME


SUDO_USERS = Config.SUDO_USERS

OWNER_ID = Config.OWNER_ID

SUDO = Config.SUDO

temalar = [" [OldMultiBot](https://t.me/addtheme/sf158WSw7LWOtpvV) ",
" [OldMultiBot](https://t.me/addtheme/bpcrFtP4qYu0DdnJ) " ,
" [OldMultiBot](https://t.me/addtheme/aUFKCX7AQ3aQpDjp) " ,
" [OldMultiBot](https://t.me/addtheme/L7HVQjC4UUyOfL9y) " ,
" [OldMultiBot](https://t.me/addtheme/Qd4eBWTIOH4Ai3Zv) " ,
" [OldMultiBot](https://t.me/addtheme/NightWolf) " ,
" [OldMultiBot](https://t.me/addtheme/GreenBlack) " ,
" [OldMultiBot](https://t.me/addtheme/TvldPzYmpG8LqkY3) " ,
" [OldMultiBot](https://t.me/addtheme/Q4GuvNPpMvG59G6V) " ,
" [OldMultiBot](https://t.me/addtheme/kGQaW0HHsjc7oFOv) " ,
" [OldMultiBot](https://t.me/addtheme/z3E6vkceX0pfmo5P) " ,
" [OldMultiBot](https://t.me/addtheme/poMW3amfnwUwOefI) " ,
" [OldMultiBot](https://t.me/addtheme/l1felAbEVNQCN3NW) " ,
" [OldMultiBot](https://t.me/addtheme/y6xMaSuBOmuGekHj) " ,
" [OldMultiBot](https://t.me/addtheme/Fp6h6JpzXrWnjF9y) " ,
" [OldMultiBot](https://t.me/addtheme/Purple_Grapes) " ,
" [OldMultiBot](https://t.me/addtheme/xQNP1Jp2aklmldNx) " ,
" [OldMultiBot](https://t.me/addtheme/ry0AgHsISs439fxi) " ,
" [OldMultiBot](https://t.me/addtheme/ZHl93FYO9ja7hN81) " ,
" [OldMultiBot](https://t.me/addtheme/gc2MlPyKHMBjw5WS) " ,
" [Aylin](https://t.me/addtheme/ciNZt5N6QCFjsrQI) " ,
" [OldMultiBot](https://t.me/addtheme/bEKOF0v8XuLAFZ6P) " ,
" [OldMultiBot](https://t.me/addtheme/IOSTelegramThemes2020_11july) " ,
" [OldMultiBot](https://t.me/addtheme/DarkPink_1) " ,
" [OldMultiBot](https://t.me/addtheme/Halloween_04) " ,
" [OldMultiBot](https://t.me/addtheme/BlackBlue_ByYamila) " ,
" [OldMultiBot](https://t.me/addtheme/NewYorkNyVK) " ,
" [OldMultiBot](https://t.me/addtheme/blackcircles_ByYamila) " ,
" [OldMultiBot](https://t.me/addtheme/KINGByVK) " ,
" [OldMultiBot](https://t.me/addtheme/MRPERFECTBYVK) " ,
" [OldMultiBot](https://t.me/addtheme/ChanchiNeonByVK) " ,
" [OldMultiBot](https://t.me/addtheme/SamurayByVK) " ,
" [OldMultiBot](https://t.me/addtheme/NeonRocks_ByYamila) " ,
" [OldMultiBot](https://t.me/addtheme/StichOhanaByVK) " ,
" [OldMultiBot](https://t.me/addtheme/SkullDarkByVK) " ,
" [OldMultiBot](https://t.me/addtheme/RedGirlByVK) " ,
" [OldMultiBot](https://t.me/addtheme/SpidermanByVK) " ,
" [OldMultiBot](https://t.me/addtheme/CuteMelodyByVK) " ,
" [OldMultiBot](https://t.me/addtheme/YouAreBeautifulStichByVK) " ,
" [OldMultiBot](https://t.me/addtheme/ManchesterUnitedByVK) "]


ALIVE = (
    "Sahibim OLD MULTI BOT : ONLINE\n\nVERSIYA ⚡️"
    f"\nv{__version__}"
)

ydl_opts = {
    'format': 'best',
    'keepvideo': True,
    'prefer_ffmpeg': False,
    'geo_bypass': True,
    'outtmpl': '%(title)s.%(ext)s',
    'quite': True
}

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton(text="➕️ GROUPA ELAVE ET", url=f"http://t.me/oldtaggerbot?startgroup=a")]])

FORCE_SUB = "TEAMABASOFcom"

#-#-#-# Pyrogram Başlanğıc #-#-#-#
app = Client(":memory:", api_id, api_hash, bot_token=bot_token)





                
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = [] 

tekli_calisan = []


 

#pyrogram
@app.on_message(filters.command("info"))
async def _id(_, message: Message):
    msg = message.reply_to_message or message
    out_str = "**User İnfo:**\n"
    out_str += f" 💎 __Yanıtlanan Kullanıcı Adı__ : {msg.from_user.first_name}\n"
    out_str += f" 💬 __Mesaj ID__ : `{msg.forward_from_message_id or msg.message_id}`\n"
    if msg.from_user:
        out_str += f" 🙋🏻‍♂️ __Yanıtlanan Kullanıcı ID__ : `{msg.from_user.id}`\n"
 
    await message.reply(out_str)



#mahnı yükləmə#
@app.on_message(filters.command("song"))
def song(_, message):
    query = " ".join(message.command[1:])
    m = message.reply("<b>Mahnınız Axtarılır ... 🔍</b>")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        m.edit("<b>❌ Bunu deməliyəm üzürlü say 😔 mahnı tapılmadı.\n\n Zəhmət Olmasa başqa mahnı adı deyin @oldsupport 🍷.</b>")
        print(str(e))
        return
    m.edit("<b>📥 Yükləmə Prosesi Başladı...</b>")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"**╭───────────────**\n**├▷ ♬ Adı: [{title[:35]}]({link})**\n**├───────────────**\n**├▷♬ Playlist @{Config.PLAYLIST_NAME}**\n**╰───────────────**"
        res = f"**╭───────────────**\n**├▷ ♬ Adı: [{title[:35]}]({link})**\n**├───────────────**\n**├▷👤 İstəyən** [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n**├───────────────**\n**├▷🌀 Bot: @{Config.BOT_USERNAME}**\n**╰───────────────**"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("📤 Yüklenir..")
        message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name, performer="@OldMultiBot")
        m.delete()
        app.send_audio(chat_id=Config.PLAYLIST_ID, audio=audio_file, caption=res, performer="@OldMultiBot", parse_mode='md', title=title, duration=dur, thumb=thumb_name)
    except Exception as e:
        m.edit("<link Xətanın, düzelmesini gözləyin.</b>")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)


# video indirme 

@app.on_message(
    filters.command(["video", "vsong"])
)
async def vsong(client, message):
    ydl_opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
    }
    query = " ".join(message.command[1:])
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        results[0]["duration"]
        results[0]["url_suffix"]
        results[0]["views"]
        message.from_user.mention
    except Exception as e:
        print(e)
    try:
        msg = await message.reply("📥 **video yüklənəcəy...**")
        with YoutubeDL(ydl_opts) as ytdl:
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit(f"🚫 **Xəta:** {e}")
    preview = wget.download(thumbnail)
    await msg.edit("📤 **video yüklənir...**")
    await message.reply_video(
        file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=ytdl_data["title"],
    )
    try:
        os.remove(file_name)
        await msg.delete()
    except Exception as e:
        print(e)




#Pyrogram comand
@app.on_message(filters.command("zer"))
async def roll_dice(bot, message):
    await bot.send_dice(message.chat.id, "🎲")

@app.on_message(filters.command("ox"))                                      
async def roll_arrow(bot, message):
    await bot.send_dice(message.chat.id, "🎯")

@app.on_message(filters.command("gol"))
async def roll_goal(bot, message):
    await bot.send_dice(message.chat.id, "⚽️")

@app.on_message(filters.command("spin"))
async def roll_luck(bot, message):
    await bot.send_dice(message.chat.id, "🎰")

@app.on_message(filters.command("basket"))
async def roll_throw(bot, message):
    await bot.send_dice(message.chat.id, "🏀")

@app.on_message(filters.command(["bowling", "tenpins"]))
async def roll_bowling(bot, message):
    await bot.send_dice(message.chat.id, "🎳") 

 

#telethon xos geldin mesaj @edalet_22 terifindən hazırlandı
@client.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        await event.reply(random.choice(userjoin))


@client.on(events.ChatAction)
async def handler(event):
    if event.user_left:
        await event.reply("Əla Birdə gəlmə")

userjoin = (

    "XOŞ GƏLDİN ARAMIZA",
    "Xoş gəldin xoş söhbətlər arzu edirəm",
    "Xoş gəldin necəsən",
    "Xoş gəldin groupa",
    "Xoş gəldin əzizim",
    "",
)


@app.on_message(filters.command("ping"))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")




@app.on_message(filters.command("pin"))
async def pin(_, message: Message):
    if not message.reply_to_message:
        return
    args = message.text.lower().split()
    notify = not any(arg in args for arg in ('loud', 'notify'))
    await message.reply_to_message.pin(disable_notification=notify)

@app.on_message(filters.command("unpin"))
async def unpin(_, message: Message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.unpin()



ABISHNOIX = "https://telegra.ph/file/44d9457217353f7f955b8.jpg"


@app.on_message(filters.command(["alive"]) & filters.user(OWNER_ID))
async def alive(_, message):
    await message.reply_photo(
        photo=ABISHNOIX,
        caption=f"""✨ **@OldMultiBot AKTİVDİR {message.from_user.mention},**

**BOT SAHİBİ  : [TEAMABASOF](https://t.me/AnonyumAz)**
**ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ :** `{y()}`
**ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ :** `{s}`
**ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀꜱɪᴏɴ :** `{z}`
**ʙᴏᴛ ᴠᴇʀꜱɪᴏɴ :** `1.0`
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•🎴 KANALIM•", url="https://t.me/TEAMABASOFcoç"
                    ),
                    InlineKeyboardButton(
                        "•📂 APK•", url="https://t.me/texnoapk1"
                    ),
                ]
            ]
        ),
    )


@app.on_message(filters.command("sehid"))
async def commit(_, message):
    await message.reply_text((await random_line('AykhanPro/txt/sehid.txt')))
				
@app.on_message(filters.command("meslehet") & ~filters.edited)
async def meslehet(_, message):
    await message.reply_text((await random_line('AykhanPro/txt/meslehet.txt')))


@app.on_message(filters.command("anekdod"))
async def anekdod(_, message):
    await message.reply_text((await random_line('AykhanPro/txt/anekdod.txt')))




@app.on_message(filters.command("tema"))
async def tema(app: Client, msg: Message):
    await msg.reply(random.choice(temalar))






#Pastebins
async def p_paste(message, extension=None):
    siteurl = "https://pasty.lus.pm/api/v1/pastes"
    data = {"content": message}
    try:
        response = requests.post(url=siteurl, data=json.dumps(data), headers=headers)
    except Exception as e:
        return {"error": str(e)}
    if response.ok:
        response = response.json()
        purl = (
            f"https://pasty.lus.pm/{response['id']}.{extension}"
            if extension
            else f"https://pasty.lus.pm/{response['id']}.txt"
        )
        return {
            "url": purl,
            "raw": f"https://pasty.lus.pm/{response['id']}/raw",
            "bin": "Pasty",
        }
    return {"error": "Unable to reach pasty.lus.pm"}



@app.on_message(filters.command(["tgpaste", "pasty", "paste"]))
async def pasty(client, message):
    pablo = await message.reply_text("`Gözləyin...`")
    tex_t = message.text
    if ' ' in message.text:
        message_s = message.text.split(" ", 1)[1]
    elif message.reply_to_message:
        message_s = message.reply_to_message.text
    else:
        await message.reply("daxil olunmur mətinə yanitlayaraq yazin/paste yanitla")
    if not tex_t:
        if not message.reply_to_message:
            await pablo.edit("`Yalnız mətin və sənədlər dəsdəklənir.`")
            return
        if not message.reply_to_message.text:
            file = await message.reply_to_message.download()
            m_list = open(file, "r").read()
            message_s = m_list
            os.remove(file)
        elif message.reply_to_message.text:
            message_s = message.reply_to_message.text

    ext = "py"
    x = await p_paste(message_s, ext)
    p_link = x["url"]
    p_raw = x["raw"]

    pasted = f"**Uğurla Pasty yapışdırlıdı**\n\n**Link:** • [Click here]({p_link})\n\n**Raw Link:** • [Click here]({p_raw})"
    await pablo.edit(pasted, disable_web_page_preview=True)



@app.on_message(filters.command("mal"))
async def runs(_, message):
    """ /runs strings """
    effective_string = f"**🐄 Mal testi edildi**\n\n**{message.reply_to_message.from_user.mention} sən {random.randint(0,101)}% Malsan**"
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)


@app.on_message(filters.command("sevgi"))
async def runs(_, message):
    """ /runs strings """
    effective_string = f"**Sevgi Testi 💘**\n\n**❤️ {message.from_user.mention}**\n\n**💟 {message.reply_to_message.from_user.mention}**\n\n**Sevgi faizi  {random.randint(0,101)}%**"
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)





aiohttpsession = ClientSession()

async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with aiohttpsession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@app.on_message(filters.command("carbon"))
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "Mesaja yanıt verərək carbon yazın."
        )
    if not message.reply_to_message.text:
        return await message.reply_text(
            "Mesaja yanıt verərək carbon yazın."
        )
    user_id = message.from_user.id
    m = await message.reply_text("Emal edilir...")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("Yükləndi..")
    await message.reply_photo(
        photo=carbon,
        caption=f"**Carbon uğurla hazırlandı✅️**\n\n**@OldMultiBot ilə {message.from_user.mention} tərəfindən Carbon hazırlandı**",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝚂𝚄𝙿𝙿𝙾𝚁𝚃", url="https://t.me/TEAMABASOFcom")]]),                   
    )
    await m.delete()
    carbon.close()


@app.on_message(filters.command("telegraph"))
async def telegraph(c: app, m: Message):
    replied = m.reply_to_message
    start_t = datetime.now()
    await m.edit_text("`Trying to paste to telegraph...`", parse_mode="md")
    if not replied:
        await m.edit_text("reply to a supported media file")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4")
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await m.edit_text("**Not supported!**", parse_mode="md")
        return
    download_location = await c.download_media(
        message=m.reply_to_message, file_name="telepyrobot/downloads/"
    )
    await m.edit_text("`Pasting to telegraph...`", parse_mode="md")
    try:
        response = upload_file(download_location)
    except Exception as document:
        await m.edit_text(document)
    else:
        end_t = datetime.now()
        ms = (end_t - start_t).seconds
        await m.edit_text(
            f"**Document Passed to** [Telegra.ph](https://telegra.ph{response[0]}) **in __{ms}__ seconds**",
            parse_mode="md",
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)
    return




#@(events.NewMessage(pattern='/reklam'))
#async def handler(event):	
 #    await event.reply('🤖 [USTA Tag Bot](http://t.me/UstaTagbot)-unda Reklam Almaq Üzçün [ɴᴀᴋʜɪᴅ ᴜsᴛᴀ ¦ 🇧🇻🦅](https://t.me/UstaNakhid)-ilə Әlaqә Saxlayın.')
 

print(">> Bot işləyir narahat olmayın. @edalet_22 Məlumat almaq üçün <<")
app.start()
client.run_until_disconnected()
