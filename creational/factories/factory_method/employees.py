from abc import ABC, abstractmethod


class EmployeeInterface(ABC):
    """
    Interface that is implemented by all company employees.
    """

    @abstractmethod
    def get_details(self) -> dict:
        """
        Returns employee details as a dictionary.
        """


class Programmer(EmployeeInterface):
    """
    The class represents a software developer entity.
    """

    def __init__(self, name: str, surname: str):
        self._name = name
        self._surname = surname

    def get_details(self) -> dict:
        return {
            "name": self._name,
            "surname": self._surname,
        }


class Manager(EmployeeInterface):
    """
    The class represents a manager entity.
    """

    def __init__(self, name: str, surname: str, experience: int):
        self._name = name
        self._surname = surname
        self._experience = experience

    def get_details(self) -> dict:
        return {
            "name": self._name,
            "surname": self._surname,
            "experience": self._experience,
        }
