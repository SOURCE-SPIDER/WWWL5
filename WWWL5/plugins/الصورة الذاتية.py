from WWWL5 import *
from WWWL5 import WWWL5 
from ..sql_helper.globals import gvarstatus

@WWWL5.on(admin_cmd(pattern="(ذاتية|ذاتيه)"))
async def dato(event):
    if not event.is_reply:
        return await event.edit("..")
    WWWL5 = await event.get_reply_message()
    pic = await WWWL5.download_media()
    await bot.send_file(
        "me",
        pic,
        caption=f"""
- تـم جـلب الصـورة بنجـاح ✓ 
- غير مبري الذمه اذا استخدمت الامر للابتزاز
- CH: @EE_20 
- Dev: @WWWL5 
  """,
    )
    await event.edit(" 🙂❤️ ")
