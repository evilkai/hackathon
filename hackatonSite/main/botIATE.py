import telebot
from telebot import types

from .models import Telegram

# Создаем экземпляр бота
bot = telebot.TeleBot('6099785434:AAFPF_09I2QSfo-P2y-Y9l8GZ6srOF-pdF8')
chat_ids = []
print(chat_ids)

# Обработчик команды /start 
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, text="Это чат-бот ИАТЭ НИУЯ МИФИ с публикацией новостей")

    # далее нужно прописать функцию добавления chat_id в модель для работы с пользователями из телеграмма
    chat_ids.append(message.from_user.id) # это заглушка чтобы работала для моего бота
    tg = Telegram.objects.create(tgID=message.from_user.id)
    tg.save()
    print(chat_ids)


def send_message(topic: str, text: str , chat_ids:set):
    # chat_ids = [] Здесь нужно получить модель пользователей телеграмма с их chat_id
    markdown = f"""
        *{topic}*\n{text}
        """
    for chat_id in chat_ids:
        bot.send_message(chat_id, text=markdown,parse_mode="Markdown")



# Запускаем бота
bot.polling()
