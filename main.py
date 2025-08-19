import telebot
from config import TOKEN, CHAT_ID

bot = telebot.TeleBot(TOKEN)

# Коли запустимо цей файл, він одразу відправить повідомлення
bot.send_message(CHAT_ID, "Привіт 👋! Бот працює!")

print("Повідомлення надіслано!")
