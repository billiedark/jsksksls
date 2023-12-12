from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


menu = [
    [InlineKeyboardButton(text="💊 Listings", callback_data="listings")],
    [InlineKeyboardButton(text="🛒 Cart", callback_data="cart"),
    InlineKeyboardButton(text="📦 Orders", callback_data="orders")],
    [InlineKeyboardButton(text="🧾 Export price list", callback_data="export_prices")],
    [InlineKeyboardButton(text="⭐️ Reviews", callback_data="reviews"),
    InlineKeyboardButton(text="ℹ️ About", callback_data="about")],
    [InlineKeyboardButton(text="✉️ Contact us", callback_data="contact_us"),
    InlineKeyboardButton(text="👤 Profile", callback_data="profile")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)

admin_menu = [
    [InlineKeyboardButton(text="➕ Add a new item", callback_data="add_item"),],
    [InlineKeyboardButton(text="➕ Add a new category", callback_data="add_category"),],
]
admin_menu = InlineKeyboardMarkup(inline_keyboard=admin_menu)

back = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Go back", callback_data="menu")]])
back_admin = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Go back", callback_data="admin")]])

cancel = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="🚫 Cancel", callback_data="menu")]])
cancel_admin = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="🚫 Cancel", callback_data="admin")]])

item_purchase = [
    [InlineKeyboardButton(text="", callback_data="listings")],
    [InlineKeyboardButton(text="🛒 Cart", callback_data="cart"),
    InlineKeyboardButton(text="📦 Orders", callback_data="orders")],
    [InlineKeyboardButton(text="🧾 Export price list", callback_data="export_prices")],
    [InlineKeyboardButton(text="⭐️ Reviews", callback_data="reviews"),
    InlineKeyboardButton(text="ℹ️ About", callback_data="about")],
    [InlineKeyboardButton(text="✉️ Contact us", callback_data="contact_us"),
    InlineKeyboardButton(text="👤 Profile", callback_data="profile")]
]
item_purchase = InlineKeyboardMarkup(inline_keyboard=item_purchase)

done_manually = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Done", callback_data="{data}")]])