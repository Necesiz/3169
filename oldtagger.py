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

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.reply(f"**👋 Salam {ad} Mən OLD MULTİ BOT bir cox funksyaya malik OLD MULTİ botam\n\n🤔 Botun isdifade qaydasın bilmirsen indi ise '🎛 ƏMRLƏR' bölməsinə daxil olun\n\n✉️ Botu başladıqına dayir Sahibime mesaj yolladım**", buttons=(
                     [Button.inline("🎛 ƏMRLƏR", data="emir")],
       # [Button.url('🎉 Sahib', 'https://t.me/Nehmedov')],
              # [Button.url('Qurup🛠', 'https://t.me/Bizim_Paytaxt'),
                    #  Button.url('💡 USTA Bots', 'https://t.me/ustabots')],
               [Button.url('➕ Qrupa Əlavə Et ➕','http://t.me/OldMultiBot?startgroup=a'),
                Button.url('🎴 KANALIM','http://t.me/TEAMABASOFcom')],
               [Button.url("🌟 SAHİB",'https://t.me/AnonyumAz'),
                      Button.url('🎶 PLAY LİST','https://t.me/oldmultisong')],
                    ),
                    link_preview=False)


  if event.is_group:
    return await client.send_message(event.chat_id, f"**Əziz isdifadeçi Qroupda cox yazmaqla başınızı ağrıtmıyım Bota Keç vuraraq şexside melumat ala bilersiz**", buttons=(
                     [Button.url('💡 Bota Keç','https://t.me/OldMultiBot?start=start')],
                    ),
                    link_preview=False)



@client.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.edit(f"**👋 Salam {ad} Mən OLD MULTİ BOT bir cox funksyaya malik OLD MULTİ botam\n\n🤔 Botun isdifade qaydasın bilmirsen indi ise '🎛 ƏMRLƏR' bölməsinə daxil olun\n\n✉️ Botu başladıqına dayir Sahibime mesaj yolladım**", buttons=(
                     [Button.inline(f"🎛 ƏMRLƏR", data="emir")],
        # [Button.url('🎉 Sahib', 'https://t.me/Nehmedov')],
               #[Button.url('Qurup🛠', 'https://t.me/Bizim_Paytaxt'),
                      #Button.url('🤖 USTA Bots', 'https://t.me/ustabots')],
               [Button.url('➕ Qrupa Əlavə Et ➕','http://t.me/OldMultiBot?startgroup=a'),
                Button.url('🎴 KANALIM','http://t.me/TEAMABASOFcom')],
               [Button.url('🌟 SAHİB','https://t.me/AnonyumAz'),
                      Button.url('🎶 PLAY LİST', 'https://t.me/oldmultisong')],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="emir"))
async def handler(event):
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.edit(f"**🤩 Siz artıq ƏMRLƏR bölümündesiz\n\n🫡 Hansı əmri isdəsəniz aşağıda Buttonla vuraraq baxa bilersiz\n\n🩶 XOŞ İSDİFADELER @OldMultiBot**", buttons=(
                     [Button.inline("🌟 ADMİN ƏMRLƏR", data="ahelp")],
        # [Button.url('🎉 Sahib', 'https://t.me/Nehmedov')],
               #[Button.url('Qurup🛠', 'https://t.me/Bizim_Paytaxt'),
                      #Button.url('🤖 USTA Bots', 'https://t.me/ustabots')],
               [Button.inline(f"🪬 SAHİB ƏMRLƏRİ", data="thelp"),
                Button.inline(f"📥 YÜKLƏMƏ", data="yhelp")],
               [Button.inline(f"🕹 ƏYLƏNCƏ", data="dhelp"),
                      Button.inline(f"➕️ ƏLAVƏLƏR", data="elave")],
	       [Button.inline(f"🔙 Geri", data="start")]
                    ),
                    link_preview=False)

