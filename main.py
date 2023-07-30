# import replicate
# import os

# output = replicate.Client(api_token="r8_4gDeJkCwuDSv7r11PjFoXcX8hBiLITL2807Tm").run(
#     "methexis-inc/img2prompt:50adaf2d3ad20a6f911a8a9e3ccf777b263b8596fbd2c8fc26e8888f8a0edbb5",
#     input={"image": open("meme.png", "rb")}
# )
# print(output)


import os
from dotenv.main import load_dotenv
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import router


async def main():
    bot = Bot(token=os.environ.get("BOT_TOKEN"), parse_mode="HTML")
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())