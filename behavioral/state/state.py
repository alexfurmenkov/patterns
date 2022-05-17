from abc import ABC, abstractmethod
from typing import List

from behavioral.state.user import User


class UserStateInterface(ABC):
    """
    This class defines an interface for communicating
    with the user object.
    """

    @abstractmethod
    def get_username(self) -> str:
        """
        Returns a username.
        """

    @abstractmethod
    def get_posts(self) -> List[str]:
        """
        Returns all posts of a user.
        """

    @abstractmethod
    def get_friends(self) -> List[str]:
        """
        Returns all friends of a user.
        """


class BaseUserState(UserStateInterface, ABC):
    """
    A base class for all states. Implements a common behavior.
    """

    def __init__(self, user: User):
        self._user = user

    def get_username(self) -> str:
        return self._user.username


class NormalUserState(BaseUserState):
    """
    This state represents a normal user.
    """

    def get_posts(self) -> List[str]:
        return self._user.posts

    def get_friends(self) -> List[str]:
        return self._user.friends


class BlockedUserState(BaseUserState):
    """
    This state represents a blocked user.
    When a user is blocked, we can't see his posts and friends.
    """

    def get_posts(self) -> List[str]:
        return []

    def get_friends(self) -> List[str]:
        return []


class UserController:
    """
    A context class that represents a controller through which
    the clients have to communicate with the User object.
    """

    def __init__(self, state: UserStateInterface):
        self._state = state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state: UserStateInterface):
        self._state = new_state

    def get_username(self) -> str:
        return self._state.get_username()

    def get_posts(self) -> List[str]:
        return self._state.get_posts()

    def get_friends(self) -> List[str]:
        return self._state.get_friends()


if __name__ == "__main__":
    # client code

    # create a user
    new_user = User(
        username="Aleksei",
        age=23,
        posts=["post_id_1", "post_id_2", ],
        friends=["friend_id_1", "friend_id_2", ]
    )

    normal_state = NormalUserState(new_user)
    controller = UserController(normal_state)

    assert controller.get_username() == new_user.username
    assert controller.get_posts() == new_user.posts
    assert controller.get_friends() == new_user.friends

    # block a user
    controller.state = BlockedUserState(new_user)
    assert controller.get_username() == new_user.username
    assert controller.get_posts() == []
    assert controller.get_friends() == []
