# A bot that creates characters for the game "Bunker" (I dropped it because I found the bot @Bunkerz_Bot)(ru)
# Бот, который создает персонажей для игры "Бункер" (Закинул, так как нашёл бота @Bunkerz_Bot)
import telebot
from telebot import types
import random
# для второго способа
import requests


# Способ 1: считывает файл и выбирает рандомно
def update():
    # Переменная, в которой собирается персонаж и которая будет отображена
    person = ''
    # Словарь со всеми вариантами (намного легче все варианты перечислить в файле)
    # Правила написания вариантов в файле:
    # Обобщающее слово, ':', и варианты, перечисленные через запятую
    alls = {}
    # Открываем файл с вариантами и добавляем в словарь alls
    with open('variants.txt') as f1le:
        for line in f1le:
            line = line[:-1]
            # Разделяем в каждой строке обобщающее слово от вариантов (между ними символ ":")
            gen_and_var = line.split(':')
            # Разделяем варианты в список (между ними символ ",")
            alls[gen_and_var[0]] = gen_and_var[1].split(',')
    # Добавляем в переменную person каждый вариант
    for key in alls.keys():
        person += '{}: {}\n'.format(key, random.choice(alls[key]))
    # Если нужно прямое отображение в интерпретаторе
    # print(person)
    return person


# Считывает правила с файла и показывает в боте при необходимости
# Открывает файл, добавляет каждую строку в переменную rules и возвращает её
def rules_from_txt():
    rules = ''
    with open('rules.txt') as text:
        for line in text:
            rules += line
    return rules


# Способ 2: Передает данные с онлайн рандомайзера
'''def update():
    # Делаем запрос
    request = requests.get("https://randomall.ru/api/custom/gen/758/")
    # Превращаем полученное в словарь и возвращаем нужное
    info = request.json()
    return info['text']'''


# Отображение того, что код запустился
print('Бот запущен')
bot = telebot.TeleBot('<token>')


# Создание отклика
@bot.message_handler(content_types=['text'])
def rand(message):
    # Создание и отображение кнопок
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    butt1 = types.KeyboardButton('Рандом')
    butt2 = types.KeyboardButton('Правила')
    markup.add(butt1, butt2)
    # Проверка на входящее сообщение
    if message.text == 'Рандом' or message.text == '/random':
        final = update()
    elif message.text == 'Правила' or message.text == '/rules':
        final = rules_from_txt()
    # Если пришло другое сообщение
    else:
        final = 'Хотите сыграть, {}?'.format(message.from_user.username)
    bot.send_message(message.chat.id, final, parse_mode='html', reply_markup=markup)


# Это нужно, чтобы бот постоянно работал
bot.polling(none_stop=True)
