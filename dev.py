from pyrogram import Client, filters, idle
import config 

Dev = Client(config.STRING, api_id = config.API_ID, api_hash = config.API_HASH, plugins=dict(root="Deadbody"))

if config.P != "R_a_Y":
    print("wrong password Bruhh !")
else:
    Dev.start()
    Dev.idle()
    print("done vro !, made in pain")
    print("I'm Alive !")
