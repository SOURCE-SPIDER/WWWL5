#الملف بحقوق سورس سبايدر @EE_20
import asyncio
import random
from asyncio.exceptions import TimeoutError

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from WWWL5 import WWWL5
from ..helpers.utils import reply_id


@WWWL5.on(admin_cmd(outgoing=True, pattern="آيه قصيره$"))
async def jepvois(vois):
  rl = random.randint(111,210)
  url = f"https://t.me/MEMESv2/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⎊︙ BY : @EE_20 🌺",parse_mode="html")
  await vois.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الفاتحة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/26"
  await Voice.client.send_file(Voice.chat_id,url,caption="⎊︙ سوره الفاتحة\n⎊︙ بصوت القارئ ماهر المعيقلي\n⎊︙ BY : @EE_20 🌺",parse_mode="html")
  await Voice.delete()
