from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn_main_menu: KeyboardButton = KeyboardButton("↩️ Назад в меню")

# Main Menu
btn_start: KeyboardButton = KeyboardButton("▶️ Начать")
btn_info: KeyboardButton = KeyboardButton("ℹ️ Информация")
main_menu: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_start, btn_info)

# Info Menu
info_menu: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_main_menu)

# Test Menu
test_menu: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_main_menu)
