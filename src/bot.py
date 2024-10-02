from gptconvert import get_responce
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from cfg import TOKEN, d02f02
from gptconvert import get_responce
from utils import lec_2

#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN)
dp = Dispatcher()

async def cmd_start(message: types.Message):

    #тут должна быть реплай клавиатура с лекциями

    await message.answer('выберите лекцию')

@dp.message(Command('start'))
async def lalala(message: types.Message):
    await cmd_start(message)
    
    
async def main():
        
        await dp.start_polling(bot)
        
if __name__ == '__main__':
    asyncio.run(main())