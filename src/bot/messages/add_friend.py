from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.bot.messages.base import BaseMessageBuilder


class AddFriendMessageBuilder(BaseMessageBuilder):
    text = "Хорошо, давайте добавим нового друга. \n" "Выберите способ добавления:"
    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Добавить вручную",
                    url="https://ya.ru",
                ),
                InlineKeyboardButton(
                    text="Отправить приглашение",
                    url="https://ya.ru",
                ),
                InlineKeyboardButton(
                    text="Отмена",
                    callback_data="start",
                ),
            ]
        ],
        resize_keyboard=True,
    )


class AddFriendsManuallyMessageBuilder(BaseMessageBuilder):
    _text = (
        "Ты выбрал добавить друга вручную."
        "Пожалуйста, введи имя друга, которого хочешь добавить:"
    )
    _reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Отмена",
                    callback_data="friend",
                ),
            ]
        ],
        resize_keyboard=True,
    )


class GetFriendRequestMessageBuilder(BaseMessageBuilder):
    def __init__(self, user_ref_id: str) -> None:
        self.user_ref_id = user_ref_id

    @property
    def text(self) -> str:
        return ""
