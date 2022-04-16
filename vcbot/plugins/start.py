import asyncio
from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME, UPDATES_CHANNEL, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**
🖤 𝗛𝗲𝗹𝗹𝗼 {message.from_user.mention()} !
         𝗜 𝗔𝗺 [{bn}](t.me/{bu}) 𝗜 𝗰𝗮𝗻 𝗽𝗹𝗮𝘆 𝗺𝘂𝘀𝗶𝗰 𝗶𝗻 𝘃𝗰 🤍
         𝘀𝗼 .... 𝗔𝗱𝗱 𝗺𝗲 𝗶𝗻 𝘆𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽...!!
━━━━━━━━━━━━━━━━━━
💞 𝗠𝘆 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 - @HeroX_xD
━━━━━━━━━━━━━━━━━━

💞 𝗜𝗙 𝘆𝗼𝘂 𝗵𝗮𝘃𝗲 𝗮𝗻𝘆 𝗾𝘂𝗲𝘀𝘁𝗶𝗼𝗻 𝘁𝗵𝗲𝗻 𝗗𝗠 𝗺𝘆 [𝗢𝗪𝗡𝗘𝗥](t.me/{OWNER_USERNAME}) ʙᴀʙʏ...
**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• 𝗔𝗱𝗱 𝗺𝗲 𝗶𝗻 𝘆𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "• 𝗢𝗪𝗡𝗘𝗥", url=f"https://t.me/{OWNER_USERNAME}"
                    ),
                    InlineKeyboardButton(
                        "• 𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "• 𝗨𝗽𝗱𝗮𝘁𝗲𝘀", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )],[ 
                    InlineKeyboardButton(
                        "• 𝗦𝗼𝘂𝗿𝗰𝗲 𝗰𝗼𝗱𝗲", url="https://github.com/SJMxADITI/Vc-Bot"
                    )]
            ]
       ),
    )
