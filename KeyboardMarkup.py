from aiogram import types

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
