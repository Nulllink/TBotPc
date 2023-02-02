from aiogram import types

movie_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["esc", "space"]
movie_kb.row(*buttons)
buttons = ["left", "right", "up", "down"]
movie_kb.row(*buttons)
buttons = ["f", "m"]
movie_kb.row(*buttons)
buttons = ["mode", "lang"]
movie_kb.row(*buttons)

mode_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["key", "write"]
mode_kb.add(*buttons)
buttons = ["movie", "media"]
mode_kb.add(*buttons)

media_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["volup", "voldown", "mute"]
media_kb.add(*buttons)
buttons = ["pause", "next", "prev"]
media_kb.add(*buttons)
buttons = ["mode"]
media_kb.add(*buttons)
