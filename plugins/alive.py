import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_IMAGE, BOT_USERNAME, OWNER_USERNAME, UPDATES_CHANNEL, SUPPORT_GROUP, SOURCE_CODE
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""**• ━━━━━━━━━━━━━━━━━━━━━━━━ •
• Hᴇʟʟᴏ I Aᴍ SᴜᴘᴇʀFᴀsᴛ Hɪɢʜ Qᴜᴀʟɪᴛʏ Nᴏ Lᴀɢ VC Mᴜsɪᴄ Pʟᴀʏᴇʀ Bᴏᴛ •

┏━━━━━━━━━━━━━━━━━━━━━━┓
┣❥︎ • Oᴡɴᴇʀ •   » [• Cʟɪᴄᴋ Hᴇʀᴇ •](https://t.me/{OWNER_USERNAME})

┣❥︎ Uᴘᴅᴀᴛᴇs ➪ » [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞]({UPDATES_CHANNEL})
┣❥︎ Sᴜᴘᴘᴏʀᴛ ➪ » [• Cʟɪᴄᴋ Hᴇʀᴇ •]({SUPPORT_GROUP})

┗━━━━━━━━━━━━━━━━━━━━━━┛

• Jᴜsᴛ Aᴅᴅ Mᴇ ➾ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Eɴᴊᴏʏ Sᴜᴘᴇʀ Qᴜᴀʟɪᴛʏ ⬙Mᴜsɪᴄ •
• ━━━━━━━━━━━━━━━━━━━━━━━━ •**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ •", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", f"start@{BOT_USERNAME}", "/alive", ".alive", "#bikash", "#aditya"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " • Jᴏɪɴ Oᴜʀ Cʜᴀᴛ Gʀᴏᴜᴘ •", url=f"{SUPPORT_GROUP}")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "bikash", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/64dcf7da559b7021edbc3.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• Cʟɪᴄᴋ Mᴇ Tᴏ Gᴇᴛ Rᴇᴘᴏ •", url=f"{SOURCE_CODE}")
                ]
            ]
        ),
    )
