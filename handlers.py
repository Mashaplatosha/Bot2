from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from buttons import create_start_keyboard, create_alert_keyboard, create_location_keyboard
from database import save_user_alert
from aiogram.utils.exceptions import Throttled

# Start 
async def start_command(message: types.Message):
    await message.reply("Пожалуйста, поделитесь своим контактом, чтобы пользоваться ботом.", reply_markup=create_start_keyboard())

# Getting a phone number
async def contact_handler(message: types.Message):
    user_id = message.from_user.id
    phone_number = message.contact.phone_number
    
    # Saving to the database
    save_user_alert(user_id, phone_number)

    await message.reply("Если вы видите или слышите беспилотник, нажмите кнопку ОПАСНОСТЬ БПЛА, чтобы предупредить других пользователей.", reply_markup=create_alert_keyboard())

# ОПАСНОСТЬ БПЛА
async def alert_handler(message: types.Message):
    user_id = message.from_user.id

    # Limit 10 min
    try:
        await message.bot.throttle('alert', rate=600)  
        await message.reply("Вы уже отправили сообщение об опасности. Подождите 10 минут перед повторной отправкой.")
        return
    except Throttled:
        return

    # Send location
    await message.reply("Пожалуйста, отправьте свое местоположение.", reply_markup=create_location_keyboard())

# Handle location
async def location_handler(message: types.Message):
    user_id = message.from_user.id
    location = f"Широта: {message.location.latitude}, Долгота: {message.location.longitude}"
    alert_time = None  # Здесь можно указать текущее время
    
    # Save in base
    save_user_alert(user_id, phone_number="", alert_time=alert_time, location=location)  

    # Message to all users
    alert_message = f"Обнаружен БПЛА! Местоположение: {location}"
    await message.bot.send_message(chat_id=message.chat.id, text=alert_message)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(contact_handler, content_types=types.ContentType.CONTACT)
    dp.register_message_handler(alert_handler, Text(equals="ОПАСНОСТЬ БПЛА"))
    dp.register_message_handler(location_handler, content_types=types.ContentType.LOCATION)
