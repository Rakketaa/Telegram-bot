import telebot
import datetime
from telebot import types
import os

bot = telebot.TeleBot(os.environ["API_KEY"])

questions = [
    {"question": "Сколько будет 2+2?", "options": ["5", "6", "3", "4"], "correct_option": 3},
    {"question": "Как называют животное, которое имеет панцирь?", "options": ["Слон", "Крокодил", "Жираф", "Черепаха"], "correct_option": 3},
    {"question": "Сколько углов у треугольника?", "options": ["1", "2", "3", "4"], "correct_option": 2},
    {"question": 'Что делают из меди?', "options": ["Проволоку", "Дома", "Ведра", "Мебель"], "correct_option": 0},
    {"question": 'Сколько будет 6+6?', "options": ["10", "12", "14", "18"], "correct_option": 1},
    {"question": 'Что делают из молока?', "options": ["Деревья", "Сыр", "Кирпичи", "Ведра"], "correct_option": 1},
    {"question": 'Кто строит дома?', "options": ["Строители", "Программисты", "Стримеры", "Полицейские"], "correct_option": 0},
    {"question": 'Чего больше на нашей планете (в плане массы)?', "options": ["Воды", "Земли", "Пуха", "Угля"], "correct_option": 0},
    {"question": 'Какова плотность воды?', "options": ["2 человека", "5 грамм", "Я не знаю", "1000 кг/м3"], "correct_option": 3},
    {"question": 'Тебе понравилась эта викторина?', "options": ["Нет", "Да", "Я не знаю", "гыгыгыгыгыгы"], "correct_option": 1},
]
correct_answers = 0
start_time = 0
current_question_message = None

@bot.message_handler(commands=['help'])
def Nachalo(message):
    bot.send_message(message.chat.id, '''Привет, вот тебе мои команды:
/help - меню
/start - пройдешь викторину
''')
    
@bot.message_handler(commands=['start', 'test'])
def start(message):
    global correct_answers
    global start_time
    global current_question_message
    correct_answers = 0
    start_time = datetime.datetime.now()
    current_question_message = bot.send_message(message.chat.id, text="Тест начат. Ответьте на первый вопрос.")
    send_question(message.chat.id, 0)

def send_question(chat_id, question_index):
    question_data = questions[question_index]
    keyboard = types.InlineKeyboardMarkup()
    for option in question_data["options"]:
        keyboard.add(types.InlineKeyboardButton(text=option, callback_data=f'{question_index}_{question_data["options"].index(option)}'))
    global current_question_message
    bot.edit_message_text(chat_id=chat_id, message_id=current_question_message.message_id,
                          text=question_data["question"], reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global correct_answers
    global current_question_message
    question_index, option_index = call.data.split('_')
    question_index = int(question_index)
    option_index = int(option_index)
    if option_index == questions[question_index]["correct_option"]:
        correct_answers += 1
    if question_index < len(questions) - 1:
        send_question(call.message.chat.id, question_index + 1)
    else:
        final_time = datetime.datetime.now() - start_time
        bot.send_message(call.message.chat.id, f"Ура! Вы прошли тест! 🎉\n\n➡️ Вот ваш результат: {correct_answers}/{len(questions)}")
        with open("score.txt", "a") as file:
            score_list = f"Результат: {correct_answers}/{len(questions)}, id: {call.from_user.id}, Имя: {call.from_user.first_name}, Время: {final_time}\n"
            file.write(score_list)

bot.polling(none_stop=True, interval=0)
