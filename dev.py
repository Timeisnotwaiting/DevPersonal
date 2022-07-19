import logging

from telethon import events
from telethon.sessions import StringSession
from telethon import TelegramClient, Button
from config import *

omfoo = "https://te.legra.ph/file/9a93122c668f2e8dfb54f.jpg"

logging.basicConfig(level=logging.INFO)

DEV = TelegramClient(StringSession(STRING), API_ID, API_HASH)

