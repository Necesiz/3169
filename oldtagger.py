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
import time
import asyncio
import os
from Config import Config 
import os, logging, asyncio
from telethon import events, Button
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from asyncio import sleep 
import time, random
# Pyrogram----------------------------------------------------------------------------------------------------
import datetime
import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
import asyncio
import datetime
import shutil, psutil, traceback, os
import random
import string
import traceback
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
from io import BytesIO
from aiohttp import ClientSession
import random
from time import time
from random import choice
from pyrogram.types import Message
from pyrogram import idle, filters
from pyrogram import Client, filters
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

temalar = [" [Aylin](https://t.me/addtheme/sf158WSw7LWOtpvV) ",
" [Aylin](https://t.me/addtheme/bpcrFtP4qYu0DdnJ) " ,
" [Aylin](https://t.me/addtheme/aUFKCX7AQ3aQpDjp) " ,
" [Aylin](https://t.me/addtheme/L7HVQjC4UUyOfL9y) " ,
" [Aylin](https://t.me/addtheme/Qd4eBWTIOH4Ai3Zv) " ,
" [Aylin](https://t.me/addtheme/NightWolf) " ,
" [Aylin](https://t.me/addtheme/GreenBlack) " ,
" [Aylin](https://t.me/addtheme/TvldPzYmpG8LqkY3) " ,
" [Aylin](https://t.me/addtheme/Q4GuvNPpMvG59G6V) " ,
" [Aylin](https://t.me/addtheme/kGQaW0HHsjc7oFOv) " ,
" [Aylin](https://t.me/addtheme/z3E6vkceX0pfmo5P) " ,
" [Aylin](https://t.me/addtheme/poMW3amfnwUwOefI) " ,
" [Aylin](https://t.me/addtheme/l1felAbEVNQCN3NW) " ,
" [Aylin](https://t.me/addtheme/y6xMaSuBOmuGekHj) " ,
" [Aylin](https://t.me/addtheme/Fp6h6JpzXrWnjF9y) " ,
" [Aylin](https://t.me/addtheme/Purple_Grapes) " ,
" [Aylin](https://t.me/addtheme/xQNP1Jp2aklmldNx) " ,
" [Aylin](https://t.me/addtheme/ry0AgHsISs439fxi) " ,
" [Aylin](https://t.me/addtheme/ZHl93FYO9ja7hN81) " ,
" [Aylin](https://t.me/addtheme/gc2MlPyKHMBjw5WS) " ,
" [Aylin](https://t.me/addtheme/ciNZt5N6QCFjsrQI) " ,
" [Aylin](https://t.me/addtheme/bEKOF0v8XuLAFZ6P) " ,
" [Aylin](https://t.me/addtheme/IOSTelegramThemes2020_11july) " ,
" [Aylin](https://t.me/addtheme/DarkPink_1) " ,
" [Aylin](https://t.me/addtheme/Halloween_04) " ,
" [Aylin](https://t.me/addtheme/BlackBlue_ByYamila) " ,
" [Aylin](https://t.me/addtheme/NewYorkNyVK) " ,
" [Aylin](https://t.me/addtheme/blackcircles_ByYamila) " ,
" [Aylin](https://t.me/addtheme/KINGByVK) " ,
" [Aylin](https://t.me/addtheme/MRPERFECTBYVK) " ,
" [Aylin](https://t.me/addtheme/ChanchiNeonByVK) " ,
" [Aylin](https://t.me/addtheme/SamurayByVK) " ,
" [Aylin](https://t.me/addtheme/NeonRocks_ByYamila) " ,
" [Aylin](https://t.me/addtheme/StichOhanaByVK) " ,
" [Aylin](https://t.me/addtheme/SkullDarkByVK) " ,
" [Aylin](https://t.me/addtheme/RedGirlByVK) " ,
" [Aylin](https://t.me/addtheme/SpidermanByVK) " ,
" [Aylin](https://t.me/addtheme/CuteMelodyByVK) " ,
" [Aylin](https://t.me/addtheme/YouAreBeautifulStichByVK) " ,
" [Aylin](https://t.me/addtheme/ManchesterUnitedByVK) "]


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



# Qruplara yayım mesajı




############## DEĞİŞKENLER ##############

DATABASE_URL = "mongodb+srv://Bots:Bots@cluster0.nedd9xs.mongodb.net/?retryWrites=true&w=majority"
BOT_USERNAME = "OldMultiBot"
LOG_CHANNEL = -1001737573985
GROUP_SUPPORT = "TEAMABASOFcom"
GONDERME_TURU = False
OWNER_ID = [5134595693]
LANGAUGE = "AZ"

#---------------------------------------------------------------GROUP GIREKEN SALAMLAMA MSJ------------------------------------------------------------------------------#
@app.on_message(filters.new_chat_members, group=1)
async def hg(bot: Client, msg: Message):
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(Config.BOT_ID):
            await msg.reply(
                f'''`Salam` {msg.from_user.mention} `Məni` {msg.chat.title} `Qrupa əlavə etdiyiniz üçün təşəkkürlər⚡️` \n\n **🤖Qrupda bir cox funksyalı Multi botam.\n🤖Kömək üçün /start yazmaq kifayətdir.✨**''')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#-------------------------------------------------------------OWNERS SALAMLAMA MSJ---------------------------------------------------------------------------------------#
      
	# elif str(new_user.id) == str(Config.OWNER_ID):
      #       await msg.reply('🤖 [OLD MULTİ](https://t.me/OldMultiBot)-un Sahibi, Qrupa Qatıldı.\n Xoş Gəldin  Aramıza Sahib, @AnonyumAz🥰.')

	
	
	
#-------------------------------------------------------------VERİTABANI VERİ GİRİŞ ÇIKIŞI---------------------------------------------------------------------------------------#
 
