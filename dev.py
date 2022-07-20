import logging
import asyncio
from telethon import events
from telethon.tl.functions.messages import ForwardMessagesRequest
from telethon.utils import get_display_name
from telethon import TelegramClient, Button
from config import *

def nayantara(name, userid):
    return f"[{name}](tg://user?id={userid})"

omfoo = "https://te.legra.ph/file/9a93122c668f2e8dfb54f.jpg"

logging.basicConfig(level=logging.INFO)

DEV = TelegramClient("alpha_op", api_id = API_ID, api_hash = API_HASH).start(bot_token=TOKEN)

@DEV.on(events.NewMessage(incoming=True, pattern="/start"))
async def _(e):
    if e.sender_id == 1985209910:
        await e.reply("alive !")

@DEV.on(events.NewMessage(incoming=True))
async def smexy(event):
    global USERNAME
    if event.is_private:
        return
    else:
        xD = event.text.split()
        if not USERNAME[0] == "@":
            USERNAME = "@" + USERNAME
        if USERNAME in xD:
            return await event.client(ForwardMessagesRequest(event.sender_id, event.message_id, LOG_ID)) 
            

if P == "YashuAlpha":
    print("verifying password !\n\npassword verified ✅, 🎉 End Forwarder started !")
    try:
        DEV.run_until_disconnected()
    except:
        print("Telethon connection error !, try after some time ")
        pass
else:
    print("verifying password !")
    try:
        asyncio.sleep(5)
    except:
        pass
    print("password you entered is wrong !")
