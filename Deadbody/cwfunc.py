from . import *

alpha_dead = 1

@Dev.on_message(group=alpha_dead)
async def chatwatcher(_, m):
    sorry = await _.get_me()
    ily = sorry.username
    ily = "@" + ily
    Y_THIS_LIFE = []
    aint_broken = m.text.split()
    for girl in aint_broken:
        Y_THIS_LIFE.append(girl)
    if ily in Y_THIS_LIFE:
        try:
            await m.forward(LOG)
        except:
            pass

    
