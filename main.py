import os
import telebot
import google.generativeai as genai

# Get tokens from Railway variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Check keys
if not BOT_TOKEN or not GEMINI_API_KEY:
    raise ValueError("BOT_TOKEN or GEMINI_API_KEY missing")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Setup Telegram bot
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(func=lambda message: True)
def reply(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)

    except Exception as e:
        print("Error:", e)
        bot.reply_to(message, "❌ Error. Try again later.")


print("🤖 Bot is running...")
bot.infinity_polling()
