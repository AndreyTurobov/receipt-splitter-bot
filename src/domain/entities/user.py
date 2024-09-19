from dataclasses import (
    dataclass,
    field,
)
from uuid import UUID

from src.domain.entities.base import NotLoaded


@dataclass
class User:
    username: str
    telegram_id: str | None = None
    oid: UUID | None = None
    first_name: str | None = None
    last_name: str | None = None
    language_code: str | None = None
    friends: list["User"] | NotLoaded = field(default_factory=NotLoaded)
