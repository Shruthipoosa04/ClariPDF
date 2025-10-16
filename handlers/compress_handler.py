# compress_handler.py
import os
from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot

router = Router()

# =========================
# 🔹 FSM States
# =========================
class CompressStates(StatesGroup):
    waiting_for_file = State()
    choosing_size = State()
    choosing_custom_size = State()

# =========================
# 🔹 Constants
# =========================
MAX_PRESET_SIZE = [1, 2, 3, 4, 5]
CUSTOM_MIN = 5
CUSTOM_MAX = 35

# Ensure download folder exists
os.makedirs("downloads", exist_ok=True)

# =========================
# 🔹 Step 1: /compress command
# =========================
@router.message(Command("compress"))
async def compress_command(message: types.Message, state: FSMContext):
    await message.answer("📤 Please upload a PDF to compress (max 25 MB).")
    await state.set_state(CompressStates.waiting_for_file)
    print("✅ FSM set to waiting_for_file")

# =========================
# 🔹 Step 2: Handle uploaded PDF
# =========================
@router.message(CompressStates.waiting_for_file, F.document)
async def handle_pdf_upload(message: types.Message, state: FSMContext, bot: Bot):
    file = message.document
    if file.mime_type != "application/pdf":
        await message.answer("⚠️ Please upload a valid PDF file.")
        return

    # Download the file locally
    file_info = await bot.get_file(file.file_id)
    file_path = f"downloads/{file.file_name}"
    await bot.download_file(file_info.file_path, file_path)

    # Store the file path in FSM
    await state.update_data(file_path=file_path)

    print(f"📄 File saved: {file_path}")

    # Inline keyboard for compression size
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"{size}️⃣ {size} MB", callback_data=f"compress_size_{size}")
                for size in MAX_PRESET_SIZE
            ],
            [InlineKeyboardButton("✏️ Custom", callback_data="compress_custom")]
        ]
    )

    await message.answer(
        f"✅ Got your file **{file.file_name}**!\nChoose a target compression size:",
        reply_markup=keyboard
    )
    await state.set_state(CompressStates.choosing_size)

# =========================
# 🔹 Step 3: Handle size selection
# =========================
@router.callback_query(CompressStates.choosing_size, F.data.startswith("compress_size_") | (F.data == "compress_custom"))
async def handle_size_selection(query: types.CallbackQuery, state: FSMContext):
    await query.answer()
    data = await state.get_data()
    file_path = data.get("file_path")

    if not file_path:
        await query.message.answer("⚠️ No file found. Please start again with /compress.")
        await state.clear()
        return

    if query.data.startswith("compress_size_"):
        size = int(query.data.split("_")[-1])
        await query.message.answer(f"⏳ Compressing {os.path.basename(file_path)} to {size} MB… (simulated)")
        await query.message.answer(f"✅ Compression complete! (simulated)\n📎 File: `{os.path.basename(file_path)}`")
        await state.clear()

    elif query.data == "compress_custom":
        await query.message.answer(f"📏 Enter a custom size in MB ({CUSTOM_MIN}–{CUSTOM_MAX}):")
        await state.set_state(CompressStates.choosing_custom_size)

# =========================
# 🔹 Step 4: Handle custom size input
# =========================
@router.message(CompressStates.choosing_custom_size, F.text)
async def handle_custom_size_input(message: types.Message, state: FSMContext):
    try:
        size = int(message.text)
        if not (CUSTOM_MIN <= size <= CUSTOM_MAX):
            raise ValueError
    except ValueError:
        await message.answer(f"⚠️ Please enter a number between {CUSTOM_MIN} and {CUSTOM_MAX}.")
        return

    data = await state.get_data()
    file_path = data.get("file_path")

    await message.answer(f"⏳ Compressing {os.path.basename(file_path)} to {size} MB… (simulated)")
    await message.answer(f"✅ Compression complete! (simulated)\n📎 File: `{os.path.basename(file_path)}`")
    await state.clear()
