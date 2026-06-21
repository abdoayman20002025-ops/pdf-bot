from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "حط_التوكن_هنا"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلاً بك، البوت شغال بنجاح 🚀"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