class Database: 
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users

    def new_user(self, id): # Veritabanına yeni kullanıcı ekler
        return dict(
            id=id,
            join_date=datetime.date.today().isoformat(),
            ban_status=dict(
                is_banned=False,
                ban_duration=0,
                banned_on=datetime.date.max.isoformat(),
                ban_reason="",
            ),
        )

    async def add_user(self, id): # Veritabına yeni kullanıcı eklemek için ön def
        user = self.new_user(id)
        await self.col.insert_one(user)

    async def is_user_exist(self, id): # Bir kullanıcının veritabında olup olmadığını kontrol eder.
        user = await self.col.find_one({"id": int(id)})
        return bool(user)

    async def total_users_count(self): # Veritabanındaki toplam kullanıcıları sayar.
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self): # Veritabındaki tüm kullanıcıların listesini verir.
        return self.col.find({})

    async def delete_user(self, user_id): # Veritabından bir kullanıcıyı siler.
        await self.col.delete_many({"id": int(user_id)})

    async def ban_user(self, user_id, ban_duration, ban_reason): # Veritabanınızdaki bir kullanıcıyı yasaklılar listesine ekler.
        ban_status = dict(
            is_banned=True,
            ban_duration=ban_duration,
            banned_on=datetime.date.today().isoformat(),
            ban_reason=ban_reason,
        )
        await self.col.update_one({"id": user_id}, {"$set": {"ban_status": ban_status}})

    async def remove_ban(self, id): # Veritabanınızdaki yasaklılar listesinde bulunan bir kullanıcın yasağını kaldırır.
        ban_status = dict(
            is_banned=False,
            ban_duration=0,
            banned_on=datetime.date.max.isoformat(),
            ban_reason="",
        )
        await self.col.update_one({"id": id}, {"$set": {"ban_status": ban_status}})

    async def get_ban_status(self, id): # Bir kullanıcın veritabanınızda yasaklılar listesinde olup olmadığını kontrol eder.
        default = dict(
            is_banned=False,
            ban_duration=0,
            banned_on=datetime.date.max.isoformat(),
            ban_reason="",
        )
        user = await self.col.find_one({"id": int(id)})
        return user.get("ban_status", default)

    async def get_all_banned_users(self): # Veritabınızdaki yasaklı kullanıcılar listesini verir.
        return self.col.find({"ban_status.is_banned": True})


db = Database(DATABASE_URL, BOT_USERNAME)
mongo_db_veritabani = MongoClient(DATABASE_URL)
dcmdb = mongo_db_veritabani.handlers



################## KULLANICI KONTROLLERİ #############
async def handle_user_status(bot: Client, cmd: Message): # Kullanıcı kontrolü
    chat_id = cmd.chat.id
    if not await db.is_user_exist(chat_id):
        if cmd.chat.type == "private":
            await db.add_user(chat_id)
            await bot.send_message(LOG_CHANNEL,LAN.BILDIRIM.format(cmd.from_user.first_name, cmd.from_user.id, cmd.from_user.first_name, cmd.from_user.id))
        else:
            await db.add_user(chat_id)
            chat = bot.get_chat(chat_id)
            if str(chat_id).startswith("-100"):
                new_chat_id = str(chat_id)[4:]
            else:
                new_chat_id = str(chat_id)[1:]
            await bot.send_message(LOG_CHANNEL,LAN.GRUP_BILDIRIM.format(cmd.from_user.first_name, cmd.from_user.id, cmd.from_user.first_name, cmd.from_user.id, chat.title, cmd.chat.id, cmd.chat.id, cmd.message_id))

    ban_status = await db.get_ban_status(chat_id) # Yasaklı Kullanıcı Kontrolü
    if ban_status["is_banned"]:
        if int((datetime.date.today() - datetime.date.fromisoformat(ban_status["banned_on"])).days) > int(ban_status["ban_duration"]):
            await db.remove_ban(chat_id)
        else:
            if GROUP_SUPPORT:
                msj = f"@{GROUP_SUPPORT}"
            else:
                msj = f"[{LAN.SAHIBIME}](tg://user?id={OWNER_ID})"
            if cmd.chat.type == "private":
                await cmd.reply_text(LAN.PRIVATE_BAN.format(msj), quote=True)
            else:
                await cmd.reply_text(LAN.GROUP_BAN.format(msj),quote=True)
                await bot.leave_chat(cmd.chat.id)
            return
    await cmd.continue_propagation()




############### Broadcast araçları ###########
broadcast_ids = {}


async def send_msg(user_id, message): # Mesaj Gönderme
    try:
        if GONDERME_TURU is False:
            await message.forward(chat_id=user_id)
        elif GONDERME_TURU is True:
            await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(int(e.x))
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id}: {LAN.NOT_ONLINE}\n"
    except UserIsBlocked:
        return 400, f"{user_id}: {LAN.BOT_BLOCKED}\n"
    except PeerIdInvalid:
        return 400, f"{user_id}: {LAN.USER_ID_FALSE}\n"
    except Exception:
        return 500, f"{user_id}: {traceback.format_exc()}\n"

async def main_broadcast_handler(m, db): # Ana Broadcast Mantığı
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message
    while True:
        broadcast_id = "".join(random.choice(string.ascii_letters) for i in range(3))
        if not broadcast_ids.get(broadcast_id):
            break
    out = await m.reply_text(
        text=LAN.BROADCAST_STARTED)
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    broadcast_ids[broadcast_id] = dict(total=total_users, current=done, failed=failed, success=success)
    async with aiofiles.open("broadcast-logs-g4rip.txt", "w") as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(user_id=int(user["id"]), message=broadcast_msg)
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            if sts == 400:
                await db.delete_user(user["id"])
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(
                    dict(current=done, failed=failed, success=success))
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await asyncio.sleep(3)
    await out.delete()
    if failed == 0:
        await m.reply_text(text=LAN.BROADCAST_STOPPED.format(completed_in, total_users, done, success, failed), quote=True,)
    else:
        await m.reply_document(document="broadcast-logs-g4rip.txt", caption=LAN.BROADCAST_STOPPED.format(completed_in, total_users, done, success, failed), quote=True,)
    os.remove("broadcast-logs-g4rip.txt")



