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
import config

router = Router()
db = Database('database/database.db')


@router.message(Command("a"))
@router.message(Command("adm"))
@router.message(Command("admin"))
async def admin_handler(msg: Message, state: FSMContext):
    if msg.from_user.id in config.ADMINS:
        await msg.answer(text.admin_panel, reply_markup=keyboards.admin_menu)


@router.callback_query(F.data == "admin")
async def admin_back_handler(cq: CallbackQuery, state: FSMContext):
    await cq.message.edit_text(text.admin_panel, reply_markup=keyboards.admin_menu)
    await state.clear()


@router.callback_query(F.data == "add_category")
async def add_category_handler(cq: CallbackQuery, state: FSMContext):
    if cq.from_user.id in config.ADMINS:
        await state.set_state(Form.add_new_category)
        await cq.message.edit_text(text.admin_add_category, reply_markup=keyboards.cancel_admin)


@router.message(Form.add_new_category)
async def add_category_after_handler(msg: Message, state: FSMContext):
    if msg.from_user.id in config.ADMINS:
        db.category_create(msg.text)
        await msg.answer(text.admin_add_category_after, reply_markup=keyboards.back_admin)
        await state.clear()


@router.callback_query(F.data == "add_item")
async def add_category_handler(cq: CallbackQuery, state: FSMContext):
    if cq.from_user.id in config.ADMINS:

        builder = InlineKeyboardBuilder()
        for category in db.get_categories():
            builder.button(text=category, callback_data=f"A-cg-{category}")
        builder.button(text=text.go_back, callback_data="admin")
        builder.adjust(1)

        await cq.message.edit_text(text.admin_add_item, reply_markup=builder.as_markup())


@router.callback_query(F.data.startswith("A-cg-"))
async def category_handler(cq: CallbackQuery, state: FSMContext):
    category = cq.data.split("-")[2]

    await state.set_state(Form.add_new_item)
    await state.update_data(add_new_item=category)
    await cq.message.edit_text(text.admin_add_item_after, reply_markup=keyboards.cancel_admin)


@router.message(Form.add_new_item)
async def contact_us_after_handler(msg: Message, state: FSMContext):
    if msg.from_user.id in config.ADMINS:
        category = await state.get_data()
        category = category["add_new_item"]
        print(category)
        data = msg.text.split("\n")
        print(data)
        db.create_item(category, data[0], data[1], data[2], data[3], data[4], data[5])

        await msg.answer(text.admin_add_new_item_after_two, reply_markup=keyboards.back_admin)
        await state.clear()