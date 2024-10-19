from django.db import models
import telebot


class Feedback(models.Model):
    name = models.CharField(max_length=144)
    number = models.CharField(max_length=144)
    text = models.TextField()

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        bot_token = '7130510261:AAEWidIK9jjtC70jN1YhGts7Ph57hD0rGBE'
        chat_id = '5556117159'

        bot = telebot.TeleBot(bot_token)
        message_text = (f"ФИО: {self.name}\n"
                        f"Номер: {self.number}\n"
                        f"Текст отзыва: {self.text}")

        bot.send_message(chat_id, message_text)
