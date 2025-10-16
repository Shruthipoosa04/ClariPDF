from aiogram import F, Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.fsm.context import FSMContext

router = Router()

# --- /start command ---
@router.message(F.text == "/start")
async def start_command(message: Message, state: FSMContext):
    keyboard = InlineKeyboardMarkup(
         inline_keyboard=[
            [InlineKeyboardButton(text="📉 Compress PDF", callback_data="main_compress")],
            [InlineKeyboardButton(text="📎 Merge PDFs", callback_data="main_merge")],
            [InlineKeyboardButton(text="🔁 Convert Files", callback_data="main_convert")]
        ]
    )

    await message.answer(
        "👋 <b>Welcome to ClariPDF Bot</b>\n\n"
        "Your all-in-one academic file assistant. Efficiently compress, merge, and convert PDFs and other documents.\n\n"
        "Select an option below to get started ⬇️",
        reply_markup=keyboard
    )

# --- Callback query handler for main menu ---
@router.callback_query(lambda c: c.data in ["main_compress", "main_merge", "main_convert"])
async def handle_main_menu(query: CallbackQuery, state: FSMContext):
    await query.answer()

    if query.data == "main_compress":
        await query.message.answer("📤 Please upload your PDF file to compress (max 25MB).")
        await state.update_data(mode="compress")

    elif query.data == "main_merge":
        await query.message.answer(
            "📎 Upload all PDFs you want to merge.\n"
            "When finished, tap ✅ Done."
        )
        await state.update_data(mode="merge")

    elif query.data == "main_convert":
        keyboard = InlineKeyboardMarkup(
            [InlineKeyboardButton(text="PDF ↔ DOCX", callback_data="convert_docx")],
[InlineKeyboardButton(text="PDF ↔ Images", callback_data="convert_images")],
[InlineKeyboardButton(text="PPT → PDF", callback_data="convert_ppt")],
[InlineKeyboardButton(text="Images → PDF", callback_data="convert_img2pdf")]

        )
        await query.message.answer(
            "🔁 Choose the type of file conversion:",
            reply_markup=keyboard
        )
