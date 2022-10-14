import config
from loguru import logger
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from database import WordsDB
import markups as nav

logger.add(
    config.settings['LOG_FILE'],
    format="{time} {level} {message}",
    level="DEBUG",
    rotation="1 week",
    compression="zip"
)

bot: Bot = Bot(token=config.settings['API_KEY'])
dp: Dispatcher = Dispatcher(bot)

database: WordsDB = WordsDB()
database.parse()
word: str = database.get_random()

is_playing: bool = False

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message) -> None:
    user_id: str = str(message.from_id)
    try:
        await bot.send_message(user_id, f"Привет, {message.from_user.first_name}!", reply_markup=nav.main_menu)
    except Exception as send_error:
        logger.debug(f"{send_error} | Trouble id: {user_id}")


@dp.message_handler()
async def get_random_word(message: types.Message) -> None:
    user_id: str = str(message.from_id)
    global word
    global is_playing
    if message.text == "▶️ Начать":
        try:
            is_playing = True
            await bot.send_message(user_id, word.lower(), reply_markup=nav.test_menu)
        except Exception as send_error:
            logger.debug(f"{send_error} | Trouble id: {user_id}")
    elif message.text == word.strip():
        word = database.get_random()
        try:
            await bot.send_message(user_id, f"Верно!\nСледующее слово: {word.lower()}", reply_markup=nav.test_menu)
        except Exception as send_error:
            logger.debug(f"{send_error} | Trouble id: {user_id}")
    elif message.text == "↩️ Назад в меню":
        try:
            is_playing = False
            await bot.send_message(user_id, f"Привет, {message.from_user.first_name}!", reply_markup=nav.main_menu)
        except Exception as send_error:
            logger.debug(f"{send_error} | Trouble id: {user_id}")
    elif message.text == "ℹ️ Информация":
        try:
            await bot.send_message(user_id, f"Bot made by github.com/chuvashcode\n\
            Libraries used: aiogram, loguru\n2022", reply_markup=nav.info_menu)
        except Exception as send_error:
            logger.debug(f"{send_error} | Trouble id: {user_id}")
    else:
        if is_playing:
            try:
                await bot.send_message(user_id, f"Неверно!", reply_markup=nav.test_menu)
            except Exception as send_error:
                logger.debug(f"{send_error} | Trouble id: {user_id}")
        else:
            try:
                await bot.send_message(user_id, f"Неизвестная команда", reply_markup=nav.main_menu)
            except Exception as send_error:
                logger.debug(f"{send_error} | Trouble id: {user_id}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
