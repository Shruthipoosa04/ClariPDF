from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    buttons = [
        [KeyboardButton("📤 Upload File"), KeyboardButton("🔽 Compress PDF")],
        [KeyboardButton("🔄 Convert Format"), KeyboardButton("📚 Merge PDFs")],
        [KeyboardButton("❓ Help")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        one_time_keyboard=False
    )

def compression_menu():
    markup = InlineKeyboardMarkup()
    sizes = ["1MB", "2MB", "5MB", "10MB"]
    for s in sizes:
        markup.add(InlineKeyboardButton(f"{s}", callback_data=f"compress_{s}"))
    return markup

def convert_menu():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("PDF ↔ DOCX", callback_data="conv_pdf_docx"),
        InlineKeyboardButton("PDF ↔ Images", callback_data="conv_pdf_img"),
        InlineKeyboardButton("PPT → PDF", callback_data="conv_ppt_pdf"),
        InlineKeyboardButton("Images → PDF", callback_data="conv_img_pdf"),
    )
    return markup
