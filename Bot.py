from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler

# توکن ربات رو از BotFather بگیر و اینجا قرار بده
TOKEN = "7192616766:AAF89lcUump9ds2nntjJezsZwYd4tiCL8-w"

# سوالات و گزینه‌ها
QUESTIONS = [
    {
        "question": "کدام سیاره نزدیک‌ترین به خورشید است؟",
        "options": ["زهره", "زمین", "
