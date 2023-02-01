import re
import time
import keyboard
from aiogram import Bot, Dispatcher, executor, types

f = open("token.txt", "r")
TOKEN = f.readline()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

mode = 'buttons'
last_msg = 'emp'
b_mode = False
board = None

@dp.message_handler(content_types=['text'])
async def get_text_messages(message: types.Message):
    global mode
    global last_msg
    global b_mode
    global board
    m: str = message.text
    m = m.lower()

    rus = re.search('[а-яА-Я]', m)
    if rus is None:
        if m == 'mode':
            board = types.ReplyKeyboardMarkup(resize_keyboard=True)
            buttons = ["key", "write", "buttons"]
            board.add(*buttons)
            await message.answer(f"Change mode on", reply_markup=board)
        elif last_msg == 'mode':
            mode = m
            await message.reply(f"I changed mode to: {m}", reply_markup=types.ReplyKeyboardRemove())
            print(f"I changed mode to: {m}")
        else:
            if mode == 'key' or b_mode:
                blocks = m.split(' ')
                if len(blocks) > 1:
                    times = int(blocks[1])
                    while times > 0:
                        times -= 1
                        keyboard.send(blocks[0])
                        time.sleep(0.5)
                    await message.reply(f"I pressed: {m} times")
                    print(f"I pressed: {m} times")
                else:
                    keyboard.send(m, do_release=False)
                    time.sleep(0.5)
                    keyboard.send(m, do_press=False)
                    await message.reply(f"I pressed: {m}")
                    print(f"I pressed: {m}")
                b_mode = False
            elif mode == 'write':
                keyboard.write(m, 0.5)
                await message.reply(f"I wrote: {m}")
                print(f"I wrote: {m}")
            if mode == 'buttons':
                board = types.ReplyKeyboardMarkup(resize_keyboard=True)
                buttons = ["esc", "space", "backspace"]
                board.row(*buttons)
                buttons = ["left", "right", "up", "down"]
                board.row(*buttons)
                buttons = ["f", "m"]
                board.row(*buttons)
                buttons = ["mode", "delete"]
                board.row(*buttons)
                await message.answer("Press button", reply_markup=board)
                b_mode = True
    last_msg = m

print('Bot started')
executor.start_polling(dp,skip_updates=True)
