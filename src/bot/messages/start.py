from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.messages.base import BaseMessageBuilder


class StartMessageBuilder(BaseMessageBuilder):
    _text = (
        "Привет! Я бот для разделения чеков."
        "Помогу вам и вашим друзьям без проблем"
        " поделить счета кафе,ресторанов и баров.\n\n"
        "Выберите действие: "
    )
    _reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Добавить друга",
                    callback_data="friend",
                ),
                InlineKeyboardButton(
                    text="Разбить чек",
                    url="https://ya.ru",
                ),
            ]
        ],
        resize_keyboard=True,
    )