# Genelde müzik botlarının mesaj silme özelliği olur. Bu özelliği ReadMe.md dosyasındaki örnekteki gibi kullanabilirsiniz.
delcmdmdb = dcmdb.admins

async def delcmd_is_on(chat_id: int) -> bool: # Grup için mesaj silme özeliğinin açık olup olmadığını kontrol eder.
    chat = await delcmdmdb.find_one({"chat_id": chat_id})
    return not chat


async def delcmd_on(chat_id: int): # Grup için mesaj silme özeliğini açar.
    already_del = await delcmd_is_on(chat_id)
    if already_del:
        return
    return await delcmdmdb.delete_one({"chat_id": chat_id})


async def delcmd_off(chat_id: int): # Grup için mesaj silme özeliğini kapatır.
    already_del = await delcmd_is_on(chat_id)
    if not already_del:
        return
    return await delcmdmdb.insert_one({"chat_id": chat_id})



################# SAHİP KOMUTLARI #############

# Verileri listeleme komutu
@app.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def botstats(bot: Client, message: Message):
    g4rip = await bot.send_message(message.chat.id, LAN.STATS_STARTED.format(message.from_user.mention))
    all_users = await db.get_all_users()
    groups = 0
    pms = 0
    async for user in all_users:
        if str(user["id"]).startswith("-"):
            groups += 1
        else:
            pms += 1
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent
    total_users = await db.total_users_count()
    await g4rip.edit(text=LAN.STATS.format(BOT_USERNAME, total_users, groups, pms, total, used, disk_usage, free, cpu_usage, ram_usage, __version__), parse_mode="md")



# Botu ilk başlatan kullanıcıların kontrolünü sağlar.
@app.on_message()
async def G4RIP(bot: Client, cmd: Message):
    await handle_user_status(bot, cmd)



# Broadcast komutu
@app.on_message(filters.command("reklam") & filters.user(OWNER_ID) & filters.reply)
async def broadcast_handler_open(_, m: Message):
    await main_broadcast_handler(m, db)



# Bir kullanıcı yasaklama komutu
@app.on_message(filters.command("block") & filters.user(OWNER_ID))
async def ban(c: Client, m: Message):
    if m.reply_to_message:
        user_id = m.reply_to_message.from_user.id
        if len(m.command) <= 1:
            ban_duration = 9999
            ban_reason = LAN.BAN_REASON.format(BOT_USERNAME)
        elif len(m.command) == 2:
            ban_duration = 9999
            ban_reason = " ".join(m.command[1:])
    else:
        if len(m.command) <= 1:
            return await m.reply(LAN.NEED_USER)
        elif len(m.command) == 2:
            user_id = int(m.command[1])
            ban_duration = 9999
            ban_reason = LAN.BAN_REASON.format(BOT_USERNAME)
        elif len(m.command) == 3:
            user_id = int(m.command[1])
            ban_duration = 9999
            ban_reason = " ".join(m.command[2:])
    
        if str(user_id).startswith("-"):
            try:    
                ban_log_text = LAN.BANNED_GROUP.format(m.from_user.mention, user_id, ban_duration, ban_reason)
                await c.send_message(user_id, LAN.AFTER_BAN_GROUP.format(ban_reason))
                await c.leave_chat(user_id)
                ban_log_text += LAN.GROUP_BILGILENDIRILDI
            except BaseException:
                traceback.print_exc()
                ban_log_text += LAN.GRUP_BILGILENDIRILEMEDI.format(traceback.format_exc())
        else:
            try:    
                ban_log_text = LAN.USER_BANNED.format(m.from_user.mention, user_id, ban_duration, ban_reason)
                await c.send_message(user_id, LAN.AFTER_BAN_USER.format(ban_reason))
                ban_log_text += LAN.KULLANICI_BILGILENDIRME
            except BaseException:
                traceback.print_exc()
                ban_log_text += LAN.KULLANICI_BILGILENDIRMEME.format(traceback.format_exc())
        await db.ban_user(user_id, ban_duration, ban_reason)
        await c.send_message(LOG_CHANNEL, ban_log_text)
        await m.reply_text(ban_log_text, quote=True)



# Bir kullanıcın yasağını kaldırmak komutu
@app.on_message(filters.command("unblock") & filters.user(OWNER_ID))
async def unban(c: Client, m: Message):
        if m.reply_to_message:
            user_id = m.reply_to_message.from_user.id
        else:
            if len(m.command) <= 1:
                return await m.reply(LAN.NEED_USER)
            else:
                user_id = int(m.command[1])
        unban_log_text = LAN.UNBANNED_USER.format(m.from_user.mention, user_id)
        if not str(user_id).startswith("-"):
            try:
                await c.send_message(user_id, LAN.USER_UNBAN_NOTIFY)
                unban_log_text += LAN.KULLANICI_BILGILENDIRME
            except BaseException:
                traceback.print_exc()
                unban_log_text += LAN.KULLANICI_BILGILENDIRMEME.format(traceback.format_exc())
        await db.remove_ban(user_id)
        await c.send_message(LOG_CHANNEL, unban_log_text)
        await m.reply_text(unban_log_text, quote=True)



