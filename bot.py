import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from config import BOT_TOKEN

# --- Import all routers ---
from handlers.start_handler import router as start_router
from handlers.help_handler import router as help_router
from handlers.compress_handler import router as compress_router


# ==========================
# 🔹 Setup Logging
# ==========================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)


# ==========================
# 🔹 Initialize Bot & Dispatcher
# ==========================
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode="HTML")
)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


# ==========================
# 🔹 Register Routers
# ==========================
dp.include_router(start_router)
dp.include_router(help_router)
dp.include_router(compress_router)


# ==========================
# 🔹 Main Entry Point
# ==========================
async def main():
    logging.info("🚀 ClariPDF Bot is starting...")
    try:
        # Drop pending updates and start polling
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        logging.exception(f"❌ Bot crashed: {e}")
    finally:
        await bot.session.close()
        logging.info("🛑 Bot session closed.")


# ==========================
# 🔹 Run the Bot
# ==========================
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("🧩 Bot stopped manually.")
