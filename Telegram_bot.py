import telebot
import config
from telebot import types
import random
from datetime import datetime
import requests

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start(message: types.Message):
    mess = f"<b>Привет, {message.from_user.first_name} !</b> ✌"
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить YOTUBE", url="https://www.youtube.com/?hl=RU"))
    markup.add(types.InlineKeyboardButton("Посетить WIKIPEDIA", url="https://ru.wikipedia.org/w/index.php?go="))
    if message.text == 'website':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("YOTUBE", callback_data="url")
        item2 = types.InlineKeyboardButton("WIKIPEDIA", callback_data="url")
        markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Передите на сайт!', reply_markup=markup)


@bot.message_handler(commands=['help'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,  row_width=3)
    item1 = types.KeyboardButton("Функция Монета")
    item2 = types.KeyboardButton("Запрос курса биткоина")
    item3 = types.KeyboardButton("Запрос номера телефона")
    item4 = types.KeyboardButton("Как дела?")
    item5 = types.KeyboardButton("/start")
    item6 = types.KeyboardButton("/website")
    markup.add(item1, item2, item3, item4, item5, item6)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.chat.type == 'private':
        if message.text == 'Функция Монета':
            number = random.randint(0, 2)
            if number == 0:
                bot.send_message(message.chat.id, 'Орел! Сделай это!')
            elif number == 1:
                bot.send_message(message.chat.id, 'Решка! Не делай! 🥲')
        elif message.text == 'Запрос курса биткоина':
            bot.send_message(message.chat.id, get_data())
        elif message.text == 'Запрос номера телефона':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            kn1 = types.KeyboardButton("Предоставить номер телефона", request_contact=True)
            kn2 = types.KeyboardButton("Назад")
            markup.add(kn1, kn2)
            bot.send_message(message.chat.id, 'Нажмите кнопку ниже', reply_markup=markup)
        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Функция Монета")
            item2 = types.KeyboardButton("Запрос курса биткоина")
            item3 = types.KeyboardButton("Запрос номера телефона")
            item4 = types.KeyboardButton("Как дела?")
            item5 = types.KeyboardButton("/start")
            item6 = types.KeyboardButton("/website")
            markup.add(item1, item2, item3, item4, item5, item6)
            bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)
        elif message.text == 'Как дела?':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Плохо", callback_data='bad')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)


def get_data():
    req = requests.get('https://yobit.net/api/3/ticker/btc_usd')
    response = req.json()
    sell_price = response['btc_usd']['sell']
    return f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nСтоимость BTC: {sell_price}$"


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, '✌️')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Сочувствую!')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Как дела?',
                                  reply_markup=None)
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)

# Veil_bot:
#  созданный разработчиком Косяченко Ольгой в качестве домашнего задания семинара по "Знакомству с языком Python" в школе GeekBrains!
# Я умею:
# - Приветствовать собеседника по имени.
# - Спрашивать как дела и отвечать по нажатию кнопки "Как дела?".
# - Запрашивать предоставление номера телефона пользователя по нажатию кнопки "Номер телефона".
# - Выводить рандомный результат по нажатию кнопки "Функция монета".
# - Приглашаю посетить сайты: Yotube и  Wikipedia
# - Выводить стоимость BTC на текущий момент времени по нажатию кнопки "Цена BTC".
# -

