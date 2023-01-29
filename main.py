f = open("token.txt", "r")
TOKEN = f.readline()

import telebot
bot = telebot.TeleBot(TOKEN)
import keyboard

mode = 'key'
last_msg = 'emp'

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global mode
    global last_msg
    m: str = message.text
    m = m.lower()

    if m == 'mode':
        bot.send_message(message.from_user.id, f"Change mode on: key, write")
    elif last_msg == 'mode':
        mode = m
        bot.send_message(message.from_user.id, f"I changed mode to: {m}")
    else:
        if mode == 'key':
            blocks = m.split(' ')
            if len(blocks) > 1:
                times = int(blocks[1])
                while times > 0:
                    times -= 1
                    keyboard.send(blocks[0])
                bot.send_message(message.from_user.id, f"I pressed: {m} times")
            else:
                keyboard.send(m)
                bot.send_message(message.from_user.id, f"I pressed: {m}")
        elif mode == 'write':
            keyboard.write(m, 0.1)
            bot.send_message(message.from_user.id, f"I wrote: {m}")
    last_msg = m

print('Bot started')
bot.polling(none_stop=True, interval=0)
