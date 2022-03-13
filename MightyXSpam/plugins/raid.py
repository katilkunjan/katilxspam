
import asyncio
import base64
import os
import random
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from MightyXSpam import Mig, Mig2, Mig3, Mig4, Mig5 , Mig6, Mig7, Mig8, Mig9, Mig10, SUDO_USERS, OWNER_ID
from resources.data import RAID, REPLYRAID, MightyX
from MightyXSpam import CMD_HNDLR as hl


que = {}


@Mig.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Mig2.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Mig3.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Mig4.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Mig5.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Mig6.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Mig7.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Mig8.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Mig9.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@Mig10.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n{hl}raid <count> <Username of User>\n\n{hl}raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Mighty = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(Mighty) == 2:
            user = str(Mighty[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in MightyX:
                text = f"I Can't Raid on katil"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"This Guy Is Owner Of These Bots."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This Guy is a Sudo User."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(Mighty[0])
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.5)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in MightyX:
                text = f"I Can't Raid on katil"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"This Guy Is Owner Of These Bots."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This Guy is a Sudo us6er."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = b.first_name
                counter = int(Mighty[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)



@Mig.on(events.NewMessage(incoming=True))
@Mig2.on(events.NewMessage(incoming=True))
@Mig3.on(events.NewMessage(incoming=True))
@Mig4.on(events.NewMessage(incoming=True))
@Mig5.on(events.NewMessage(incoming=True))
@Mig6.on(events.NewMessage(incoming=True))
@Mig7.on(events.NewMessage(incoming=True))
@Mig8.on(events.NewMessage(incoming=True))
@Mig9.on(events.NewMessage(incoming=True))
@Mig10.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(REPLYRAID)),
            reply_to=event.message.id,
        )


@Mig.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Mig2.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Mig3.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Mig4.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Mig5.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Mig6.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Mig7.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Mig8.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Mig9.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Mig10.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
async def _(e):
    global que
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n{hl}replyraid <Username of User>\n\n{hl}replyraid <reply to a User>."
    if e.sender_id in SUDO_USERS:
        Mighty = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        Migx = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(Mighty[0])
            a = await e.client.get_entity(message)
            user_idd = a.id
            user_id = int(user_idd)
            if int(user_id) in MightyX:
                text = f"I Can't Raid on katil."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                text = f"This Guy is Owner Of These Bots."            
                await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"This Guy is a Sudo User."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"Activated ReplyRaid...😈"
                await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            umser = await e.client.get_entity(a.sender_id)
            user_idd = umser.id
            user_id = int(user_idd)
            if int(user_id) in MightyX:
                text = f"I Can't Raid on MightyX's Owner."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                text = f"This Guy is Owner Of These Bots."
                await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"This Guy is a Sudo User."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"Activated ReplyRaid...😈"
                await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)


@Mig.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Mig2.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Mig3.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Mig4.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Mig5.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Mig6.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Mig7.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Mig8.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Mig9.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@Mig10.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
async def _(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n{hl}dreplyraid <Username of User>\n\n{hl}dreplyraid <reply to a User>"
    global que    
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Migoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(Migoel[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "Reply Raid De-Activated 🌚"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "Reply Raid De-Activated 🌚"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
@Mig.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Mig2.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Mig3.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Mig4.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Mig5.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Mig6.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Mig7.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Mig8.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Mig9.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Mig10.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
async def _(event):
   usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗘𝗟𝗔𝗬𝗥𝗔𝗜𝗗\n\nCommand:\n\n{hl}delayraid <delay> <count> <Username of User>\n\n{hl}delayraid <delay> <count> <reply to a User>\n\nCount and Sleeptime must be a integer."        
   if event.sender_id in SUDO_USERS:
         if event.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
         Mighty = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
         if len(Mighty) == 3:
             user = str(Mighty[2])
             a = await event.client.get_entity(user)
             e = a.id
             if int(e) in MightyX:
                    text = f"I Can't Raid on katil"
                    await event.reply(text, parse_mode=None, link_preview=None )
             elif int(e) == OWNER_ID:
                text = f"This Guy is Owner Of These Bots."
                await event.reply(text, parse_mode=None, link_preview=None )
             elif int(e) in SUDO_USERS:
                    text = f"This Guy is a Sudo User."
                    await event.reply(text, parse_mode=None, link_preview=None )
             else:
                 c = a.first_name
                 username = f"[{c}](tg://user?id={e})"
                 counter = int(Mighty[1])
                 sleeptimet = sleeptimem = float(Mighty[0])
                 for _ in range(counter):
                      reply = random.choice(RAID)
                      caption = f"{username} {reply}"
                      async with event.client.action(event.chat_id, "typing"):
                          await event.client.send_message(event.chat_id, caption)
                          await asyncio.sleep(sleeptimem)
         elif event.reply_to_msg_id:
               a = await event.get_reply_message()
               b = await event.client.get_entity(a.sender_id)
               e = b.id
               if int(e) in MightyX:
                       text = f"I Can't Raid on katil"
                       await event.reply(text, parse_mode=None, link_preview=None )
               elif int(e) == OWNER_ID:
                       text = f"This Guy is Owner Of These Bots."
                       await event.reply(text, parse_mode=None, link_preview=None )
               elif int(e) in SUDO_USERS:
                       text = f"This Guy is a Sudo User."
                       await event.reply(text, parse_mode=None, link_preview=None )
               else:
                   c = b.first_name
                   username = f"[{c}](tg://user?id={e})"
                   sleeptimet = sleeptimem = float(Mighty[0])
                   counter = int(Mighty[1])
                   for _ in range(counter):
                        reply = random.choice(RAID)
                        caption = f"{username} {reply}"
                        async with event.client.action(event.chat_id, "typing"):
                             await event.client.send_message(event.chat_id, caption)
                             await asyncio.sleep(sleeptimem)
         else:
            await event.reply(usage)