# rehim / abasof
@client.on(events.callbackquery.CallbackQuery(data="thelp"))
async def handler(event): 
    await event.edit(f"**[@OldMultiBot](http://t.me/OldMultiBot)-un '🪬 SAHİB ƏMRLƏR' bölməsi ⤵**\n\n\n•━━━━━━━━•••━━━━━━━━•\n**🪬 ➪ /stats - Botun istdifadəçiləri və botun olduqu groupları göstərir**\n\n**🪬 ➪ /reklam - reklam yollayar**\n\n**🪬 ➪ /alive - Botun aktiv olduqun göstərir**\n•━━━━━━━━•••━━━━━━━━•", buttons=(
              # [Button.url('➕ Məni Qrupa əlavə et ➕','http://t.me/UstaTagbot?startgroup=a')],
         #[Button.url('🎉 Sahib', 'https://t.me/Nehmedov')],
               [Button.url('🔮 Kanalım','https://t.me/TEAMABASOFcom'),
                      Button.url('🎶 PLAY LİST','https://t.me/oldmultisong')],
               [Button.inline(f"🔙 Geri", data="emir")]
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="yhelp"))
async def handler(event): 
    await event.edit(f"**[@OldMultiBot](http://t.me/OldMultiBot)-un '📥 YÜKLƏMƏ' bölməsi ⤵**\n\n\n•━━━━━━━━•••━━━━━━━━•\n**🎵 ➪  /song - MAHNI YÜKLƏYİR**\n**📽 ➪ /video və ya /vsong - İsdədiyiniz videonu Youtub dan yükləyər\n**📜 ➪ /paste - mətini pastebin edin**\n•━━━━━━━━•••━━━━━━━━•", buttons=(
              # [Button.url('➕ Məni Qrupa əlavə et ➕','http://t.me/UstaTagbot?startgroup=a')],
         #[Button.url('🎉 Sahib', 'https://t.me/Nehmedov')],
               [Button.url('🔮 Kanalım','https://t.me/TEAMABASOFcom'),
                      Button.url('🎶 PLAY LİST','https://t.me/oldmultisong')],
               [Button.inline(f"🔙 Geri", data="emir")]
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="dhelp"))
async def handler(event): 
    await event.edit(f"**[@OldMultiBot](http://t.me/OldMultiBot)-un '🕹 ƏYLƏNCƏ' bölməsi ⤵**\n\n\n•━━━━━━━━•••━━━━━━━━•\n**☸️ ➪ /dc - Doğruluq Və Cəsarət oyunu basladır**\n**🎲 ➪ /zer - Zər atar**\n**🎯 ➪ /ox - Ox atar**\n**⚽️ ➪ /gol - Goal atar**\n**🎰 ➪ /spin - Spin cevir**\n**🏀 ➪ /basket - Basket atar**\n**🎳 ➪ /bowling - Bowling atar**\n\n**❤️‍🔥 ➪ /sevgi - sevdiyiniz insanın adininin baş hərfini göstərir(Groupda işləkdir)**\n•━━━━━━━━•••━━━━━━━━•", buttons=(
              # [Button.url('➕ Məni Qrupa əlavə et ➕','http://t.me/UstaTagbot?startgroup=a')],
         #[Button.url('🎉 Sahib', 'https://t.me/Nehmedov')],
               [Button.url('🔮 Kanalım','https://t.me/TEAMABASOFcom'),
                      Button.url('🎶 PLAY LİST','https://t.me/oldmultisong')],
               [Button.inline(f"🔙 Geri", data="emir")]
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="elave"))
async def handler(event): 
    await event.edit(f"**[@OldMultiBot](http://t.me/OldMultiBot)-un '➕️ ƏLAVƏLƏR' bölməsi ⤵**\n\n\n•━━━━━━━━•••━━━━━━━━•\n**🪪 ➪ /info - Kullanıcı melumat getirii**\n**📈 ➪ /ping - Botun pingin ölçür**\n**\n**😔 ➪ /sehid - şəhid adları atır**\n**🤖 ➪ /anekdod - Random anekdod atar**\n**🤖 ➪ /meslehet - Botdan Məsləhət alin**\n**🤖 ➪ /carbon - Mətini carbona dönüşdür (Qroupda isliyir)**\n**🤖 ➪ /tema - Random Telegram Teması atar (Qroupda isliyir)**\n**👋 ➪ salamlama - Groupa qatılanlara xoş geldin deyir**\n•━━━━━━━━•••━━━━━━━━•", buttons=(
              # [Button.url('➕ Məni Qrupa əlavə et ➕','http://t.me/UstaTagbot?startgroup=a')],
         #[Button.url('🎉 Sahib', 'https://t.me/Nehmedov')],
               [Button.url('🔮 Kanalım','https://t.me/TEAMABASOFcom'),
                      Button.url('🎶 PLAY LİST','https://t.me/oldmultisong')],
               [Button.inline(f"🔙 Geri", data="emir")]
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="ahelp"))
async def handler(event): 
    await event.edit(f"**[@OldMultiBot](http://t.me/OldMultiBot)-un '🌟 ADMİN ƏMRLƏRİ' bölməsi ⤵**\n\n\n•━━━━━━━━•••━━━━━━━━•\n**🌟 ➪ /pin - Groupda mesaj sabitleyir**\n**🌟 ➪ /unpin - bot kendi etdiyi mesajı sabitden qaldırar**\n•━━━━━━━━•••━━━━━━━━•", buttons=(
              # [Button.url('➕ Məni Qrupa əlavə et ➕','http://t.me/UstaTagbot?startgroup=a')],
         #[Button.url('🎉 Sahib', 'https://t.me/Nehmedov')],
               [Button.url('🔮 Kanalım','https://t.me/TEAMABASOFcom'),
                      Button.url('🎶 PLAY LİST','https://t.me/oldmultisong')],
               [Button.inline(f"🔙 Geri", data="emir")]
                    ),
                    link_preview=False)


 

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

