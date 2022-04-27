import copy
from abc import ABC, abstractmethod
from typing import List


class CopyableInterface(ABC):
    """
    The class represents an interface
    that has to be implemented by all copyable objects.
    """

    @abstractmethod
    def __copy__(self):
        """
        The method returns a shallow copy of the object.
        """

    @abstractmethod
    def __deepcopy__(self, memo=None):
        """
        The method returns a deep copy of the object.
        """


class Robot(CopyableInterface):
    """
    An actual robot class produced by a conveyor.
    """

    def __init__(self, height: int, weight: int, known_phrases: List[str]):
        self.height = height
        self.weight = weight
        self.known_phrases = known_phrases

    def __copy__(self):
        known_phrases = self.known_phrases
        new_object = self.__class__(
            self.height, self.weight, known_phrases
        )
        new_object.__dict__.update(self.__dict__)
        return new_object

    def __deepcopy__(self, memo=None):
        if memo is None:
            memo = {}

        known_phrases = copy.deepcopy(self.known_phrases)
        new_object = self.__class__(
            self.height, self.weight, known_phrases
        )
        new_object.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new_object


if __name__ == "__main__":
    robot = Robot(10, 35, ["Hello"])
    shallow_copy_robot = copy.copy(robot)
    deepcopy_robot = copy.deepcopy(robot)

    assert id(robot) != id(shallow_copy_robot), "Copied object must be in another memory location"
    assert id(robot) != id(deepcopy_robot), "Copied object must be in another memory location"

    assert id(robot.known_phrases) == id(shallow_copy_robot.known_phrases), "Shallow copy doesn't copy nested lists"
    assert id(robot.known_phrases) != id(deepcopy_robot.known_phrases), "Deep copy must copy nested lists"

    shallow_copy_robot.height = 20
    deepcopy_robot.height = 35
    assert robot.height == 10
