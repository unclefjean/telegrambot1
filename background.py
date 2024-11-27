from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
from threading import Thread
import os

# Инициализация Flask
app = Flask(__name__)

# Токен вашего бота
bot_token = "7814014008:AAHXEAuNW5RP7AUbS2CUdgdNglXJKE82aCw"
bot = Bot(token=bot_token)

# Создаем экземпляр Application, который будет использоваться для бота
application = ApplicationBuilder().token(bot_token).build()

# Простая команда, которая будет отправляться при вызове /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Привет! Я твой бот для обработки файлов.")

# Добавляем обработчик для команды /start
application.add_handler(CommandHandler("start", start))

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        update = request.get_json()
        print(update)  # Добавьте это для дебага
        update_obj = Update.de_json(update, bot)
        application.process_update(update_obj)
        return 'OK', 200

# Функция для запуска Flask сервера
def run():
    app.run(host='0.0.0.0', port=80)

# Функция для запуска сервера в отдельном потоке
def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    keep_alive()