# -*- coding: utf-8 -*-

__author__ = "Emoji"
__version__ = "1.0.0"
__url__ = "https://github.com/Emojigit/join_repeater"
__description__ = "Join repeat"
__dname__ = "join_repeater"

from telethon import events
import config
from time import time
def setup(bot,storage):
    @bot.on(events.NewMessage())
    async def join_repeat(event):
        text = event.message.text or event.message.caption
        chatid = event.chat_id
        if not text or text[0] == "/": return
        last_word = storage.get("repeat_lastword_" + str(chatid))
        now = time()
        last_time = storage.get("repeat_lasttime_" + str(chatid),0)
        storage.set("repeat_lastword_" + str(chatid),text,autosave=False)
        storage.set("repeat_lasttime_" + str(chatid),now,autosave=False)
        if not(not last_word or now - last_time > 86400 or last_word != text):
            await event.message.forward_to(event.chat)
        storage.save()

