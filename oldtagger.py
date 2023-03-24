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
import asyncio
import speedtest
# Pyrogram----------------------------------------------------------------------------------------------------



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



def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        test.download()
        test.upload()
        test.results.share()
        result = test.results.dict()
    except Exception as e:
        return
    return result

@client.on(events.NewMessage(pattern="^/speedtest"))
async def speedtest_function(message):
    m = await message.reply("Running Speed test")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""**Speedtest Results**
    
**Client:**
**__ISP:__** {result['client']['isp']}
**__Country:__** {result['client']['country']}
  
**Server:**
**__Name:__** {result['server']['name']}
**__Country:__** {result['server']['country']}, {result['server']['cc']}
**__Sponsor:__** {result['server']['sponsor']}
**__Latency:__** {result['server']['latency']}  
**__Ping:__** {result['ping']}"""
    await client.send_file(message.chat.id, result["share"], caption=output)
    await m.delete()






#@(events.NewMessage(pattern='/reklam'))
#async def handler(event):	
 #    await event.reply('🤖 [USTA Tag Bot](http://t.me/UstaTagbot)-unda Reklam Almaq Üzçün [ɴᴀᴋʜɪᴅ ᴜsᴛᴀ ¦ 🇧🇻🦅](https://t.me/UstaNakhid)-ilə Әlaqә Saxlayın.')
 

print(">> Bot işləyir narahat olmayın. @edalet_22 Məlumat almaq üçün <<")
app.start()
client.run_until_disconnected()
