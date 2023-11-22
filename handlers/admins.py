from aiogram import types, F, Router
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters import Command
from aiogram import flags
from aiogram.fsm.context import FSMContext

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
        await state.set_state(Form.add_new_item)
        await cq.message.edit_text(text.admin_add_category, reply_markup=keyboards.cancel_admin)