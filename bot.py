import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GAME_SHORT_NAME = os.getenv("tetris_game")
GAME_URL = os.getenv("https://arsencold.github.io/tetris-telegram/")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Нажми кнопку ниже, чтобы сыграть в Тетрис 🎮")
    await update.message.reply_game(GAME_SHORT_NAME)

async def game_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.callback_query.game_short_name == GAME_SHORT_NAME:
        await update.callback_query.answer()
        await update.callback_query.message.reply_game(GAME_SHORT_NAME)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