# Dc Komutu İcin Olan Buttonlar
def d_or_c(user_id):
	BUTTON = [[InlineKeyboardButton(text="? Doğruluk", callback_data = " ".join(["d_data",str(user_id)]))]]
	BUTTON += [[InlineKeyboardButton(text="?? Cesaret", callback_data = " ".join(["c_data",str(user_id)]))]]
	return InlineKeyboardMarkup(BUTTON)

# Dc Komutunu Oluşturalım
@app.on_message(filters.command("dc"))
async def _(client, message):
	user = message.from_user

	await message.reply_text(text="{} İstediğin Soru Tipini Seç!".format(user.mention),
		reply_markup=d_or_c(user.id)
		)

# Buttonlarımızı Yetkilendirelim
@app.on_callback_query()
async def _(client, callback_query):
	d_soru=random.choice(D_LİST) # Random Bir Doğruluk Sorusu Seçelim
	c_soru=random.choice(C_LİST) # Random Bir Cesaret Sorusu Seçelim
	user = callback_query.from_user # Kullanıcın Kimliğini Alalım

	c_q_d, user_id = callback_query.data.split() # Buttonlarımızın Komutlarını Alalım

	# Sorunun Sorulmasını İsteyen Kişinin Komutu Kullanan Kullanıcı Olup Olmadığını Kontrol Edelim
	if str(user.id) == str(user_id):
		# Kullanıcının Doğruluk Sorusu İstemiş İse Bu Kısım Calışır
		if c_q_d == "d_data":
			await callback_query.answer(text="Doğruluq Sorusu İstədiniz", show_alert=False) # İlk Ekranda Uyarı Olarak Gösterelim
			await client.delete_messages(
				chat_id=callback_query.message.chat.id,
				message_ids=callback_query.message.message_id) # Eski Mesajı Silelim

			await callback_query.message.reply_text("**{user} Doğruluq Sorusu İstədi:** __{d_soru}__".format(user=user.mention, d_soru=d_soru)) # Sonra Kullanıcıyı Etiketleyerek Sorusunu Gönderelim
			return

		if c_q_d == "c_data":
			await callback_query.answer(text="Cəsarət Sorusu İstədiniz", show_alert=False)
			await client.delete_messages(
				chat_id=callback_query.message.chat.id,
				message_ids=callback_query.message.message_id)
			await callback_query.message.reply_text("**{user} Cəsarət Sorusu İstədi:** __{c_soru}__".format(user=user.mention, c_soru=c_soru))
			return


	# Buttonumuza Tıklayan Kisi Komut Calıştıran Kişi Değil İse Uyarı Gösterelim
	else:
		await callback_query.answer(text="əmiri isdifade edən kişi Sən Deyilsən!!", show_alert=False)
		return

############################
    # Sudo islemleri #
@app.on_message(filters.command("cekle"))
async def _(client, message):
  global MOD
  user = message.from_user
  
  if user.id not in OWNER_ID:
    await message.reply_text("**[?]** **Sən botda Sudo deyilsən!!**")
    return
  MOD="cekle"
  await message.reply_text("**[?]** **Əlavə etmək isdədiyiniz cəsarət sualını yazın!**")
  
@app.on_message(filters.command("dekle"))
async def _(client, message):
  global MOD
  user = message.from_user
  
  if user.id not in OWNER_ID:
    await message.reply_text("**[?]** **Sən botda Sudo deyilsən!!**")
    return
  MOD="cekle"
  await message.reply_text("**[?]** **Əlavə etmək isdədiyiniz cəsarət sualını yazın!**")