# Yasaklı listesini görme komutu
@app.on_message(filters.command("blocklist") & filters.user(OWNER_ID))
async def _banned_usrs(_, m: Message):
    all_banned_users = await db.get_all_banned_users()
    banned_usr_count = 0
    text = ""
    async for banned_user in all_banned_users:
        user_id = banned_user["id"]
        ban_duration = banned_user["ban_status"]["ban_duration"]
        banned_on = banned_user["ban_status"]["banned_on"]
        ban_reason = banned_user["ban_status"]["ban_reason"]
        banned_usr_count += 1
        text += LAN.BLOCKS.format(user_id, ban_duration, banned_on, ban_reason)
    reply_text = LAN.TOTAL_BLOCK.format(banned_usr_count, text)
    if len(reply_text) > 4096:
        with open("banned-user-list.txt", "w") as f:
            f.write(reply_text)
        await m.reply_document("banned-user-list.txt", True)
        os.remove("banned-user-list.txt")
        return
    await m.reply_text(reply_text, True)



############## BELİRLİ GEREKLİ DEF'LER ###########
def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "K", 2: "M", 3: "G", 4: "T"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"



########### ÇOKLU DİL ##############
class LAN(object):

    if LANGAUGE == "TR":

        BILDIRIM = "```📣 Yeni Bildirim``` \n\n#YENI_KULLANICI **botu başlattı!** \n\n🏷 isim: `{}` \n📮 kullanıcı id: `{}` \n🧝🏻‍♂️ profil linki: [{}](tg://user?id={})"
        GRUP_BILDIRIM = "```📣 Yeni Bildirim``` \n\n#YENI_GRUP **botu başlattı!** \n\n🏷 Gruba Alan İsim: `{}` \n📮 Gruba Alan kullanıcı id: `{}` \n🧝🏻‍♂️ profil linki: [{}](tg://user?id={})\n Grubun Adı: {}\n Grubun ID: {}\n Grubun Mesaj Linki( sadece açık gruplar): [Buraya Tıkla](https://t.me/c/{}/{})"
        SAHIBIME = "sahibime"
        PRIVATE_BAN = "Üzgünüm, yasaklandınız! Bunun bir hata olduğunu düşünyorsanız {} yazın."
        GROUP_BAN = "Üzgünüm, grubunuz karalisteye alındı! Burada daha fazla kalamam. Bunun bir hata olduğunu düşünyorsanız {} yazın.'"
        NOT_ONLINE = "aktif değil"
        BOT_BLOCKED = "botu engellemiş"
        USER_ID_FALSE = "kullanıcı kimliği yanlış"
        BROADCAST_STARTED = "```📤 BroadCast başlatıldı! Bittiği zaman mesaj alacaksınız!"
        BROADCAST_STOPPED = "✅ ```Broadcast başarıyla tamamlandı.``` \n\n**Şu Kadar Sürede Tamamlandı:** `{}` \n\n**Kayıtlı Toplam Kullanıcı:** `{}` \n\n**Toplam Gönderme Denemesi:** `{}` \n\n**Başarıyla Gönderilen:** `{}` \n\n**Toplam Hata:** `{}`"
        STATS_STARTED = "{} **Lütfen bekleyiniz verileri getiriyorum!**"
        STATS = """**@{} Verileri**\n\n**Kullanıcılar;**\n» **Toplam Sohbetler:** `{}`\n» **Toplam Gruplar: `{}`\n» **Toplam PM's: `{}`\n\n**Disk Kullanımı;**\n» **Disk Alanı:** `{}`\n» **Kullanılan:** `{}({}%)`\n» **Boşta:** `{}`\n\n**🎛 En Yüksek Kullanım Değerleri;**\n» **CPU:** `{}%`\n» **RAM:** `{}%`\n**Sürümler;**\n» **Pyrogram:** {}\n\n\n__• By @BasicBots__"""
        BAN_REASON = "Bu sebep yasaklandığınız için @{} tarafından otomatik olarak oluşturulmuştur"
        NEED_USER = "**Lütfen Kullanıcı kimliği verin.**"
        BANNED_GROUP = "🚷 **Yasaklandı!\n\nTarafından:** {}\n**Grup ID:** `{}` \n**Süre:** `{}` \n**Sebep:** `{}`"
        AFTER_BAN_GROUP = "**Üzgünüm grubunuz kara listeye alındı! \n\nSebep:** `{}`\n\n**Daha fazla burada kalamam. Bunun bir hata olduğunu düşünüyorsanız destek grubuna gelin.**"
        GROUP_BILGILENDIRILDI = "\n\n✅ **Grubu bilgilendirdim ve gruptan ayrıldım.**"
        GRUP_BILGILENDIRILEMEDI = "\n\n❌ **Grubu bilgilendirmeye çalışırken bir hata oluştu:** \n\n`{}`"
        USER_BANNED = "🚷 **Yasaklandı! \n\nTarafından:** {}\n **Kullanıcı ID:** `{}` \n**Süre:** `{}` \n**Sebep:** `{}`"
        AFTER_BAN_USER = "**Üzgünüm kara listeye alındınız! \n\nSebep:** `{}`\n\n**Bundan sonra size hizmet veremeyeceğim.**"
        KULLANICI_BILGILENDIRME = "\n\n✅ Kişiyi bilgilendirdim."
        KULLANICI_BILGILENDIRMEME = "\n\n❌ **Kişiyi bilgilendirmeye çalışırken bir hata oluştu:** \n\n`{}`"
        UNBANNED_USER = "🆓 **Kullanıcının Yasağı Kaldırıldı !** \nTarafından: {} \n**Kullanıcı ID:**{}"
        USER_UNBAN_NOTIFY = "🎊 Müjde! Yasağınız kaldırıldı!"
        BLOCKS = "🆔 **Kullanıcı ID**: `{}`\n⏱ **Süre**: `{}`\n🗓 **Yasaklanan Tarih**: `{}`\n💬 **Sebep**: `{}`\n\n"
        TOTAL_BLOCK = "🚷 **Toplam Yasaklanan:** `{}`\n\n{}"

    elif LANGAUGE == "AZ":

        BILDIRIM = "```📣 Yeni İsmarıc``` \n\n#YENI_ISTIFADƏÇİ **botu başlatdı!** \n\n🏷 isim: `{}` \n📮 istifadəçi id: `{}` \n🧝🏻‍♂️ profil linki: [{}](tg://user?id={})"
        GRUP_BILDIRIM = "```📣 Yeni İsmarıc``` \n\n#YENI_QRUP **botu başlatdı!** \n\n🏷 Qrupa əlavə edən: `{}` \n📮 Qrupa əlavə edən istifadəçi id: `{}` \n🧝🏻‍♂️ profil linki: [{}](tg://user?id={})\n Qrupun adı: {}\n Qrupun ID: {}\n Qrupun mesaj kinki( sadəcə açıq qruplar): [Buraya Toxun](https://t.me/c/{}/{})"
        SAHIBIME = "sahibimə"
        PRIVATE_BAN = "Məyusam, əngəlləndiniz! Bunun bir xəta olduğunu düşünürsünüz isə {} yazın."
        GROUP_BAN = "Məyusam, qrupunuz qara siyahıya əlavə olundu! Artıq burada qala bilmərəm! Bunun bir xəta olduğunu düşünürsünüz isə {} yazın.'"
        NOT_ONLINE = "aktiv deyil"
        BOT_BLOCKED = "botu əngəlləyib"
        USER_ID_FALSE = "istifadəçi id'i yanlışdır."
        BROADCAST_STARTED = "```📤 BroadCast başladıldı! Bitəndə mesaj alacaqsınız."
        BROADCAST_STOPPED = "✅ ```Broadcast uğurla tamamlandı.``` \n\n**Bu qədər vaxtda tamamlandı** `{}` \n\n**Ümumi istifadəçilər:** `{}` \n\n**Ümumi göndərmə cəhdləri:** `{}` \n\n**Uğurla göndərilən:** `{}` \n\n**Ümumi xəta:** `{}`"
        STATS_STARTED = "{} **Zəhmət olmasa gözləyin, bilgiləri gətirirəm!**"
        STATS = """**@{} Məlumatları**\n\n**İstifadəçiləri;**\n» **Ümumi söhbətlər:** `{}`\n» **Ümumi qruplar: `{}`\n» **Ümumi PM's: `{}`\n\n**Disk İstifadəsi;**\n» **Disk'in Sahəsi:** `{}`\n» **İstifadə edilən:** `{}({}%)`\n» **Boş qalan:** `{}`\n\n**🎛 Ən yüksək istifadə dəyərləri;**\n» **CPU:** `{}%`\n» **RAM:** `{}%`\n**Versiyalar;**\n» **Pyrogram:** {}\n\n\n__• By @BasicBots__"""
        BAN_REASON = "Bu sebep yasaklandığınız için @{} tarafından otomatik olarak oluşturulmuştur"
        NEED_USER = "**Zəhmət olmasa istifadəçi id'si verin.**"
        BANNED_GROUP = "🚷 **Qadağan olundu!\n\nQadağan edən:** {}\n**Qrup ID:** `{}` \n**Vaxt:** `{}` \n**Səbəb:** `{}`"
        AFTER_BAN_GROUP = "**Məyusam, qrupunyz qara siyahıya əlavə edildi! \n\nSəbəb:** `{}`\n\n**Artıq burada qala bilmərəm. Bunun bir xəta olduğunu düşünürsünüzsə, dətək qrupuna gəlin.**"
        GROUP_BILGILENDIRILDI = "\n\n✅ **Qrupu bilgiləndirdim və qrupdan çıxdım.**"
        GRUP_BILGILENDIRILEMEDI = "\n\n❌ **Qrupu məlumatlandırarkən xəta yarandı:** \n\n`{}`"
        USER_BANNED = "🚷 **Qadağan olundu! \n\nQadağan edən:** {}\n **İstifadəçi ID:** `{}` \n**Vaxt:** `{}` \n**Səbəb:** `{}`"
        AFTER_BAN_USER = "**Məyusam, qara siyahıya əlavə edildiniz! \n\nSəbəb:** `{}`\n\n**Bundan sonra sizə xidmət etməyəcəyəm.**"
        KULLANICI_BILGILENDIRME = "\n\n✅ İstifadəçini məlumatlandırdım."
        KULLANICI_BILGILENDIRMEME = "\n\n❌ **İstifadəçini məlumatlandırarkən xəta yarandı:** \n\n`{}`"
        UNBANNED_USER = "🆓 **İstifadəçinin qadağası qaldırıldı !** \nQadağanı qaldıran: {} \n**İstifadəçi ID:**{}"
        USER_UNBAN_NOTIFY = "🎊 Sizə gözəl bir xəbərim var! Artıq əngəliniz qaldırıldı!"
        BLOCKS = "🆔 **İstifadəçi ID**: `{}`\n⏱ **Vaxt**: `{}`\n🗓 **Qadağan edildiyi tarix**: `{}`\n💬 **Səbəb**: `{}`\n\n"
        TOTAL_BLOCK = "🚷 **Ümumi əngəllənən:** `{}`\n\n{}"
	

	
