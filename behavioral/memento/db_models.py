from abc import ABC, abstractmethod
from typing import Set

DB = {}


class DBModelInterface(ABC):
    """
    Interface that is implemented by all DB models.
    """

    @abstractmethod
    def save(self):
        """
        Saves the record to the DB.
        """

    @abstractmethod
    def update(self, **kwargs):
        """
        Updates a record in the DB.
        kwargs contain attributes to update like balance=100, username="John"
        """

    @property
    @abstractmethod
    def balance(self) -> float:
        """
        Returns a model balance.
        """

    @classmethod
    @abstractmethod
    def get(cls, user_id: str) -> "DBModelInterface":
        """
        Gets the record from the DB
        """


class User(DBModelInterface):
    """
    The class represents a user record
    """

    def __init__(self, user_id: str, username: str, password: str, balance: float):
        self.user_id = user_id
        self.username = username
        self._balance = balance
        self._password = password
        self._allowed_to_update: Set[str] = {
            "username",
            "balance",
        }

    @property
    def balance(self) -> float:
        return self._balance

    def save(self):
        DB[self.user_id] = self._to_dict()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key in self._allowed_to_update:
                setattr(self, key, value)
        self.save()

    @classmethod
    def get(cls, user_id: str) -> "DBModelInterface":
        return DB.get(user_id)

    def _to_dict(self) -> dict:
        """
        Converts a model into a dict
        """
        return {
            "user_id": self.user_id,
            "username": self.username,
            "balance": self.balance,
            "password": self._password,
        }
