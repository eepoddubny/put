import telebot
import types

bot = telebot.TeleBot('825691070:AAFP0kLNuIgXbXrRKh8aRhbuXUVe9T0-W40')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Привет', 'Пока')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в Music4All /start', reply_markup=keyboard1)

keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('Да', 'Нет')

keyboard3 = telebot.types.ReplyKeyboardMarkup(True)
keyboard3.row('Рок', 'Поп', 'Рэп', 'Еще')

keyboard4 = telebot.types.ReplyKeyboardMarkup(True)
keyboard4.row('Классика', 'R&B', 'Хип-хоп', 'Далее')

keyboard5 = telebot.types.ReplyKeyboardMarkup(True)
keyboard5.row('Электро', 'Фанк', 'Джаз', 'К началу', 'Пока')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет. Хочешь послушать музыку?', reply_markup=keyboard2)
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай', reply_markup=keyboard1)
    elif message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'Что предпочитаешь?', reply_markup=keyboard3)
    elif message.text.lower() == 'нет':
        bot.send_message(message.chat.id, 'Вам тут делать нечего) Хорошего дня!', reply_markup=keyboard1)
    elif message.text.lower() == 'еще':
        bot.send_message(message.chat.id, 'Что предпочитаешь?', reply_markup=keyboard4)
    elif message.text.lower() == 'далее':
        bot.send_message(message.chat.id, 'Что предпочитаешь?', reply_markup=keyboard5)
    elif message.text.lower() == 'к началу':
        bot.send_message(message.chat.id, 'Что предпочитаешь?', reply_markup=keyboard3)
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling(none_stop=True, timeout=123)