@app.on_message(filters.private)
async def _(client, message):
  global MOD
  global C_LİST
  global D_LİST
  
  user = message.from_user
  
  if user.id in OWNER_ID:
    if MOD=="cekle":
      C_LİST.append(str(message.text))
      MOD=None
      await message.reply_text("**[?]** __Mətin Cəsarət Sualı Olaraq Əlavə edildi!__")
      return
    if MOD=="dekle":
      C_LİST.append(str(message.text))
      MOD=None
      await message.reply_text("**[?]** __Mətin Doğruluq Sualı Olaraq Əlavə edildi!__")
      return





@app.on_message(filters.command("ping"))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")




@app.on_message(filters.command("tema"))
async def tema(app: Client, msg: Message):
    await msg.reply(random.choice(temalar))



@app.on_message(filters.private & filters.command(["font"]))
async def style_buttons(c, m, cb=False):
    buttons = [[
        InlineKeyboardButton('𝚃𝚢𝚙𝚎𝚠𝚛𝚒𝚝𝚎𝚛', callback_data='style+typewriter'),
        InlineKeyboardButton('𝕆𝕦𝕥𝕝𝕚𝕟𝕖', callback_data='style+outline'),
        InlineKeyboardButton('𝐒𝐞𝐫𝐢𝐟', callback_data='style+serif'),
        ],[
        InlineKeyboardButton('𝑺𝒆𝒓𝒊𝒇', callback_data='style+bold_cool'),
        InlineKeyboardButton('𝑆𝑒𝑟𝑖𝑓', callback_data='style+cool'),
        InlineKeyboardButton('Sᴍᴀʟʟ Cᴀᴘs', callback_data='style+small_cap'),
        ],[
        InlineKeyboardButton('𝓈𝒸𝓇𝒾𝓅𝓉', callback_data='style+script'),
        InlineKeyboardButton('𝓼𝓬𝓻𝓲𝓹𝓽', callback_data='style+script_bolt'),
        InlineKeyboardButton('ᵗⁱⁿʸ', callback_data='style+tiny'),
        ],[
        InlineKeyboardButton('ᑕOᗰIᑕ', callback_data='style+comic'),
        InlineKeyboardButton('𝗦𝗮𝗻𝘀', callback_data='style+sans'),
        InlineKeyboardButton('𝙎𝙖𝙣𝙨', callback_data='style+slant_sans'),
        ],[
        InlineKeyboardButton('𝘚𝘢𝘯𝘴', callback_data='style+slant'),
        InlineKeyboardButton('𝖲𝖺𝗇𝗌', callback_data='style+sim'),
        InlineKeyboardButton('Ⓒ︎Ⓘ︎Ⓡ︎Ⓒ︎Ⓛ︎Ⓔ︎Ⓢ︎', callback_data='style+circles')
        ],[
        InlineKeyboardButton('🅒︎🅘︎🅡︎🅒︎🅛︎🅔︎🅢︎', callback_data='style+circle_dark'),
        InlineKeyboardButton('𝔊𝔬𝔱𝔥𝔦𝔠', callback_data='style+gothic'),
        InlineKeyboardButton('𝕲𝖔𝖙𝖍𝖎𝖈', callback_data='style+gothic_bolt'),
        ],[
        InlineKeyboardButton('C͜͡l͜͡o͜͡u͜͡d͜͡s͜͡', callback_data='style+cloud'),
        InlineKeyboardButton('H̆̈ă̈p̆̈p̆̈y̆̈', callback_data='style+happy'),
        InlineKeyboardButton('S̑̈ȃ̈d̑̈', callback_data='style+sad'),
        ],[
        InlineKeyboardButton('Next ➡️', callback_data="nxt")
    ]]
    if not cb:
        if ' ' in m.text:
            title = m.text.split(" ", 1)[1]
            await m.reply_text(title, reply_markup=InlineKeyboardMarkup(buttons), reply_to_message_id=m.id)                     
        else:
            await m.reply_text(text="İstənilən mətni daxil edin Məsələn:- `/font [mətn]`")    
    else:
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))


