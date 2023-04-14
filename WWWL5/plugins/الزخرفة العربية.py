from telethon import events

from WWWL5 import WWWL5

from ..sql_helper.globals import addgvar, delgvar, gvarstatus


@WWWL5.ar_cmd(pattern="تفعيل الزخرفة العربية")
async def zakrafaon(event):
    if not gvarstatus("enzakrafa"):
        addgvar("enzakrafa", "on")
        await edit_delete(event, "⎊ **تم تفعيل الزخرفة العربية بنجاح ✅**")
        return
    if gvarstatus("enzakrafa"):
        await edit_delete(event, "⎊ **الزخرفة العربية مفعلة بالفعل ✅**")
        return


@WWWL5.ar_cmd(pattern="تعطيل الزخرفة العربية")
async def zakrafaoff(event):
    if not gvarstatus("enzakrafa"):
        await edit_delete(event, "⎊ **الزخرفة العربية غير مفعلة بالفعل ❌**")
        return
    if gvarstatus("enzakrafa"):
        delgvar("enzakrafa")
        await edit_delete(event, "⎊ **تم تعطيل الزخرفة العربية بنجاح ❌**")
        return


@WWWL5.on(events.NewMessage(outgoing=True))
async def zakrafarun(event):
    if gvarstatus("enzakrafa"):
        text = event.message.message
        uppercase_text = (
            text.replace("ا", "ٱ")
            .replace("ب", "ب֠ــ‌ۢـ‌ٰـ")
            .replace("ت", "ت֠ــ‌ۢـ‌ٰـ")
            .replace("ث", "ُث֠ــ‌ۢـ‌ٰـ")
            .replace("ج", "ج֠ــ‌ۢـ‌ٰـ")
            .replace("ح", "ح֠ــ‌ۢـ‌ٰـ")
            .replace("خ", "خــ‌ۢـ‌ٰـ")
            .replace("د", "ډ")
            .replace("ذ", "ڏ")
            .replace("ر", "ر")
            .replace("ز", "زٍ")
            .replace("س", "س֠ــ‌ۢـ‌ٰـ")
            .replace("ش", "ش֠ــ‌ۢـ‌ٰـ")
            .replace("ص", "ص֠ــ‌ۢـ‌ٰـ")
            .replace("ض", "ض֠ــ‌ۢـ‌ٰـ")
            .replace("ط", "ط֠ــ‌ۢـ‌ٰـ")
            .replace("ظ", "ظ֠ــ‌ۢـ‌ٰـ")
            .replace("ع", "ع֠ــ‌ۢـ‌ٰـ")
            .replace("غ", "غ֠ــ‌ۢـ‌ٰـ")
            .replace("ف", "فــ‌ۢـ‌ٰـ")
            .replace("ق", " ق֠ــ‌ۢـ‌ٰـ")
            .replace("ك", "ڪ֠ــ‌ۢـ‌ٰـ")
            .replace("ل", "ل֠ــ‌ۢـ‌ٰـ")
            .replace("م", "م֠ــ‌ۢـ‌ٰـ")
            .replace("ن", "ن֠ــ‌ۢـ‌ٰـ")
            .replace("ن", "هہؚ")
            .replace("و", "ﯛ‌୭")
            .replace("ي", "ي֠ــ‌ۢـ‌ٰـ")
        )
        await event.edit(uppercase_text)
