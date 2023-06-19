from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bosh_menu_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ichimliklar", callback_data="1"),
            InlineKeyboardButton(text="Lavashlar", callback_data="2"),
            InlineKeyboardButton(text="Burgerlar", callback_data="3"),
            InlineKeyboardButton(text="Pizzalar", callback_data="4"),
        ]
    ]
)

Ichimliklar_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Coca cola", callback_data="5"),
            InlineKeyboardButton(text="Fanta", callback_data="6"),
            InlineKeyboardButton(text="Pepsi", callback_data="7"),
            InlineKeyboardButton(text="Orqaga", callback_data="8"),
        ]
    ]
)

Lavashlar_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kichkina", callback_data="9"),
            InlineKeyboardButton(text="Standart", callback_data="2"),
            InlineKeyboardButton(text="Katta", callback_data="3"),
            InlineKeyboardButton(text="Orqaga", callback_data="4"),
        ]
    ]
)

Burgerlar_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Burger", callback_data="1"),
            InlineKeyboardButton(text="Bigburger", callback_data="2"),
            InlineKeyboardButton(text="Cheaseburger", callback_data="3"),
            InlineKeyboardButton(text="Orqaga", callback_data="4"),
        ]
    ]
)

Pizzalar_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kichkina", callback_data="1"),
            InlineKeyboardButton(text="Standart", callback_data="2"),
            InlineKeyboardButton(text="Katta", callback_data="3"),
            InlineKeyboardButton(text="Orqaga", callback_data="4"),
        ]
    ]
)