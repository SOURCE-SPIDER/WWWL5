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
            text.replace("ا", "اٰ")
            .replace("ب", "بـٰ‌ـہ")
            .replace("ت", "تـٰ‌ـہ")
            .replace("ث", "ثـٰ‌ـہ")
            .replace("ج", "جـٰ‌ـہ")
            .replace("ح", "حـٰ‌ـہ")
            .replace("خ", "خـٰ‌ـہ")
            .replace("د", "دٰ")
            .replace("ذ", "ذٰ")
            .replace("ر", "رٰ")
            .replace("ز", "زٰ")
            .replace("س", "سـٰ‌ـہ")
            .replace("ش", "شـٰ‌ـہ")
            .replace("ص", "صـٰ‌ـہ")
            .replace("ض", "ضـٰ‌ـہ")
            .replace("ط", "طـٰ‌ـہ")
            .replace("ظ", "ظـٰ‌ـہ")
            .replace("ع", "عـٰ‌ـہ")
            .replace("غ", "غـٰ‌ـہ")
            .replace("ف", "فـٰ‌ـہ")
            .replace("ق", "قـٰ‌ـہ")
            .replace("ك", "كـٰ‌ـہ")
            .replace("ل", "لـٰ̲ـہ")
            .replace("م", "مـٰ̲ـہ")
            .replace("ن", "نـٰ̲ـہ")
            .replace("ه", "هـٰ̲ـہ")
            .replace("و", "وٰ")
            .replace("ي", "يـٰ̲ـہ")
        )
        await event.edit(uppercase_text)
