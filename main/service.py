import os
import django
import telebot
import logging
from django.conf import settings
from .models import Feedback


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm.settings')

django.setup()


# Get the most recently added DateSale instance
instance = Feedback.objects.all()
bot_token = '7130510261:AAEWidIK9jjtC70jN1YhGts7Ph57hD0rGBE'
CHAT_ID = '5249187638'
logging.basicConfig(level=logging.INFO)

bot = telebot.TeleBot(bot_token)

if not bot_token:
    logging.error("TELEGRAM_BOT_TOKEN не установлен!")
else:
    logging.info("Токен бота загружен.")


@bot.message_handler(commands=['start'])
def start_message(message):
    if instance:
        bot.send_message(message.chat.id, f'Дата: {instance.date}'
                                          f'ФИО: {instance.name}\n Почта: {instance.email}\n '
                                          f'Кол-во продаж: {instance.text}')
    else:
        bot.send_message(message.chat.id, "No products found.")


# Uncomment these if you want to use them
# def send_message(instance):
#     try:
#         bot.send_message(CHAT_ID, f'Новый продукт добавлен: {instance.name}\n{instance.model}')
#         logging.info("Сообщение успешно отправлено.")
#     except Exception as e:
#         logging.error(f"Ошибка при отправке сообщения: {e}")
#
#
# def date_sale_send_message(instance): try: bot.send_message(CHAT_ID, f'Ежедневный отчет: \nДата: {
# instance.date}\nОбщее кол-во продано: {instance.model}\nПрибыль: {instance.revenue}\nЧистая прибыль: {
# instance.net_profit}') logging.info("Сообщение успешно отправлено.") except Exception as e: logging.error(f"Ошибка
# при отправке сообщения: {e}")

if __name__ == "__main__":
    logging.info("Бот начинает polling.")
    bot.polling(non_stop=True)
