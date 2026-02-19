import telebot

BOT_TOKEN = "BU YERGA TOKEN"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Bot ishlayapti ✅")

bot.polling()
