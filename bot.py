import telebot

TOKEN = "8391969768:AAHOyiYlPwmHdj9wRio_etVCIv7uE0Y5FI8"

bot = telebot.TeleBot("8391969768:AAHOyiYlPwmHdj9wRio_etVCIv7uE0Y5FI8")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Bot ishlayapti ✅")

bot.polling()
