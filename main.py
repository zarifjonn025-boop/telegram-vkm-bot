import telebot
import requests

BOT_TOKEN = 8391969768:AAHOyiYlPwmHdj9wRio_etVCIv7uE0Y5FI8
ADMIN_ID = FFzarif

bot = telebot.TeleBot(BOT_TOKEN)

# START
@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("📥 Video yuklash")
    btn2 = telebot.types.KeyboardButton("👨‍💻 Admin")
    markup.add(btn1, btn2)

    bot.send_message(message.chat.id, "Salom! Link yubor (Instagram/VK)", reply_markup=markup)

# ADMIN
@bot.message_handler(func=lambda m: m.text == "👨‍💻 Admin")
def admin(message):
    bot.send_message(message.chat.id, "Admin: @username")

# VIDEO DOWNLOAD
@bot.message_handler(func=lambda message: True)
def download(message):
    url = message.text

    if "instagram.com" in url:
        api = f"https://api.vevioz.com/api/button/mp4?url={url}"
        
        bot.send_message(message.chat.id, "⏳ Yuklanmoqda...")
        bot.send_message(message.chat.id, api)

    elif "vk.com" in url:
        api = f"https://api.vevioz.com/api/button/mp4?url={url}"
        
        bot.send_message(message.chat.id, "⏳ Yuklanmoqda...")
        bot.send_message(message.chat.id, api)

    else:
        bot.send_message(message.chat.id, "❌ Noto‘g‘ri link yubording")

bot.polling()
