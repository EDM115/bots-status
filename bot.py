# (c) @xditya
# This file is a part of https://github.com/xditya/BotStatus

import pytz
import logging
import asyncio
from time import sleep
from datetime import datetime as dt
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.errors.rpcerrorlist import MessageNotModifiedError, FloodWaitError, AuthKeyDuplicatedError
from decouple import config
from telethon.sessions import StringSession
from telethon import TelegramClient

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)

try:
    appid = config("APP_ID")
    apihash = config("API_HASH")
    session = config("SESSION", default=None)
    chnl_id = config("CHANNEL_ID", cast=int)
    msg_id = config("MESSAGE_ID", cast=int)
    botlist = config("BOTS")
    bots = botlist.split()
    session_name = str(session)
    user_bot = TelegramClient(StringSession(session_name), appid, apihash)
    logging.info("\n\nStarted ☺️\nVisit @EDM115bots")
except Exception as e:
    logging.info(f'ERROR\n{e}')


async def BotzHub():
    async with user_bot:
        while True:
            logging.info("[INFO] starting to check uptime…")
            try:
                await user_bot.edit_message(
                    int(chnl_id),
                    msg_id,
                    "@EDM115 bots status\n\n`Performing a periodic check… ⏳`",
                )
            except MessageNotModifiedError:
                pass
            c = 0
            edit_text = "@EDM115 bots status\n\n**Heyo everyone 🥺**\nHere is the list of my bots, and if they are running or no :\n\n"
            for bot in bots:
                try:
                    logging.info(f"[INFO] checking @{bot}")
                    snt = await user_bot.send_message(bot, "/start")
                    await asyncio.sleep(10)

                    history = await user_bot(
                        GetHistoryRequest(
                            peer=bot,
                            offset_id=0,
                            offset_date=None,
                            add_offset=0,
                            limit=1,
                            max_id=0,
                            min_id=0,
                            hash=0,
                        )
                    )

                    msg = history.messages[0].id
                    if snt.id == msg:
                        logging.info(f"@{bot} is down")
                        edit_text += f"`@{bot}` • **❌ Offline for the moment, come back later**\n"
                    elif snt.id + 1 == msg:
                        edit_text += f"@{bot} • **✅ Up & online**\n"
                    await user_bot.send_read_acknowledge(bot)
                    c += 1
                except FloodWaitError as f:
                    logging.info(f"Floodwait !\n\nSleeping for {f.seconds}…")
                    sleep(f.seconds + 10)
            await user_bot.edit_message(int(chnl_id), int(msg_id), edit_text)
            k = pytz.timezone("Europe/Paris")
            month = dt.now(k).strftime("%B")
            day = dt.now(k).strftime("%d")
            year = dt.now(k).strftime("%Y")
            t = dt.now(k).strftime("%H:%M:%S")
            edit_text += f"\n__Last check :__ \n`{t} • {day} {month} {year} [UTC+1]`\n__(bots status are auto-updated every hour ☺️)__\n\nYou can dm me here if there’s any problem : **@EDM115**\nHave a good day, and subscribe for more news about the existing bots updates and the upcoming ones… 😏💓"
            await user_bot.edit_message(int(chnl_id), int(msg_id), edit_text)
            logging.info(f"Checks since latest restart : {c}")
            logging.info("Sleeping for 1 hour") # we use workflows here
            if c != 0:
                break

try:
    user_bot.loop.run_until_complete(BotzHub())
    user_bot.disconnect()   # try prevent AuthKeyDuplicatedError
except AuthKeyDuplicatedError:
    logging.warning("Session string expired. Create a new one")

logging.info("\nProcess Completed Successfully 😌")
