from handlers import nachalo, start, callback_worker
from start_point import bot

bot.register_message_handler(nachalo, commands=['help'])
bot.register_message_handler(start, commands=['start', 'test'])
bot.register_callback_query_handler(callback_worker, func=lambda call: True)

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
