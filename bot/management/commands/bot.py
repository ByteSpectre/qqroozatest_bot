import telebot
import os
from django.core.management.base import BaseCommand
from bot.models import Text, User
import random
from dotenv import load_dotenv


load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я ваш бот. Используйте /help для списка команд.")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Доступные команды:\n/start - приветственное сообщение\n/help - список команд\n/info - случайный текст из базы данных")

@bot.message_handler(commands=['info'])
def send_info(message):
    texts = Text.objects.all()
    if texts:
        random_text = random.choice(texts)
        bot.reply_to(message, random_text.content)
    else:
        bot.reply_to(message, "Нет доступных текстов.")

    user_id = message.from_user.id
    user, created = User.objects.get_or_create(user_id=user_id)
    if created:
        user.save()

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text == '/start':
        send_welcome(message)
    elif message.text == '/help':
        send_help(message)
    elif message.text == '/info':
        send_info(message)
    else:
        bot.reply_to(message, "Я не понимаю эту команду")

class Command(BaseCommand):
    help = 'Запуск Telegram-бота'

    def handle(self, *args, **kwargs):
        bot.polling(none_stop=True)
