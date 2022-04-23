# 11-04-22
# (C) Arunkumar Shibu

# Using aiogram first time
# Test

import os
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import BoundFilter, Command
from gplink import get_link

BOT_TOKEN = os.environ.get("BOT_TOKEN")

K = Bot(token=BOT_TOKEN)
bot = Dispatcher(K)

#https://github.com/BotfatherDev/CommonChatModer/blob/work_in_groups/filters/chat_filters.py#L10
class IsPrivate(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE


@bot.message_handler(IsPrivate(), Command("start", prefixes="/"))
async def start(message):
    await message.answer("Send gplink to get direct link!")


@bot.message_handler(IsPrivate())
async def gp(message):
    if not message.text.startswith("https://gplinks") or message.text.startswith("gplinks"):
       await message.answer("Sorry, all I do is scrape GPLinks URLs :(")
       return
    m = await message.answer("Please wait...")
    link = await get_link(message.text)
    await m.delete()
    if not link:      
       await message.answer("Something went wrong\nTry again later..")
    else:
       await message.answer(f"Here is your direct link:\n\n{link}", disable_web_page_preview=True)
    
executor.start_polling(bot)
