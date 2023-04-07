from telethon import functions
from telethon.tl import functions
from telethon.tl.functions.channels import InviteToChannelRequest

from WWWL5 import WWWL5

from ..core.managers import edit_delete, edit_or_reply

@WWWL5.on(admin_cmd(pattern="تاك(?: |$)(.*)"))
async def iq(WWWL5):
    mentions = WWWL5.text[8:]
    chat = await WWWL5.get_input_chat()
    async for x in WWWL5.client.iter_participants(chat, 200):
        mentions += f" \n🝳 ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉"
    await WWWL5.client.send_message(WWWL5.chat_id, mentions)
    await WWWL5.delete()
@WWWL5.on(admin_cmd(pattern="تاك 150(?: |$)(.*)"))
async def iq(WWWL5):
    mentions = WWWL5.text[8:]
    chat = await WWWL5.get_input_chat()
    async for x in WWWL5.client.iter_participants(chat, 150):
        mentions += f" \n🝳 ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await WWWL5.client.send_message(WWWL5.chat_id, mentions)
    await WWWL5.delete()
@WWWL5.on(admin_cmd(pattern="تاك 100(?: |$)(.*)"))
async def iq(WWWL5):
    mentions = WWWL5.text[8:]
    chat = await WWWL5.get_input_chat()
    async for x in WWWL5.client.iter_participants(chat, 100):
        mentions += f" \n🝳 ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await WWWL5.client.send_message(WWWL5.chat_id, mentions)
    await WWWL5.delete()
@WWWL5.on(admin_cmd(pattern="تاك 50(?: |$)(.*)"))
async def iq(WWWL5):
    mentions = WWWL5.text[8:]
    chat = await WWWL5.get_input_chat()
    async for x in WWWL5.client.iter_participants(chat, 50):
        mentions += f" \n🝳 ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await WWWL5.client.send_message(WWWL5.chat_id, mentions)
    await WWWL5.delete()
@WWWL5.on(admin_cmd(pattern="تاك 10(?: |$)(.*)"))
async def iq(WWWL5):
    mentions = WWWL5.text[8:]
    chat = await WWWL5.get_input_chat()
    async for x in WWWL5.client.iter_participants(chat, 10):
        mentions += f" \n 🝳 ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await WWWL5.client.send_message(WWWL5.chat_id, mentions)
    await WWWL5.delete()
