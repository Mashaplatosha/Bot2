from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from config import TELEGRAM_TOKEN
from handlers import register_handlers

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
