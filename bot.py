import os
import telebot

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلا بيك! أنا Meta Bot 🔥 خدام 24/24")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"قلت: {message.text}")

print("البوت بدا يخدم...")
bot.infinity_polling()
