from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


menu = [
    [InlineKeyboardButton(text="🔥 BUNDLE DEALS", callback_data="bundle_deals"),
    InlineKeyboardButton(text="🛒 Cart", callback_data="cart")],
    [InlineKeyboardButton(text="💊 Listings", callback_data="listings"),
    InlineKeyboardButton(text="📦 Orders", callback_data="orders")],
    [InlineKeyboardButton(text="🧾 Export price list", callback_data="export_prices")],
    [InlineKeyboardButton(text="⭐️ Reviews", callback_data="reviews"),
    InlineKeyboardButton(text="ℹ️ About", callback_data="about")],
    [InlineKeyboardButton(text="✉️ Contact us", callback_data="contact_us"),
    InlineKeyboardButton(text="👤 Profile", callback_data="profile")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)

back = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Go back", callback_data="menu")]])
cancel = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="🚫 Cancel", callback_data="menu")]])