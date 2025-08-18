import os
import requests
import telebot
from datetime import datetime

# Токен і chat_id зберігаємо у змінних середовища
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# API для отримання цін (CoinGecko)
API_URL = "https://api.coingecko.com/api/v3/simple/price"

COINS = ["bitcoin", "ethereum", "solana"]

def get_prices():
    response = requests.get(API_URL, params={"ids": ",".join(COINS), "vs_currencies": "usd"})
    return response.json()

def generate_report():
    data = get_prices()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    report = f"📊 Звіт ({now})\n"
    for coin in COINS:
        price = data[coin]["usd"]
        report += f"🔹 {coin.capitalize()}: ${price}\n"
    return report

@bot.message_handler(commands=["report"])
def send_report(message):
    report = generate_report()
    bot.send_message(message.chat.id, report)

if __name__ == "__main__":
    report = generate_report()
    bot.send_message(CHAT_ID, report)
    bot.polling()