@app.on_message(filters.command("delcmd") & ~filters.private)
async def delcmdc(bot: Client, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("Bu əmrdən istifadə etmək üçün əmrinizin yanında 'off' və ya 'on' yazın.")
    durum = message.text.split(None, 1)[1].strip()
    durum = durum.lower()
    chat_id = message.chat.id

    if durum == "on":
        if await delcmd_is_on(message.chat.id):
            return await message.reply_text("Komandanın Silinməsi Artıq Aktivdir.")
        else:
            await delcmd_on(chat_id)
            await message.reply_text("Bu söhbət üçün Sil əmri uğurla aktivləşdirildi.")

    elif durum == "off":
        await delcmd_off(chat_id)
        await message.reply_text("Komanda Silmə funksiyası bu Söhbət üçün uğurla deaktiv edildi.")
    else:
        await message.reply_text("Bu əmrdən istifadə etmək üçün əmrinizin yanında 'off' və ya 'on' yazın.")

rehim = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)



@rehim.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.reply(f"**👋 Salam {mention} Mən OLD MULTİ BOT bir cox funksyaya malik OLD MULTİ botam\n\n🤔 Botun isdifade qaydasın bilmirsen indi ise '🎛 ƏMRLƏR' bölməsinə daxil olun\n\n✉️ Botu başladıqına dayir Sahibime mesaj yolladım**", buttons=(
                     [Button.inline("🎛 ƏMRLƏR", data="emir")],
       # [Button.url('🎉 Sahib', 'https://t.me/Nehmedov')],
              # [Button.url('Qurup🛠', 'https://t.me/Bizim_Paytaxt'),
                    #  Button.url('💡 USTA Bots', 'https://t.me/ustabots')],
               [Button.url('➕ Qrupa Əlavə Et ➕','http://t.me/OldMultiBot?startgroup=a'),
                Button.url('🎴 KANALIM','http://t.me/TEAMABASOFcom')],
               [Button.url("🌟 SAHİB",'https://t.me/AnonyumAz'),
                      Button.url('📂 APK','http://t.me/texnoapk1')],
                    ),
                    link_preview=False)


  if event.is_group:
    return await client.send_message(event.chat_id, f"**Əziz isdifadeçi Qroupda cox yazmaqla başınızı ağrıtmıyım Bota Keç vuraraq şexside melumat ala bilersiz**", buttons=(
                     [Button.url('💡 Bota Keç','https://t.me/OldMultiBot?start=start')],
                    ),
                    link_preview=False)



