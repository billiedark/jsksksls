from aiogram import types, F, Router
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters import Command
from aiogram import flags
from aiogram.fsm.context import FSMContext

from states import Form
import keyboards
import text

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    gif_file = FSInputFile("source/start.gif")
    await msg.answer_animation(animation=gif_file)
    await msg.answer(text.start, reply_markup=keyboards.menu)


@router.callback_query(F.data == "menu")
async def menu_handler(cq: CallbackQuery):
    await cq.message.edit_text(text.start, reply_markup=keyboards.menu)


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