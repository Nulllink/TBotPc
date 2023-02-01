import re
import time
from pynput.keyboard import Key, Controller
from aiogram import Bot, Dispatcher, executor, types
import keymap

f = open("token.txt", "r")
TOKEN = f.readline()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
keycodes = keymap.keycodes
keyboard = Controller()

mode = 'buttons'
last_msg = 'emp'
b_mode = False

buttons_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["esc", "space", "backspace"]
buttons_kb.row(*buttons)
buttons = ["left", "right", "up", "down"]
buttons_kb.row(*buttons)
buttons = ["f", "m"]
buttons_kb.row(*buttons)
buttons = ["mode", "delete", "lang"]
buttons_kb.row(*buttons)

mode_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["key", "write", "buttons"]
mode_kb.add(*buttons)

@dp.message_handler(content_types=['text'])
async def get_text_messages(message: types.Message):
    global mode, last_msg, b_mode, buttons_kb, mode_kb, keycodes
    m: str = message.text
    m = m.lower()

    rus = re.search('[а-яА-Я]', m)
    if rus is None:
        if m == 'mode':
            await message.answer(f"Change mode on", reply_markup=mode_kb)
        elif m == 'lang':
            keyboard.send("shift+alt")
            await message.reply(f"I changed language")
            print(f"I changed language")
        elif last_msg == 'mode':
            mode = m
            await message.reply(f"I changed mode to: {m}", reply_markup=types.ReplyKeyboardRemove())
            print(f"I changed mode to: {m}")
            if mode == 'buttons':
                await message.answer("Press button", reply_markup=buttons_kb)
                b_mode = True
        else:
            if mode == 'key' or b_mode:
                blocks = m.split(' ')
                key = keycodes[blocks[0]]
                if len(blocks) > 1:
                    times = int(blocks[1])
                    while times > 0:
                        times -= 1
                        keyboard.send(blocks[0])
                        time.sleep(0.5)
                    await message.reply(f"I pressed: {m} times")
                    print(f"I pressed: {m} times")
                else:
                    keyboard.press('m')
                    keyboard.release('m')
                    await message.reply(f"I pressed: {m}")
                    print(f"I pressed: {m}")
                b_mode = False
            elif mode == 'write':
                keyboard.write(m, 0.5)
                await message.reply(f"I wrote: {m}")
                print(f"I wrote: {m}")
            if mode == 'buttons':
                await message.answer("Press button", reply_markup=buttons_kb)
                b_mode = True
    last_msg = m

print('Bot started')
executor.start_polling(dp, skip_updates=True)
