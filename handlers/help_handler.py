from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.message(Command("help"))
async def help_command(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📉 Compress PDF", callback_data="main_compress")],
            [InlineKeyboardButton(text="📎 Merge PDFs", callback_data="main_merge")],
            [InlineKeyboardButton(text="🔁 Convert Files", callback_data="main_convert")],
            [InlineKeyboardButton(text="❓ FAQ", callback_data="faq")],
            [InlineKeyboardButton(text="📬 Contact Support", callback_data="contact")]
        ]
    )

    help_text = (
        "📘 <b>ClariPDF Bot – Features & Usage</b>\n\n"
        "<b>🔹 How to Use:</b>\n"
        "1️⃣ Tap a feature button (Compress / Merge / Convert).\n"
        "2️⃣ Upload your file(s) when prompted.\n"
        "3️⃣ Follow instructions to receive the output.\n\n"
        "<b>🔹 Supported Formats & Limits:</b>\n"
        "• PDF, DOCX, PPT, Images (PNG, JPG)\n"
        "• Maximum file size: 25MB per file\n\n"
        "<b>🔹 Tips & Examples:</b>\n"
        "• Merge PDFs: Tap 'Merge PDFs', upload files, then press ✅ Done.\n"
        "• Convert Files: Select the conversion type first, then upload the file.\n\n"
        "🔒 <b>Privacy & Security:</b>\n"
        "All files are processed securely and deleted after conversion.\n\n"
        "ℹ️ <b>Current Version:</b> 1.2\n"
        "✨ New: Now supports PDF ↔ DOCX conversion\n\n"
        "Tap any option below to get started ⬇️"
    )

    # Specify parse_mode="HTML" here!
    await message.answer(text=help_text, reply_markup=keyboard, parse_mode="HTML")