@app.on_callback_query(filters.regex('^nxt'))
async def nxt(c, m):
    if m.data == "nxt":
        buttons = [[
            InlineKeyboardButton('🇸 🇵 🇪 🇨 🇮 🇦 🇱 ', callback_data='style+special'),
            InlineKeyboardButton('🅂🅀🅄🄰🅁🄴🅂', callback_data='style+squares'),
            InlineKeyboardButton('🆂︎🆀︎🆄︎🅰︎🆁︎🅴︎🆂︎', callback_data='style+squares_bold'),
            ],[
            InlineKeyboardButton('ꪖꪀᦔꪖꪶꪊᥴ𝓲ꪖ', callback_data='style+andalucia'),
            InlineKeyboardButton('爪卂几ᘜ卂', callback_data='style+manga'),
            InlineKeyboardButton('S̾t̾i̾n̾k̾y̾', callback_data='style+stinky'),
            ],[
            InlineKeyboardButton('B̥ͦu̥ͦb̥ͦb̥ͦl̥ͦe̥ͦs̥ͦ', callback_data='style+bubbles'),
            InlineKeyboardButton('U͟n͟d͟e͟r͟l͟i͟n͟e͟', callback_data='style+underline'),
            InlineKeyboardButton('꒒ꍏꀷꌩꌃꀎꁅ', callback_data='style+ladybug'),
            ],[
            InlineKeyboardButton('R҉a҉y҉s҉', callback_data='style+rays'),
            InlineKeyboardButton('B҈i҈r҈d҈s҈', callback_data='style+birds'),
            InlineKeyboardButton('S̸l̸a̸s̸h̸', callback_data='style+slash'),
            ],[
            InlineKeyboardButton('s⃠t⃠o⃠p⃠', callback_data='style+stop'),
            InlineKeyboardButton('S̺͆k̺͆y̺͆l̺͆i̺͆n̺͆e̺͆', callback_data='style+skyline'),
            InlineKeyboardButton('A͎r͎r͎o͎w͎s͎', callback_data='style+arrows'),
            ],[
            InlineKeyboardButton('ዪሀክቿነ', callback_data='style+qvnes'),
            InlineKeyboardButton('S̶t̶r̶i̶k̶e̶', callback_data='style+strike'),
            InlineKeyboardButton('F༙r༙o༙z༙e༙n༙', callback_data='style+frozen')
            ],[
            InlineKeyboardButton('⬅️ Back', callback_data='nxt+0')
        ]]
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))
    else:
        await style_buttons(c, m, cb=True)


@app.on_callback_query(filters.regex('^style'))
async def style(c, m):
    await m.answer()
    cmd, style = m.data.split('+')

    if style == 'typewriter':
        cls = Fonts.typewriter
    if style == 'outline':
        cls = Fonts.outline
    if style == 'serif':
        cls = Fonts.serief
    if style == 'bold_cool':
        cls = Fonts.bold_cool
    if style == 'cool':
        cls = Fonts.cool
    if style == 'small_cap':
        cls = Fonts.smallcap
    if style == 'script':
        cls = Fonts.script
    if style == 'script_bolt':
        cls = Fonts.bold_script
    if style == 'tiny':
        cls = Fonts.tiny
    if style == 'comic':
        cls = Fonts.comic
    if style == 'sans':
        cls = Fonts.san
    if style == 'slant_sans':
        cls = Fonts.slant_san
    if style == 'slant':
        cls = Fonts.slant
    if style == 'sim':
        cls = Fonts.sim
    if style == 'circles':
        cls = Fonts.circles
    if style == 'circle_dark':
        cls = Fonts.dark_circle
    if style == 'gothic':
        cls = Fonts.gothic
    if style == 'gothic_bolt':
        cls = Fonts.bold_gothic
    if style == 'cloud':
        cls = Fonts.cloud
    if style == 'happy':
        cls = Fonts.happy
    if style == 'sad':
        cls = Fonts.sad
    if style == 'special':
        cls = Fonts.special
    if style == 'squares':
        cls = Fonts.square
    if style == 'squares_bold':
        cls = Fonts.dark_square
    if style == 'andalucia':
        cls = Fonts.andalucia
    if style == 'manga':
        cls = Fonts.manga
    if style == 'stinky':
        cls = Fonts.stinky
    if style == 'bubbles':
        cls = Fonts.bubbles
    if style == 'underline':
        cls = Fonts.underline
    if style == 'ladybug':
        cls = Fonts.ladybug
    if style == 'rays':
        cls = Fonts.rays
    if style == 'birds':
        cls = Fonts.birds
    if style == 'slash':
        cls = Fonts.slash
    if style == 'stop':
        cls = Fonts.stop
    if style == 'skyline':
        cls = Fonts.skyline
    if style == 'arrows':
        cls = Fonts.arrows
    if style == 'qvnes':
        cls = Fonts.rvnes
    if style == 'strike':
        cls = Fonts.strike
    if style == 'frozen':
        cls = Fonts.frozen

    r, oldtxt = m.message.reply_to_message.text.split(None, 1) 
    new_text = cls(oldtxt)            
    try:
        await m.message.edit_text(f"`{new_text}`\n\n👆 Kopyalamaq üçün kikləyin", reply_markup=m.message.reply_markup)
    except Exception as e:
        print(e)


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
    "content-type": "application/json",
}

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
