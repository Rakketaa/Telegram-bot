import telebot
import datetime
from telebot import types

bot = telebot.TeleBot("7011405100:AAGm9bDbPXWa2nmntxi2601A3IpUrJ0Y7cQ")
correct_answers = 0
start_time = 0

@bot.message_handler(commands=['help'])
def Nachalo(message):
    bot.send_message(message.chat.id, '''Привет, вот тебе мои команды:
/help - меню
/start или /test - пройдешь викторину
''')

@bot.message_handler(commands=['start', 'test'])
def start(message):
    global correct_answers
    global start_time
    correct_answers = 0
    start_time = 0
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    key_maybe = types.InlineKeyboardButton(text='Не знаю', callback_data='nothing')
    keyboard.add(key_yes, key_no, key_maybe)
    bot.send_message(message.chat.id, text='Вы хотите пройти тест?', reply_markup=keyboard)
    bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(commands=['top'])
def start(message):
    f = open("result.txt", 'r')
    lst = f.readlines()
    lst.sort()
    f.close()
    bot.send_message(message.chat.id, text=''.join(lst[::-1][:10]))

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global correct_answers
    global start_time

    if call.data == "yes":
        start_time = datetime.datetime.now()
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='5', callback_data='second_question')
        key_2 = types.InlineKeyboardButton(text='6', callback_data='second_question')
        key_3 = types.InlineKeyboardButton(text='3', callback_data='second_question')
        key_4 = types.InlineKeyboardButton(text='4', callback_data='second_question_t')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.send_message(call.message.chat.id, text='Сколько будет 2+2?', reply_markup=keyboard)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Хорошо, нажми /help')

    elif call.data == "nothing":
        bot.send_message(call.message.chat.id, 'Хорошо, нажми /help')

    elif call.data == "second_question":
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='Слон', callback_data='third_question')
        key_2 = types.InlineKeyboardButton(text='Крокодил', callback_data='third_question')
        key_3 = types.InlineKeyboardButton(text='Жираф', callback_data='third_question')
        key_4 = types.InlineKeyboardButton(text='Черепаха', callback_data='third_question_t')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.send_message(call.message.chat.id, text='Как называют животное, которое имеет панцирь?',
                         reply_markup=keyboard)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == "second_question_t":
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='Слон', callback_data='third_question')
        key_2 = types.InlineKeyboardButton(text='Крокодил', callback_data='third_question')
        key_3 = types.InlineKeyboardButton(text='Жираф', callback_data='third_question')
        key_4 = types.InlineKeyboardButton(text='Черепаха', callback_data='third_question_t')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.send_message(call.message.chat.id, text='Как называют животное, которое имеет панцирь?',
                         reply_markup=keyboard)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        correct_answers += 1

    elif call.data == "third_question":
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='1', callback_data='fourth_question')
        key_2 = types.InlineKeyboardButton(text='2', callback_data='fourth_question')
        key_3 = types.InlineKeyboardButton(text='3', callback_data='fourth_question_t')
        key_4 = types.InlineKeyboardButton(text='4', callback_data='fourth_question')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.send_message(call.message.chat.id, text='Сколько углов у треугольника?',
                         reply_markup=keyboard)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == "third_question_t":
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='1', callback_data='fourth_question')
        key_2 = types.InlineKeyboardButton(text='2', callback_data='fourth_question')
        key_3 = types.InlineKeyboardButton(text='3', callback_data='fourth_question_t')
        key_4 = types.InlineKeyboardButton(text='4', callback_data='fourth_question')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.send_message(call.message.chat.id, text='Сколько углов у треугольника?',
                         reply_markup=keyboard)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        correct_answers += 1

    elif call.data == "fourth_question":
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='Проволоку', callback_data='fifth_question_t')
        key_2 = types.InlineKeyboardButton(text='Дома', callback_data='fifth_question')
        key_3 = types.InlineKeyboardButton(text='Ведра', callback_data='fifth_question')
        key_4 = types.InlineKeyboardButton(text='Мебель', callback_data='fifth_question')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.send_message(call.message.chat.id, text='Что делают из меди?',
                         reply_markup=keyboard)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == "fourth_question_t":
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='Проволоку', callback_data='fifth_question_t')
        key_2 = types.InlineKeyboardButton(text='Дома', callback_data='fifth_question')
        key_3 = types.InlineKeyboardButton(text='Ведра', callback_data='fifth_question')
        key_4 = types.InlineKeyboardButton(text='Мебель', callback_data='fifth_question')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.send_message(call.message.chat.id, text='Что делают из меди?',
                         reply_markup=keyboard)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        correct_answers += 1

    elif call.data == "fifth_question":
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='10', callback_data='sixth_question')
        key_2 = types.InlineKeyboardButton(text='12', callback_data='sixth_question_t')
        key_3 = types.InlineKeyboardButton(text='14', callback_data='sixth_question')
        key_4 = types.InlineKeyboardButton(text='18', callback_data='sixth_question')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.send_message(call.message.chat.id, text='Сколько будет 6+6?',
                         reply_markup=keyboard)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == "fifth_question_t":
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='10', callback_data='sixth_question')
        key_2 = types.InlineKeyboardButton(text='12', callback_data='sixth_question_t')
        key_3 = types.InlineKeyboardButton(text='14', callback_data='sixth_question')
        key_4 = types.InlineKeyboardButton(text='18', callback_data='sixth_question')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.send_message(call.message.chat.id, text='Сколько будет 6+6?',
                         reply_markup=keyboard)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        correct_answers += 1

    elif call.data == "sixth_question":
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='Деревья', callback_data='seventh_question')
        key_2 = types.InlineKeyboardButton(text='Сыр', callback_data='seventh_question_t')
        key_3 = types.InlineKeyboardButton(text='Кирпичи', callback_data='seventh_question')
        key_4 = types.InlineKeyboardButton(text='Ведра', callback_data='seventh_question')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.send_message(call.message.chat.id, text='Что делают из молока?',
                         reply_markup=keyboard)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == "sixth_question_t":
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='Деревья', callback_data='seventh_question')
        key_2 = types.InlineKeyboardButton(text='Сыр', callback_data='seventh_question_t')
        key_3 = types.InlineKeyboardButton(text='Кирпичи', callback_data='seventh_question')
        key_4 = types.InlineKeyboardButton(text='Ведра', callback_data='seventh_question')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.send_message(call.message.chat.id, text='Что делают из молока?',
                         reply_markup=keyboard)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        correct_answers += 1

    elif call.data == "seventh_question":
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='Строители', callback_data='eighth_question_t')
        key_2 = types.InlineKeyboardButton(text='Программисты', callback_data='eighth_question')
        key_3 = types.InlineKeyboardButton(text='Стримеры', callback_data='eighth_question')
        key_4 = types.InlineKeyboardButton(text='Полицейские', callback_data='eighth_question')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.send_message(call.message.chat.id, text='Кто строит дома?',
                         reply_markup=keyboard)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == "seventh_question_t":
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='Строители', callback_data='eighth_question_t')
        key_2 = types.InlineKeyboardButton(text='Программисты', callback_data='eighth_question')
        key_3 = types.InlineKeyboardButton(text='Стримеры', callback_data='eighth_question')
        key_4 = types.InlineKeyboardButton(text='Полицейские', callback_data='eighth_question')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.send_message(call.message.chat.id, text='Кто строит дома?',
                         reply_markup=keyboard)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        correct_answers += 1

    elif call.data == "eighth_question":
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='Воды', callback_data='nineth_question_t')
        key_2 = types.InlineKeyboardButton(text='Земли', callback_data='nineth_question')
        key_3 = types.InlineKeyboardButton(text='Пуха', callback_data='nineth_question')
        key_4 = types.InlineKeyboardButton(text='Угля', callback_data='nineth_question')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.send_message(call.message.chat.id, text='Чего больше на нашей планете (в плане массы)?',
                         reply_markup=keyboard)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == "eighth_question_t":
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='Воды', callback_data='nineth_question_t')
        key_2 = types.InlineKeyboardButton(text='Земли', callback_data='nineth_question')
        key_3 = types.InlineKeyboardButton(text='Пуха', callback_data='nineth_question')
        key_4 = types.InlineKeyboardButton(text='Угля', callback_data='nineth_question')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.send_message(call.message.chat.id, text='Чего больше на нашей планете (в плане массы)?',
                         reply_markup=keyboard)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        correct_answers += 1

    elif call.data == "nineth_question":
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='2 человека', callback_data='tenth_question')
        key_2 = types.InlineKeyboardButton(text='5 грамм', callback_data='tenth_question')
        key_3 = types.InlineKeyboardButton(text='Я не знаю', callback_data='tenth_question')
        key_4 = types.InlineKeyboardButton(text='1000 кг/м3', callback_data='tenth_question_t')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.send_message(call.message.chat.id, text='Какова плотность воды?',
                         reply_markup=keyboard)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == "nineth_question_t":
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='2 человека', callback_data='tenth_question')
        key_2 = types.InlineKeyboardButton(text='5 грамм', callback_data='tenth_question')
        key_3 = types.InlineKeyboardButton(text='Я не знаю', callback_data='tenth_question')
        key_4 = types.InlineKeyboardButton(text='1000 кг/м3', callback_data='tenth_question_t')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.send_message(call.message.chat.id, text='Какова плотность воды?',
                         reply_markup=keyboard)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        correct_answers += 1

    elif call.data == "tenth_question":
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='Нет', callback_data='eleventh_question')
        key_2 = types.InlineKeyboardButton(text='Да', callback_data='eleventh_question_t')
        key_3 = types.InlineKeyboardButton(text='Я не знаю', callback_data='eleventh_question')
        key_4 = types.InlineKeyboardButton(text='гыгыгыгыгыгыгы', callback_data='eleventh_question')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.send_message(call.message.chat.id, text='Тебе понравилась эта викторина?',
                         reply_markup=keyboard)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == "tenth_question_t":
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='Нет', callback_data='eleventh_question')
        key_2 = types.InlineKeyboardButton(text='Да', callback_data='eleventh_question_t')
        key_3 = types.InlineKeyboardButton(text='Я не знаю', callback_data='eleventh_question')
        key_4 = types.InlineKeyboardButton(text='гыгыгыгыгыгыгы', callback_data='eleventh_question')
        keyboard.add(key_1, key_2, key_3, key_4)
        bot.send_message(call.message.chat.id, text='Тебе понравилась эта викторина?',
                         reply_markup=keyboard)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        correct_answers += 1

    elif call.data == "eleventh_question":
        bot.send_message(call.message.chat.id, f"Ура! Вы прошли тест! 🎉\n\n➡️ Вот ваш результат: {correct_answers}/10")
        f = open("result.txt", 'a')
        f.write(f"Result: {correct_answers}/10, id: {call.message.chat.id}, date: {datetime.datetime.now() - start_time}\n")
        f.close()
    elif call.data == "eleventh_question_t":
        correct_answers += 1
        bot.send_message(call.message.chat.id, f"Ура! Вы прошли тест! 🎉\n\n➡️ Вот ваш результат: {correct_answers}/10")
        f = open("result.txt", 'a')
        f.write(f"Result: {correct_answers}/10, id: {call.message.chat.id}, date: {datetime.datetime.now() - start_time}\n")
        f.close()

bot.polling(none_stop=True, interval=0)
