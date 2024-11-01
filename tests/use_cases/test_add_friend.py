import uuid

import pytest

from src.domain.entities.user import User
from src.domain.services.user import (
    IFriendService,
    IUserService,
)
from src.domain.use_cases.user import (
    AddFriendCommand,
    AddFriendUseCase,
)


@pytest.fixture
async def use_case(container) -> AddFriendUseCase:
    return container.resolve(AddFriendUseCase)


@pytest.fixture
async def user_service(container) -> IUserService:
    return container.resolve(IUserService)


@pytest.fixture
async def friend_service(container) -> IFriendService:
    return container.resolve(IFriendService)


@pytest.fixture
async def one_user(user_service: IUserService) -> User:
    return await user_service.get_or_create(User(oid=uuid.uuid4(), username="SomeName"))


@pytest.fixture
async def duo_users(user_service: IUserService) -> tuple[User, User]:
    first_user = await user_service.get_or_create(
        User(oid=uuid.uuid4(), username="SomeName")
    )
    second_user = await user_service.get_or_create(
        User(oid=uuid.uuid4(), username="SomeName2")
    )
    return first_user, second_user


async def test_add_not_exist_friend(
    use_case: AddFriendUseCase,
    friend_service: IFriendService,
    one_user: User,
):
    user = one_user
    user_friend = User(username="SomeName2")
    command = AddFriendCommand(
        user=user,
        friend=user_friend,
    )
    await use_case.execute(command)

    friends = await friend_service.get_friends(user_oid=user.oid)
    assert any(friend.username == user_friend.username for friend in friends)


async def test_add_not_existed_friend(
    use_case: AddFriendUseCase,
    friend_service: IFriendService,
    duo_users: tuple[User, User],
):
    user, user_friend = duo_users
    command = AddFriendCommand(
        user=user,
        friend=user_friend,
    )
    await use_case.execute(command)

    friends = await friend_service.get_friends(user_oid=user.oid)
    assert any(friend.username == user_friend.username for friend in friends)
