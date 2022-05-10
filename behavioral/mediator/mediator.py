import random
from abc import ABC, abstractmethod
from typing import List


class ParkingMediatorInterface(ABC):
    """
    An interface that must be implemented
    by a parking mediator.
    """

    @abstractmethod
    def get_parking_position(self) -> int:
        """
        Returns a parking position.
        """


class ParkingAssistant(ParkingMediatorInterface):
    """
    A concrete parking assistant that
    manages the parking slots.
    """

    def __init__(self):
        # Simulates a parking. In reality, a parking can be a separate class.
        self._free_parking_positions: List[int] = list(range(9))

    def get_parking_position(self) -> int:
        # ensure that free positions are left
        if not self._free_parking_positions:
            raise Exception("The parking is full")

        # get random parking position and remove it from the list of free positions
        parking_position: int = random.choice(self._free_parking_positions)
        self._free_parking_positions.remove(parking_position)

        return parking_position


class Car:
    """
    This class represents a car that is willing to park
    at a certain slot. Encapsulates a mediator object
    and calls it during parking.
    """

    def __init__(self, brand: str, mediator: ParkingMediatorInterface):
        self.brand = brand
        self._mediator = mediator

    def park(self):
        position: int = self._mediator.get_parking_position()
        print(f"{self.brand} parking at position {position}")


if __name__ == "__main__":
    # client code

    parking_assistant = ParkingAssistant()
    jeep = Car("Jeep", parking_assistant)
    audi = Car("Audi", parking_assistant)

    jeep.park()
    audi.park()
