from aiogram import types

mode_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["key", "write", "os"]
mode_kb.row(*buttons)
buttons = ["movie", "media"]
mode_kb.row(*buttons)

movie_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["esc", "space"]
movie_kb.row(*buttons)
buttons = ["left", "right", "up", "down"]
movie_kb.row(*buttons)
buttons = ["f", "m"]
movie_kb.row(*buttons)
buttons = ["mode", "lang"]
movie_kb.row(*buttons)

media_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["volup", "voldown", "mute"]
media_kb.row(*buttons)
buttons = ["pause", "next", "prev"]
media_kb.row(*buttons)
buttons = ["mode"]
media_kb.row(*buttons)

os_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["alt+f4", "enter", "tab"]
os_kb.row(*buttons)
buttons = ["ctrl+a", "ctrl+c", "ctrl+v"]
os_kb.row(*buttons)
buttons = ["left", "right", "up", "down"]
os_kb.row(*buttons)
buttons = ["mode", "lang"]
os_kb.row(*buttons)