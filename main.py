import telebot

from config import BOT_TOKEN


bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message,"Hello world!")

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id,"Привет! Я ничего не умею, но обязательно научусь")

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Привет! Пойдем гулять?":
        bot.send_message(message.chat.id, f"Привет! Я не могу, у меня лапки")
    else:
        bot.send_message(message.chat.id, f"Я не знаю, что мне с этим делать(")

bot.infinity_polling()