#الملف بحقوق سورس سبايدر @EE_20 بواسطة @WWWL5
import asyncio
import os
from secrets import choice
import random
from urllib.parse import quote_plus
from collections import deque
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import InputMessagesFilterVideo

from WWWL5 import WWWL5

from WWWL5.core.logger import logging
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from . import ALIVE_NAME, mention
from ..helpers import get_user_from_event
from ..helpers.utils import _format

from . import reply_id


@WWWL5.on(admin_cmd(outgoing=True, pattern="هارلي$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/3"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ فيلم هارلي 2023 بجودة 360p \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="تحت تهديد السلاح$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/4"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙فيلم تحت تهديد السلاح 2023_ #360p \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="ولا غلطة$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/5"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙فيلم ولا غلطة 2023- #360p \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="خطة مازنجر$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/6"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ فيلم خطة مازنجر hd ️: #360p 2023  \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="هاشتاج جوزني$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/7"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙فيلم #هاشتاج جوزني 2023- #360p \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="بعد الشر$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/8"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙فيلم بعد الشر 2023 | #360p \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="أبن الحج احمد$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/9"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙فيلم أبن الحج احمد نسخه اوضح 2023 \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="رمسيس باريس$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/10"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙فيلم رمسيس باريس 2023 جودة عالية \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="جروب الماميز$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/11"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ 📽| جروب الماميز (2023)  360p \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="العنكبوت$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/12"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙العنكبوت 2022 بجودة # #FHD \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="اشباح اوروبا$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/13"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙فيلم اشباح اوروبا 2022 (360p) \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="كيرة و الجن$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/14"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙فلم كيرة و الجن 2022 جوده #360p \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="بحبك$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/15"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙فيلم : بحبك 2022  بجودة : #360p  \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="موسى$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/16"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ فيلم موسى بجودة #1080HD #شاشةكاملة  \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="عمهم$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/17"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙فيلم #عمهم 2022  #360p  \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="الجريمة$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/18"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙فيلم : الجريمة 2022 بجودة : #360p  \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="العارف$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/19"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙فيلم العارف (2021) #360p بجودة  \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="نبيل الجميل اخصائى تجميل$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/20"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ فيلم نبيل الجميل اخصائى تجميل [2023] \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="الفيل الازرق1$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/21"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙الفيلم الرائع الفيل الازرق 1 كامل الجودة HD \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="اخي فوق الشجرة$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/22"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ فلم أخي فوق الشجرة | 2023 \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="احمد نوتردام$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/23"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ فيلم احمد نوتردام نسخة (FHD) جودة #480p \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="محمد حسين$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/24"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ فيلم محمد حسين - HD \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مسرح مصر1$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/25"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ مسرح مصر - الحلقة الاولي- موسم 3 ( كواليس الكواليس ) \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مسرح مصر2$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/26"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الثانية - موسم 3 ( شوكت وشاطوفني )  \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مسرح مصر3$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/27"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الثالثة - موسم 3 ( فرحة )  \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مسرح مصر4$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/28"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الرابعة - موسم 3 ( عودة ضرغام )  \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مسرح مصر5$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/29"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الخامسة - موسم 3 ( زي كل مرة )  \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مسرح مصر6$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/30"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة السادسة - موسم 3 ( المؤلف )  \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مسرح مصر7$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/31"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة السابعة - موسم 3 ( عملية تجميل )  \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مسرح مصر8$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/32"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الثامنة - موسم 3 ( زي الفل )  \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مسرح مصر9$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/33"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة التاسعة - موسم 3 ( ورينا القوة ) \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مسرح مصر10$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/34"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة العاشرة - موسم 3 ( المتحولون ) \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مسرح مصر11$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/35"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الحادية عشر - موسم 3 ( ال كابوني \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مسرح مصر12$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/36"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الثانية عشر - موسم 3 ( من عشرين سنة ) \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مسرح مصر13$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/37"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الثالثة عشر - موسم 3 ( قرب قرب ) \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مسرح مصر14$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/38"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الرابعة عشر - موسم 3 ( حاجة مهمة جدا ) \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مسرح مصر15$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/39"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الخامسة عشر - موسم 3 ( اوبرا فايزة ) \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مسرح مصر16$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/40"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة السادسة عشر - موسم 3 ( عصابة في المول ) \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مسرح مصر17$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/41"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة السابعة عشر - موسم 3 ( كلام كبار ) \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مسرح مصر18$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/42"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الثامنة عشر - موسم 3 ( ضربة جزاء ) \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مسرح مصر19$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/43"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة التاسعة عشر - موسم 3 ( راس السنة \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مسرح مصر20$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/44"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة العشرون - موسم 3 ( رجالة بلدنا ) \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مسرح مصر21$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/45"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الواحدة والعشرون - موسم 3 ( الخاتم ) \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مسرح مصر22$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/46"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الثانية والعشرون - موسم 3 ( رايح جاي ) \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="الواد سيد الشغال$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/47"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرحية الواد سيد الشغال كاملة اونلاين🎭 \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="اخويا هايص وانا لايص$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/48"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرحية اخويا هايص وانا لايص كاملة \n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سك على بناتك$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/49"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ مسرحيه سك على بناتك كاملة اون لاين 🎭\n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="المتزوجون$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/50"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ مسرحيه المتزوجون كاملة اون لاين 🎭\n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="العيال كبرت$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/51"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ مسرحية العيال كبرت كاملة اون لاين HD\n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مدرسة المشاغبين$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/52"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ مسرحية مدرسة المشاغبين كاملة اون لاين HD\n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="وجهة نظر$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/53"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ مسرحية وجهة نظر كاملة اونلاين HD\n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="حزمنى يا$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/54"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ مسرحية حزمنى يا كاملة اون لاين HD\n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="المرجيحة$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/55"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ مسرح امين وشركاه مسرحيه المرجيحة\n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مدرسة المشاغبين بالالوان$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/57"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ مدرسة المشاغبين بالألوان بجودة #360p\n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="بودي جارد$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/60"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ مسرحية بودي جارد (1999) | بجودة #480p\n⎊︙ BY : @EE_20 🎬",parse_mode="html")
  await Video.delete()
