from gptconvert import get_responce
import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
from cfg import TOKEN, d02f02
from gptconvert import get_responce
from utils import lec_2


#logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher(storage=MemoryStorage())
start_router = Router()


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'), logger == logging.getLogger(__name__)

@start_router.message(Command('start_2'))
async def cmd_start_2(message: Message):
    await message.answer('Запуск сообщения по команде /start_2 используя фильтр Command()')
    
""" 
@dp.message_handler(text=['02'])
async def echo(message: types.Message):

    # old style:

    # await bot.send_message(message.chat.id, message.text)
    await message.answer(get_responce(lec_2[d02f02]))
"""

if __name__ == '__main__':
    async def main():
        dp.include_router(start_router)
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    
    asyncio.run(main())