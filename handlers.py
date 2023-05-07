from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command('start'))
async def start_handker(msg: Message):
    await msg.answer('Привет! Я первый бот Ивана, пока могу немного, но он меня учит)))'
                     '\n Если хочешь, я помогу тебе узнать твой ID, просто нажми: /ID'
                     '\n Или можешь со мной попрощаться /bye')

@router.message(Command('ID'))
async def all_messege_holder(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")

@router.message(Command('bye'))
async def bye_massage(msg: Message):
    await msg.answer('И тебе не хворать!')

@router.message(Command('chamomile'))
async def daisy(msg: Message):
    data = msg.text
    _, num = data.split()
    for i in range(int(num)):
        if i%2:
            await msg.answer('Не любит')
        else:await msg.answer('Любит')

@router.message()
async def all(msg: Message):
    await msg.answer('Сам ты ' + msg.text + ' 😜')