@rehim.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.edit(f"**👋 Salam {mention} Mən OLD MULTİ BOT bir cox funksyaya malik OLD MULTİ botam\n\n🤔 Botun isdifade qaydasın bilmirsen indi ise '🎛 ƏMRLƏR' bölməsinə daxil olun\n\n✉️ Botu başladıqına dayir Sahibime mesaj yolladım**", buttons=(
                     [Button.inline(f"🎛 ƏMRLƏR", data="emir")],
        # [Button.url('🎉 Sahib', 'https://t.me/Nehmedov')],
               #[Button.url('Qurup🛠', 'https://t.me/Bizim_Paytaxt'),
                      #Button.url('🤖 USTA Bots', 'https://t.me/ustabots')],
               [Button.url('➕ Qrupa Əlavə Et ➕','http://t.me/OldMultiBot?startgroup=a'),
                Button.url('🎴 KANALIM','http://t.me/TEAMABASOFcom')],
               [Button.url('🌟 SAHİB','https://t.me/AnonyumAz'),
                      Button.url('📂 APK', 'https://t.me/texnoapk1')],
                    ),
                    link_preview=False)

@rehim.on(events.callbackquery.CallbackQuery(data="emir"))
async def handler(event):
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.edit(f"**🤩 Siz artıq ƏMRLƏR bölümündesiz\n\n🫡 Hansı əmri isdəsəniz aşağıda Buttonla vuraraq baxa bilersiz\n\n🩶 XOŞ İSDİFADELER @OldMultiBot**", buttons=(
                     [Button.inline("🌟 ADMİN ƏMRLƏR", data="admin")],
        # [Button.url('🎉 Sahib', 'https://t.me/Nehmedov')],
               #[Button.url('Qurup🛠', 'https://t.me/Bizim_Paytaxt'),
                      #Button.url('🤖 USTA Bots', 'https://t.me/ustabots')],
               [Button.inline(f"📮 TAG ƏMRLƏRİ", data="thelp"),
                Button.inline(f"📥 YÜKLƏMƏ", data="yhelp")],
               [Button.inline(f"🕹 GAME", data="dhelp"),
                      Button.inline(f"➕️ ƏLAVƏLƏR", data="elave")],
	       [Button.inline(f"🔙 Geri", data="start")]
                    ),
                    link_preview=False)

# rehim / abasof
@rehim.on(events.callbackquery.CallbackQuery(data="thelp"))
async def handler(event): 
    await event.edit(f"**[@OldMultiBot](http://t.me/OldMultiBot)-un '📮TAG ƏMRLƏR' bölməsi ⤵**\n\n\n•━━━━━━━━•••━━━━━━━━•\n**🤖➪ /admin - Group adminlərin tag edir**\n•━━━━━━━━•••━━━━━━━━•", buttons=(
              # [Button.url('➕ Məni Qrupa əlavə et ➕','http://t.me/UstaTagbot?startgroup=a')],
         #[Button.url('🎉 Sahib', 'https://t.me/Nehmedov')],
               [Button.url('🔮 Kanalım','https://t.me/TEAMABASOFcom'),
                      Button.url('📂 APK','https://t.me/texnoapk1')],
               [Button.inline(f"🔙 Geri", data="emir")]
                    ),
                    link_preview=False)

