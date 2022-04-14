from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_webhook
from argparse import ArgumentParser
import asyncio
import settings


bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    """
    Example
    """
    await message.answer("O hi Mark")


async def main():
    argp = ArgumentParser(description="Run {{cookiecutter.project_name}}")
    argp.add_argument("--polling", action="store_true", default=False, help="Run in polling mode (for debug)")

    args = argp.parse_args()
    if args.polling:
        await dp.start_polling()
    else:
        await bot.set_webhook(settings.WEBHOOK_URL)
        start_webhook(dp, settings.WEBHOOK_PATH, skip_updates=True, host="localhost", port=8000)


if __name__ == '__main__':
    asyncio.run(main())
