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

DEV = TelegramClient(StringSession(STRING), API_ID, API_HASH)

@DEV.on(events.NewMessage(outgoing=True, pattern="!on"))
async def _(event):
    on()
    await event.edit("Message forwarding process is starting")
    await asyncio.sleep(2)
    await event.edit("Process started, check log group")

@DEV.on(event.NewMessage(incoming=True))
async def smexy(event):
    if event.is_private:
        if event.message.text:
            entity = await DEV.get_entity(event.sender_id)
            name = get_display_name(entity)
            hehe = nayantara(name, event.sender_id)
            lm = f"#PM\n\n{hehe}\n\n{event.message}"
            await event.client.send_message(LOG, lm)
        
