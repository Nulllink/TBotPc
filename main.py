import re
import time
from pynput.keyboard import Controller
from aiogram import Bot, Dispatcher, executor, types
import KeyboardMarkup
import KeyMap

f = open("token.txt", "r")
TOKEN = f.readline()
f.close()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
controller = Controller()

mode = 'buttons'
last_msg = 'emp'
b_mode = False

def controller_send(command):
    keys = command.split('+')
    if len(keys) > 1:
        for key in keys:
            if len(key) > 1:
                key = KeyMap.keycodes[key]
            controller.press(key)
            print(f"press {key}")
        for key in keys:
            if len(key) > 1:
                key = KeyMap.keycodes[key]
            controller.release(key)
            print(f"release {key}")
    else:
        if len(keys[0]) > 1:
            keys[0] = KeyMap.keycodes[keys[0]]
        controller.press(keys[0])
        print(f"press {keys[0]}")
        controller.release(keys[0])
        print(f"release {keys[0]}")

@dp.message_handler(content_types=['text'])
async def get_text_messages(message: types.Message):
    global mode, last_msg, b_mode
    m: str = message.text
    m = m.lower()

    rus = re.search('[а-яА-Я]', m)
    if rus is None:
        if m == 'mode':
            await message.answer(f"Change mode on", reply_markup=KeyboardMarkup.mode_kb)
        elif m == 'lang':
            controller_send("shift+alt")
            await message.reply(f"I changed language")
        elif last_msg == 'mode':
            mode = m
            await message.reply(f"I changed mode to: {m}", reply_markup=types.ReplyKeyboardRemove())
            if mode == 'buttons':
                await message.answer("Press button", reply_markup=KeyboardMarkup.buttons_kb)
                b_mode = True
        else:
            if mode == 'key' or b_mode:
                blocks = m.split(' ')
                if len(blocks) > 1:
                    times = int(blocks[1])
                    while times > 0:
                        times -= 1
                        controller_send(blocks[0])
                        time.sleep(0.5)
                    await message.reply(f"I pressed: {m} times")
                else:
                    controller_send(blocks[0])
                    await message.reply(f"I pressed: {m}")
                b_mode = False
            elif mode == 'write':
                controller.type(m)
                await message.reply(f"I wrote: {m}")
            if mode == 'buttons':
                await message.answer("Press button", reply_markup=KeyboardMarkup.buttons_kb)
                b_mode = True
    else:
        await message.answer("I don't support russian at all")
    last_msg = m

print('Bot started')
executor.start_polling(dp, skip_updates=True)
