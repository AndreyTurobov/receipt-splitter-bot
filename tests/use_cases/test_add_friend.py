import uuid

import pytest

from src.domain.entities.user import User
from src.domain.services.user import (
    IUserService,
)
from src.domain.use_cases.user import (
    AddFriendCommand,
    AddFriendUseCase,
)


@pytest.fixture
async def first_user(container) -> User:
    user_service: IUserService = container.resolve(IUserService)
    return await user_service.get_or_create(User(oid=uuid.uuid4(), username="SomeName"))


@pytest.fixture
async def use_case(container) -> AddFriendUseCase:
    return container.resolve(AddFriendUseCase)


async def test_base_add_friend(
    use_case,
    first_user,
):
    command = AddFriendCommand(
        user=first_user,
        friend=User(username="SomeName2"),
    )
    await use_case.execute(command)

    assert 1 == 1
