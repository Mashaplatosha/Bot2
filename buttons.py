from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def create_start_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_contact = KeyboardButton("Поделиться контактом", request_contact=True)
    keyboard.add(button_contact) 
    return keyboard

def create_alert_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_alert = KeyboardButton("ОПАСНОСТЬ БПЛА")
    button_cancel = KeyboardButton("Отмена")  
    keyboard.add(button_alert, button_cancel)
    return keyboard
