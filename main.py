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

mode = 'movie'
last_msg = 'emp'
b_mode = False
key_on = "none"


def controller_send(command, fi=0):
    global key_on
    if fi == 1:
        key = KeyMap.keycodes[command]
        controller.press(key)
        key_on = command
    elif fi == 2:
        key = KeyMap.keycodes[key_on]
        controller.release(key)
        key_on = "none"
    else:
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
        else:
            if len(keys[0]) > 1:
                keys[0] = KeyMap.keycodes[keys[0]]
            controller.press(keys[0])
            controller.release(keys[0])
            print(f"press {keys[0]}")


async def button_control(message: types.Message):
    global b_mode
    if mode == 'movie':
        await message.answer(f"Press {mode} button", reply_markup=KeyboardMarkup.movie_kb)
        b_mode = True
    elif mode == 'media':
        await message.answer(f"Press {mode} button", reply_markup=KeyboardMarkup.media_kb)
        b_mode = True
    elif mode == 'os':
        await message.answer(f"Press {mode} button", reply_markup=KeyboardMarkup.os_kb)
        b_mode = True
    elif mode == 'long':
        await message.answer(f"Press {mode} button", reply_markup=KeyboardMarkup.long_kb)
        b_mode = True


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
            time.sleep(0.3)
            await button_control(message)
        else:
            if mode == 'key' or b_mode:
                blocks = m.split(' ')
                if len(blocks) > 1:
                    times = int(blocks[1])
                    while times > 0:
                        times -= 1
                        controller_send(blocks[0])
                        time.sleep(0.5)
                    #await message.reply(f"I pressed: {m} times")
                else:
                    if mode == "long" and blocks[0] in KeyboardMarkup.lng and key_on == "none":
                        await message.reply(f"I pressed: {blocks[0].upper()}")
                        controller_send(blocks[0], 1)
                    elif blocks[0] in KeyboardMarkup.lng and key_on != "none":
                        await message.reply(f"I released: {key_on.upper()}")
                        controller_send(blocks[0], 2)
                    else:
                        controller_send(blocks[0])
                    #await message.reply(f"I pressed: {m}")
                b_mode = False
            elif mode == 'write':
                controller.type(m)
                #await message.reply(f"I wrote: {m}")
            await button_control(message)
    else:
        await message.answer("I don't support russian at all")
    last_msg = m

print('Bot started')
executor.start_polling(dp, skip_updates=True)
