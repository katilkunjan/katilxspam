from MightyXSpam import Mig, Mig2, Mig3, Mig4, Mig5, Mig6, Mig7, Mig8, Mig9, Mig10, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from MightyXSpam import CMD_HNDLR as hl
    
HELP_PIC = "https://telegra.ph/file/06f28e4288070eb5f26a8.jpg"

Mig_Help = "★𝐊𝐚𝐭𝐢𝐥𝙓𝙎𝙥𝙖𝙢 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪 ★\n𝐂𝐥𝐢𝐜𝐤 𝐎𝐧 𝐁𝐞𝐥𝐨𝐰 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐅𝐨𝐫 𝐇𝐞𝐥𝐩"


@Mig.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mig2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mig3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mig4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mig5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mig6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mig7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mig8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mig9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mig10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Mig_Help,
                                  buttons=[
           [
            Button.inline("🔥 Spam 🔥", data="spam"),
            Button.inline("😈 Raid 😈", data="raid"),
           ],
           [
            Button.inline("⚡ Extra ⚡", data="extra"),
           ],
           [    
            Button.url("✨ ᴄʜᴀɴɴᴇʟ ✨", "https://t.me/heartbrokenperson1")
           ],
           [
           Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/full_masti_clubs")
           ],
           ],
           )              

  
  
extra_msg = f"""
**Help Extra Cmds**

**UserBot :** Userbot Cmds
Command :
1) {hl}ping 
2) {hl}alive
3) {hl}restart
4) {hl}addsudo <reply to user> || Owner Cmd ||

**Echo :** To Active Echo On Any User
Command :
1) {hl}addecho <reply to user>
2) {hl}rmecho <reply to user>

**Leave :** To Leave Group/Channel
Command :
1) {hl}leave <group/chat id>
2) {hl}leave : Type in the Group bot will auto leave that group

**PackSpam :** Sticker Pack Spam
1) {hl}packspam (replying to any sticker)

**© @tera_baap_katil**
"""

                 
raid_msg = f"""
**Help Raid Cmds**


**Raid :** Activates Raid on Any individual User For Given Range.
Command :
1) {hl}raid <count> <username
2) {hl}raid <count> <reply to user>

**DelayRaid :** Activates Raid on Any individual User For Given Range.
Command :
1) {hl}delayraid <delay> <count> <Username of User>
2) {hl}delayraid <delay> <count> <reply to a User>

**ReplyRaid :** Activates Reply Raid on The User!!
Command :
1) {hl}replyraid <replying to user>
2) {hl}dreplyraid <username>

**DReplyRaid :** Deactivates Reply Raid on The User!!
Command :
1) {hl}dreplyraid <replying to user>
2) {hl}dreplyraid <username>


**© @tera_baap_katil**
"""

spam_msg = f"""
**Help Spam Cmds**

**Spam :** Spams a Message For Given Counter(<= 100).
Command :
1) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
2) {hl}spam <count> <replying any message>

**BigSpam :** Spams a Message For Given Counter.
Command :
1) {hl}bigspam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
2) {hl}bigspam <count> <replying any message>

**DelaySpam :** Delay Spam a Text For Given Counter After Given Time.
Command :
1) {hl}delayspam <delay> <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
2) {hl}delayspam <delay> <count> <replying any message>

**PormSpam :** Pormography Spam.
Command :
1) {hl}pornspam <count>

**Hang :** Spams Hanging Message For Given Counter.
Command :
1) {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)

** © @tera_baap_katil**
"""                     
           
           
@Mig.on(events.CallbackQuery(pattern=r"help_back"))
@Mig2.on(events.CallbackQuery(pattern=r"help_back"))
@Mig3.on(events.CallbackQuery(pattern=r"help_back"))
@Mig4.on(events.CallbackQuery(pattern=r"help_back"))
@Mig5.on(events.CallbackQuery(pattern=r"help_back"))
@Mig6.on(events.CallbackQuery(pattern=r"help_back"))
@Mig7.on(events.CallbackQuery(pattern=r"help_back"))
@Mig8.on(events.CallbackQuery(pattern=r"help_back"))
@Mig9.on(events.CallbackQuery(pattern=r"help_back"))
@Mig10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
      await event.edit(
            Mig_Help,
            buttons=[
           [
            Button.inline("🔥 Spam 🔥", data="spam"),
            Button.inline("😈 Raid 😈", data="raid"),
           ],
           [
            Button.inline("⚡ Extra ⚡", data="extra"),
           ],
           [    
            Button.url("✨ ᴄʜᴀɴɴᴇʟ ✨", "https://t.me/heartbrokenperson1")
           ],
           [
           Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/full_masti_clubs")
           ],
           ],
        )           
   else:
        Alert = (
                "Noob !! Make Your Own Katil X Spam Bots !! @full_masti_clubs"
            )
        await event.answer(Alert, cache_time=0, alert=True)
      
           
                      
@Mig.on(events.CallbackQuery(pattern=r"spam"))
@Mig2.on(events.CallbackQuery(pattern=r"spam"))
@Mig3.on(events.CallbackQuery(pattern=r"spam"))
@Mig4.on(events.CallbackQuery(pattern=r"spam"))
@Mig5.on(events.CallbackQuery(pattern=r"spam"))
@Mig6.on(events.CallbackQuery(pattern=r"spam"))
@Mig7.on(events.CallbackQuery(pattern=r"spam"))
@Mig8.on(events.CallbackQuery(pattern=r"spam"))
@Mig9.on(events.CallbackQuery(pattern=r"spam"))
@Mig10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(
            spam_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            ) 
   else:
        Alert = (
                "Noob !! Make Your Own Katil X Spam Bots !! @full_masti_clubs"
            )
        await event.answer(Alert, cache_time=0, alert=True)
                 
                                                       
@Mig.on(events.CallbackQuery(pattern=r"raid"))
@Mig2.on(events.CallbackQuery(pattern=r"raid"))
@Mig3.on(events.CallbackQuery(pattern=r"raid"))
@Mig4.on(events.CallbackQuery(pattern=r"raid"))
@Mig5.on(events.CallbackQuery(pattern=r"raid"))
@Mig6.on(events.CallbackQuery(pattern=r"raid"))
@Mig7.on(events.CallbackQuery(pattern=r"raid"))
@Mig8.on(events.CallbackQuery(pattern=r"raid"))
@Mig9.on(events.CallbackQuery(pattern=r"raid"))
@Mig10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(
            raid_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            )  
     else:
        Alert = (
                "Noob !! Make Your Own Katil X Spam Bots !! @full_masti_clubs"
            )
        await event.answer(Alert, cache_time=0, alert=True)
       


@Mig.on(events.CallbackQuery(pattern=r"extra"))
@Mig2.on(events.CallbackQuery(pattern=r"extra"))
@Mig3.on(events.CallbackQuery(pattern=r"extra"))
@Mig4.on(events.CallbackQuery(pattern=r"extra"))
@Mig5.on(events.CallbackQuery(pattern=r"extra"))
@Mig6.on(events.CallbackQuery(pattern=r"extra"))
@Mig7.on(events.CallbackQuery(pattern=r"extra"))
@Mig8.on(events.CallbackQuery(pattern=r"extra"))
@Mig9.on(events.CallbackQuery(pattern=r"extra"))
@Mig10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(
            extra_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),                        
            ],
            ],
            )
   else:
        Alert = (
                "Noob !! Make Your Own 𝚔𝙰𝚃𝙸𝙻 X Spam Bots !! @FULL_MASTI_CLUBS"
            )
        await event.answer(Alert, cache_time=0, alert=True)

