from aiogram import types

mode_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["key", "write"]
mode_kb.row(*buttons)
buttons = ["movie", "media"]
mode_kb.row(*buttons)
buttons = ["os", "long"]
mode_kb.row(*buttons)

movie_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["esc", "space"]
movie_kb.row(*buttons)
buttons = ["left", "right", "up", "down"]
movie_kb.row(*buttons)
buttons = ["f", "m"]
movie_kb.row(*buttons)
buttons = ["mode", "lang", "screen"]
movie_kb.row(*buttons)

media_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["volup", "voldown", "mute"]
media_kb.row(*buttons)
buttons = ["pause", "next", "prev"]
media_kb.row(*buttons)
buttons = ["mode", "lang", "screen"]
media_kb.row(*buttons)

os_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["win", "enter", "tab", "win+r"]
os_kb.row(*buttons)
buttons = ["ctrl+a", "ctrl+c", "ctrl+v"]
os_kb.row(*buttons)
buttons = ["left", "right", "up", "down"]
os_kb.row(*buttons)
buttons = ["backspace", "delete", "esc"]
os_kb.row(*buttons)
buttons = ["ctrl+shift+esc", "alt+f4", "win+d"]
os_kb.row(*buttons)
buttons = ["mode", "lang", "screen"]
os_kb.row(*buttons)

long_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
lng = ["shift", "ctrl", "win", "alt"]
long_kb.row(*lng)
buttons = ["tab", "delete"]
long_kb.row(*buttons)
buttons = ["mode", "lang", "screen"]
long_kb.row(*buttons)
