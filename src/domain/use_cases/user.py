from dataclasses import dataclass

from src.domain.entities.user import User
from src.domain.services.user import IFriendService
from src.domain.use_cases.base import BaseUseCase


@dataclass
class AddFriendCommand:
    user: User
    friend: User


@dataclass
class AddFriendUseCase(BaseUseCase[AddFriendCommand, None]):
    friend_service: IFriendService

    async def execute(self, command: AddFriendCommand) -> None:
        await self.friend_service.add_friend(user=command.user, friend=command.friend)
