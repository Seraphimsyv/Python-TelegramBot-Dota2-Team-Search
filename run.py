from aiogram import executor
from aiogram import Dispatcher
from bot import dp, register_handlers


async def __startup(dp: Dispatcher) -> None:
    register_handlers(dp)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=__startup)