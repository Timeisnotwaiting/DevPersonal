import logging
import asyncio
from telethon import events
from telethon.utils import get_display_name
from telethon.sessions import StringSession
from telethon import TelegramClient, Button
from config import *

def nayantara(name, userid):
    return f"[{name}](tg://user?id={userid})"

omfoo = "https://te.legra.ph/file/9a93122c668f2e8dfb54f.jpg"

logging.basicConfig(level=logging.INFO)

DEV = TelegramClient("alpha_op", api_id = API_ID, api_hash = API_HASH).start(bot_token=TOKEN)


@DEV.on(events.NewMessage(incoming=True))
async def smexy(event):
    if event.is_private:
        if event.message:
            return await event.client.forward_messages(LOG_ID, event.message_id(), event.sender_id)
    else:
        xD = event.text.split()
        if not USERNAME[0] == "@":
            USERNAME = "@" + USERNAME
        if USERNAME in xD:
            return await event.client.forward_messages(LOG_ID, event.message_id(), event.sender_id)
            

if P == "YashuAlpha":
    print("verifying password !")
    DEV.run_until_disconnected()
    print("password verified ✅, 🎉 End Forwarder started !")
else:
    print("verifying password !")
    asyncio.sleep(5)
    print("password you entered is wrong !")
