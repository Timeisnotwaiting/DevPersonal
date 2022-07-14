from pyrogram import Client, filters, idle
import config 

Dev = Client(s_n = config.STRING, a_i = config.API_ID, a_h = config.API_HASH, plugins=dict(root="Deadbody"))
