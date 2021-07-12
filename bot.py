from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token="#")
dp = Dispatcher(bot)

@dp.message_handler()
async def get_message(message: types.Message):
    messagechat = message.chat.id
    if "фотография" in messagechat:
        text = "Понял"
#    bot_user = await bot.get_me()    
 #   text = "Какой-то текст"
    sent_message = await bot.send_message(chat_id=messagechat, text=text)

    print (bot_user.username)

executor.start_polling(dp)