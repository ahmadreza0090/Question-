from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler

# توکن ربات رو از BotFather بگیر و اینجا قرار بده
TOKEN = "YOUR_BOT_TOKEN"

# سوالات و گزینه‌ها
QUESTIONS = [
    {
        "question": "کدام سیاره نزدیک‌ترین به خورشید است؟",
        "options": ["زهره", "زمین", "