@rehim.on(events.callbackquery.CallbackQuery(data="yhelp"))
async def handler(event): 
    await event.edit(f"**[@OldMultiBot](http://t.me/OldMultiBot)-un '📥 YÜKLƏMƏ' bölməsi ⤵**\n\n\n•━━━━━━━━•••━━━━━━━━•\n**🎵 ➪  /song - MAHNI YÜKLƏYİR**\n**📽 ➪ /video və ya /vsong - İsdədiyiniz videonu Youtub dan yükləyər\n**⛓️ ➪ Telegrap - Bota şexside photo,video,gif ataraq telegrap linki ala bilersiz Əmir şəxsidə çalışır**\n•━━━━━━━━•••━━━━━━━━•", buttons=(
              # [Button.url('➕ Məni Qrupa əlavə et ➕','http://t.me/UstaTagbot?startgroup=a')],
         #[Button.url('🎉 Sahib', 'https://t.me/Nehmedov')],
               [Button.url('🔮 Kanalım','https://t.me/TEAMABASOFcom'),
                      Button.url('📂 APK','https://t.me/texnoapk1')],
               [Button.inline(f"🔙 Geri", data="emir")]
                    ),
                    link_preview=False)

@rehim.on(events.callbackquery.CallbackQuery(data="dhelp"))
async def handler(event): 
    await event.edit(f"**[@OldMultiBot](http://t.me/OldMultiBot)-un '🕹 GAME' bölməsi ⤵**\n\n\n•━━━━━━━━•••━━━━━━━━•\n**☸️ ➪ /dc - Doğruluq Və Cəsarət oyunu basladır**\n**🎲 ➪ /zer - Zər atar**\n**🎯 ➪ /ox - Ox atar**\n**⚽️ ➪ /gol - Goal atar**\n**🎰 ➪ /spin - Spin cevir**\n**🏀 ➪ /basket - Basket atar**\n**🎳 ➪ /bowling - Bowling atar**\n•━━━━━━━━•••━━━━━━━━•", buttons=(
              # [Button.url('➕ Məni Qrupa əlavə et ➕','http://t.me/UstaTagbot?startgroup=a')],
         #[Button.url('🎉 Sahib', 'https://t.me/Nehmedov')],
               [Button.url('🔮 Kanalım','https://t.me/TEAMABASOFcom'),
                      Button.url('📂 APK','https://t.me/texnoapk1')],
               [Button.inline(f"🔙 Geri", data="emir")]
                    ),
                    link_preview=False)

@rehim.on(events.callbackquery.CallbackQuery(data="elave"))
async def handler(event): 
    await event.edit(f"**[@OldMultiBot](http://t.me/OldMultiBot)-un '➕️ ƏLAVƏLƏR' bölməsi ⤵**\n\n\n•━━━━━━━━•••━━━━━━━━•\n**🪪 ➪ /info - Kullanıcı melumat getirii**\n**📈 ➪ /ping - Botun pingin ölçür**\n**🎚 ➪ /alive Botun aktiv olmaqın gosterir Sahib isdifade ede biler**\n**😔 ➪ /sehid - şəhid adları atır**\n**🤖 ➪ /anekdod - Random anekdod atar**\n**🤖 ➪ /meslehet - Botdan Məsləhət alin**\n**🤖 ➪ /carbon - Mətini carbona dönüşdür (Qroupda isliyir)**\n**🤖 ➪ /tema - Random Telegram Teması atar (Qroupda isliyir)**\n**👋 ➪ salamlama - Groupa qatılanlara xoş geldin deyir**\n•━━━━━━━━•••━━━━━━━━•", buttons=(
              # [Button.url('➕ Məni Qrupa əlavə et ➕','http://t.me/UstaTagbot?startgroup=a')],
         #[Button.url('🎉 Sahib', 'https://t.me/Nehmedov')],
               [Button.url('🔮 Kanalım','https://t.me/TEAMABASOFcom'),
                      Button.url('📂 APK','https://t.me/texnoapk1')],
               [Button.inline(f"🔙 Geri", data="emir")]
                    ),
                    link_preview=False)

@rehim.on(events.callbackquery.CallbackQuery(data="admin"))
async def handler(event): 
    await event.edit(f"**[@OldMultiBot](http://t.me/OldMultiBot)-un '🌟 ADMİN ƏMRLƏRİ' bölməsi ⤵**\n\n\n•━━━━━━━━•••━━━━━━━━•\n**🌟 ➪ /pin - test**\n**🌟 ➪ /unpin - test**\n•━━━━━━━━•••━━━━━━━━•", buttons=(
              # [Button.url('➕ Məni Qrupa əlavə et ➕','http://t.me/UstaTagbot?startgroup=a')],
         #[Button.url('🎉 Sahib', 'https://t.me/Nehmedov')],
               [Button.url('🔮 Kanalım','https://t.me/TEAMABASOFcom'),
                      Button.url('📂 APK','https://t.me/texnoapk1')],
               [Button.inline(f"🔙 Geri", data="emir")]
                    ),
                    link_preview=False)

 # Gerekli silmeyiniz. 
anlik_calisan = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}

