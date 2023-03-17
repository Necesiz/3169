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
import openai
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

openai.api_key = "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"



@app.on_message(filters.command('gpt'))
async def start(client, msj):
    chat_id = msj.chat.id
    reply = msj.reply_to_message
    
    
    
    if reply:
        yazi = reply.text
        yazi = yazi.lower()
        if "kod" in yazi or "kodu" in yazi:
                    z = await client.send_message(chat_id, f"👩 **Mən sənin sualına  cavab hazırlayıram...**\n🥰 **Bu sənin nə istədiyindən asılı olaraq vaxt ala bilər**")
                    response = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=yazi,
                        temperature=0.9,
                        max_tokens=2048,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0.6,
                        stop=["###"]
                    )
                    text = response['choices'][0]['text']
                    await client.delete_messages(chat_id, z.id)
                    await client.send_message(chat_id, f"`{text}`")
                    await client.send_message(chat_id, f"🌌 **Sualına cavab yazdım yeni sual üçün /sofia sualını yaz**")
        else:
                    z = await client.send_message(chat_id, f"👩 **Mən sənin sualına  cavab hazırlayıram...**\n🥰 **Bu sənin nə istədiyindən asılı olaraq vaxt ala bilər**")
                    response = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=yazi,
                        temperature=0.9,
                        max_tokens=3072,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0.6,
                        stop=["###"]
                    )
                    text = response['choices'][0]['text']
                    await client.delete_messages(chat_id, z.id)
                    await client.send_message(chat_id, f"{text}")
    elif not reply:
        try:
            yazi = msj.text.split(" ", 1)[1]
            yaziVar = True
            if yaziVar == True:
                yazi = yazi.lower()
                if "kod" in yazi or "kodu" in yazi:
                    z = await client.send_message(chat_id, f"👩 **Mən sənin sualına  cavab hazırlayıram...**\n🥰 **Bu sənin nə istədiyindən asılı olaraq vaxt ala bilər**")
                    response = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=yazi,
                        temperature=0.9,
                        max_tokens=2048,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0.6,
                        stop=["###"]
                    )
                    text = response['choices'][0]['text']
                    await client.delete_messages(chat_id, z.id)
                    await client.send_message(chat_id, f"`{text}`")
                    await client.send_message(chat_id, f"🌌 **Yeni sual vermək isdyirsənsə /sofia sualını qeyd ed**")
                else:
                    z = await client.send_message(chat_id, f"👩 **Mən sənin sualına  cavab hazırlayıram...**\n🥰 **Bu sənin nə istədiyindən asılı olaraq vaxt ala bilər**")
                    response = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=yazi,
                        temperature=0.9,
                        max_tokens=3072,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0.6,
                        stop=["###"]
                    )
                    text = response['choices'][0]['text']
                    await client.delete_messages(chat_id, z.id)
                    await client.send_message(chat_id, f"{text}")
        except Exception as e:
            print(e)
            await client.send_message(chat_id, f"🤔 **Sualını aydın yaz.**")







#@(events.NewMessage(pattern='/reklam'))
#async def handler(event):	
 #    await event.reply('🤖 [USTA Tag Bot](http://t.me/UstaTagbot)-unda Reklam Almaq Üzçün [ɴᴀᴋʜɪᴅ ᴜsᴛᴀ ¦ 🇧🇻🦅](https://t.me/UstaNakhid)-ilə Әlaqә Saxlayın.')
 

print(">> Bot işləyir narahat olmayın. @edalet_22 Məlumat almaq üçün <<")
app.start()
client.run_until_disconnected()
