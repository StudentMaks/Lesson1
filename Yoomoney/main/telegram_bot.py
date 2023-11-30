from aiogram import Bot, Dispatcher, executor, types
from .config import token

API_TOKEN = token

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def send_notification(user_id, message):
    await bot.send_message(user_id, message)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    await send_notification(user_id, "Бот работает!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

