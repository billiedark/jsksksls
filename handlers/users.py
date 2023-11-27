from aiogram import types, F, Router
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters import Command
from aiogram import flags
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder

from states import Form
from database.database import Database
import keyboards
import text

router = Router()
db = Database('database/database.db')


@router.message(Command("start"))
async def start_handler(msg: Message):
    if not db.user_exists(msg.from_user.id):
        db.user_create(msg.from_user.id, msg.from_user.username)

    gif_file = FSInputFile("source/start.gif")
    await msg.answer_animation(animation=gif_file)
    await msg.answer(text.start, reply_markup=keyboards.menu)


@router.callback_query(F.data == "menu")
async def menu_handler(cq: CallbackQuery, state: FSMContext):
    await cq.message.edit_text(text.start, reply_markup=keyboards.menu)
    await state.clear()


@router.callback_query(F.data == "profile")
async def profile_handler(cq: CallbackQuery):
    await cq.message.edit_text(text.profile, reply_markup=keyboards.back)


@router.callback_query(F.data == "about")
async def about_handler(cq: CallbackQuery):
    await cq.message.edit_text(text.about, reply_markup=keyboards.back, disable_web_page_preview=True)


@router.callback_query(F.data == "contact_us")
async def contact_us_before_handler(cq: CallbackQuery, state: FSMContext):
    await state.set_state(Form.message_to_admin)
    await cq.message.edit_text(text.contact_us_before, reply_markup=keyboards.cancel)


@router.message(Form.message_to_admin)
async def contact_us_after_handler(msg: Message, state: FSMContext):
    await msg.answer(text.contact_us_after, reply_markup=keyboards.back)
    await state.clear()


@router.callback_query(F.data == "listings")
async def listings_handler(cq: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    for category in db.get_categories():
        builder.button(text=category, callback_data=f"cg-{category}")
    builder.button(text=text.go_back, callback_data="menu")
    builder.adjust(1)

    await cq.message.edit_text(text.listings_choose_category, reply_markup=builder.as_markup())


@router.callback_query(F.data.startswith("cg-"))
async def category_handler(cq: CallbackQuery, state: FSMContext):
    category = cq.data.split("-")[1]
    builder = InlineKeyboardBuilder()
    for item in db.get_items(category):
        builder.button(text=item[2], callback_data=f"item-{item[0]}")
    builder.button(text=text.go_back, callback_data="menu")
    builder.adjust(1)

    await cq.message.edit_text(text.listings_choose_item, reply_markup=builder.as_markup())


@router.callback_query(F.data.startswith("item-"))
@router.callback_query(F.data.startswith("minus-"))
@router.callback_query(F.data.startswith("plus-"))
async def item_handler(cq: CallbackQuery, state: FSMContext):
    cq_data = cq.data.split("-")
    item_id = cq_data[1]
    item = db.get_item(item_id)
    print(item)

    img = FSInputFile(item[7])

    cart_mode = True if cq_data[0] == "minus" or cq_data[0] == "plus" else False
    cart_count = int(cq_data[2]) if cart_mode else 0
    send_mode = cq.message.edit_caption if cart_mode else cq.message.answer_photo
    print(cart_count)

    builder = InlineKeyboardBuilder()
    builder.button(text="➖", callback_data=f"minus-{item_id}-{cart_count - 1 if cart_count > 0 else cart_count}")
    builder.button(text="➕", callback_data=f"plus-{item_id}-{cart_count + 1}")

    builder.button(text=text.add_to_cart, callback_data=f"atc-{item_id}")
    builder.button(text=text.go_back, callback_data="delete-this")
    builder.adjust(2)

    await send_mode(photo=img, caption=text.item_caption.format(item_name=item[2], item_stock=item[4],
                                                                item_type=item[5], item_rating=5,
                                                                item_description=item[3]), reply_markup=builder.as_markup())
    # await cq.message.delete()


@router.callback_query(F.data.startswith("delete-this"))
async def delete_this_handler(cq: CallbackQuery, state: FSMContext):
    await cq.message.delete()
    await state.clear()