@rehim.on(events.NewMessage(pattern="^/admim ?(.*)"))
async def mentionalladmin(event):
  global anlik_calisan 
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("Bu əmr sadəcə grup vəya kanallarda isdifadə edilə bilər.")
  
  admins = []
  async for admin in rehim.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmri sadəcə yönəticilər isdifadə edə bilər.**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Köhnə mesajlar üçün Kişilərdən bəhs edənmərəm! (qrouba əlavə etmədən öncə olan mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**Tag etməyə Başlamaq üçün səbəb yazın... ✋\n\n(Məsələn: /yt Salam necəsən!)**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Tag prosesi başladı.**")
        
    async for usr in rehim.iter_participants(event.chat_id,filter=ChannelParticipantsAdmins):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}),"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await rehim.send_message(event.chat_id, f"📢 ~ **{msg}**\n\n{usrtxt}")
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"{sender.first_name}"      
    if event.chat_id in rxyzdev_tagTot:
           a = await event.respond(f"**✅ Tag prosesi uğurla dayandırıldı.**\n\n**Tag olunan Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}")
           await sleep(10)
           await a.delete()

  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in rehim.iter_participants(event.chat_id,filter=ChannelParticipantsAdmins):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}),"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await rehim.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"{sender.first_name}"      
    if event.chat_id in rxyzdev_tagTot:
           a = await event.respond(f"**✅ Tag prosesi uğurla dayandırıldı.**\n\n**Tag olunan Kişi Sayısı:** {rxyzdev_tagTot[event.chat_id]}")
           await sleep(10)
           await a.delete()
       
 

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
@app.on_message(filters.command("song") & ~filters.edited)
def bul(_, message):
    query = " ".join(message.command[1:])
    m = message.reply("<b>Musiqi Axtarılır ... 🔍</b>")
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
        m.edit("İstədiyiniz musiqi tapılmadı 😔")
        print(str(e))
        return
    m.edit("`📥 Musiqini tapdım və endirirəm.`")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"🎵 Yüklədi [Music Bot](https://t.me/{Config.BOT_USERNAME})"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("📤 Yüklənir..")
        message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name, performer="MusicAzPlaylist")
        m.delete()
        bot.send_audio(chat_id=Config.PLAYLIST_ID, audio=audio_file, caption=rep, performer="@MusicAzBot", parse_mode='md', title=title, duration=dur, thumb=thumb_name)
    except Exception as e:
        m.edit('**⚠️ Gözlənilməyən xəta yarandı.**\n**Xahiş edirəm xətanı sahibimə xəbərdar et!**')
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)


# video indirme 

@app.on_message(
    filters.command(["video", "vsong"]) & ~filters.edited
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

 

#telethon xos geldin mesaj 
@rehim.on(events.ChatAction) 
async def handler(event): # Welcome every new user 
    if event.user_joined: 
       await event.reply('Salam xos geldiniz groupa!')



@app.on_message(filters.command("ping"))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")



@app.on_message(filters.private & filters.photo)
async def uploadphoto(client, message):
  msg = await message.reply_text("`Tʀʏɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅ`")
  userid = str(message.chat.id)
  img_path = (f"./DOWNLOADS/{userid}.jpg")
  img_path = await client.download_media(message=message, file_name=img_path)
  await msg.edit_text("`Tʀʏɪɴɢ Tᴏ Uᴘʟᴏᴀᴅ.....`")
  try:
    tlink = upload_file(img_path)
  except:
    await msg.edit_text("`Something went wrong`") 
  else:
    await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
    os.remove(img_path) 

@app.on_message(filters.private & filters.photo)
async def uploadgif(client, message):
  if(message.animation.file_size < 5242880):
    msg = await message.reply_text("`Tʀʏɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅ`")
    userid = str(message.chat.id)
    gif_path = (f"./DOWNLOADS/{userid}.mp4")
    gif_path = await client.download_media(message=message, file_name=gif_path)
    await msg.edit_text("`Tʀʏɪɴɢ Tᴏ Uᴘʟᴏᴀᴅ.....`")
    try:
      tlink = upload_file(gif_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")   
      os.remove(gif_path)   
    except:
      await msg.edit_text("Something really Happend Wrong...") 
  else:
    await message.reply_text("Size Should Be Less Than 5 mb")

@app.on_message(filters.private & filters.photo)
async def uploadvid(client, message):
  if(message.video.file_size < 5242880):
    msg = await message.reply_text("`Tʀʏɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅ`")
    userid = str(message.chat.id)
    vid_path = (f"./DOWNLOADS/{userid}.mp4")
    vid_path = await client.download_media(message=message, file_name=vid_path)
    await msg.edit_text("`Tʀʏɪɴɢ Tᴏ Uᴘʟᴏᴀᴅ.....`")
    try:
      tlink = upload_file(vid_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
      os.remove(vid_path)   
    except:
      await msg.edit_text("Something really Happend Wrong...") 
  else:
    await message.reply_text("Size Should Be Less Than 5 mb")



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


@app.on_message(filters.command(["alive"]))
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


@app.on_message(filters.command("sehid") & ~filters.edited)
async def commit(_, message):
    await message.reply_text((await random_line('AykhanPro/txt/sehid.txt')))
				
@app.on_message(filters.command("meslehet") & ~filters.edited)
async def meslehet(_, message):
    await message.reply_text((await random_line('AykhanPro/txt/meslehet.txt')))


@app.on_message(filters.command("anekdod") & ~filters.edited)
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


#Cahildi carbon code


aiohttpsession = ClientSession()


async def get_http_status_code(url: str) -> int:
    async with aiohttpsession.head(url) as resp:
        return resp.status
    

async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with aiohttpsession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image

@app.on_message(filters.command("carbon"))
async def carbon_func(bot: app, msg: Message):
    m = await msg.reply_text("`Hazırlanır`")
    carbon = await make_carbon(msg.reply_to_message.text)
    await m.edit("`Göndərilir`")
    await bot.send_photo(msg.chat.id, photo=carbon)
    await m.delete()
    carbon.close()



@app.on_message(filters.command("tema"))
async def tema(app: Client, msg: Message):
    await msg.reply(random.choice(temalar))


#@(events.NewMessage(pattern='/reklam'))
#async def handler(event):	
 #    await event.reply('🤖 [USTA Tag Bot](http://t.me/UstaTagbot)-unda Reklam Almaq Üzçün [ɴᴀᴋʜɪᴅ ᴜsᴛᴀ ¦ 🇧🇻🦅](https://t.me/UstaNakhid)-ilə Әlaqә Saxlayın.')
 

print(">> Bot işləyir narahat olmayın. @edalet_22 Məlumat almaq üçün <<")
app.start()
rehim.run_until_disconnected()
