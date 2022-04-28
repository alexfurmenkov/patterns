from abc import ABC, abstractmethod


class House:
    """
    The actual complex object with lots of parameters in constructor.
    """

    def __init__(
        self,
        walls: int,
        floors: int,
        windows: int,
        has_pool: bool = None,
        has_garage: bool = None,
        has_gates: bool = None,
        roof_type: str = "flat",
    ):
        self.walls = walls
        self.floors = floors
        self.windows = windows
        self.has_pool = has_pool
        self.has_garage = has_garage
        self.has_gates = has_gates
        self.roof_type = roof_type


class HouseBuilderInterface(ABC):
    """
    The interface which has to be implemented by all builders.
    Builders have to implement the same interface to
    be interchangeable in Director class.
    """

    @abstractmethod
    def set_walls(self, walls_number: int):
        pass

    @abstractmethod
    def set_floors(self, floors_number: int):
        pass

    @abstractmethod
    def set_windows(self, windows_number: int):
        pass

    @abstractmethod
    def set_pool(self) -> None:
        pass

    @abstractmethod
    def set_garage(self) -> None:
        pass

    @abstractmethod
    def set_gates(self) -> None:
        pass

    @abstractmethod
    def set_roof_type(self, roof_type: str) -> None:
        pass

    @property
    @abstractmethod
    def house(self) -> House:
        pass


class HouseBuilder(HouseBuilderInterface):
    """
    A concrete builder
    """

    def __init__(self):
        self._walls = None
        self._floors = None
        self._windows = None
        self._has_pool = None
        self._has_garage = None
        self._has_gates = None
        self._roof_type = None

    def set_floors(self, floors_number: int):
        self._floors = floors_number

    def set_walls(self, walls_number: int):
        self._walls = walls_number

    def set_windows(self, windows_number: int):
        self._windows = windows_number

    def set_pool(self) -> None:
        self._has_pool = True

    def set_gates(self) -> None:
        self._has_gates = True

    def set_garage(self) -> None:
        self._has_garage = True

    def set_roof_type(self, roof_type: str) -> None:
        self._roof_type = roof_type

    @property
    def house(self) -> House:
        return House(
            self._walls,
            self._floors,
            self._windows,
            self._has_pool,
            self._has_garage,
            self._has_gates,
            self._roof_type
        )


class Director:
    """
    A director is a wrapper around a builder class
    that has some pre-defined building logic.
    It encapsulates a builder and allows to change it
    and passes the calls to the builder object.
    """

    def __init__(self, builder_obj: HouseBuilderInterface = None):
        self._builder_obj = builder_obj

    @property
    def builder(self) -> HouseBuilderInterface:
        return self._builder_obj

    @builder.setter
    def builder(self, new_builder: HouseBuilderInterface):
        """
        A builder object can be changed any time.
        """
        self._builder_obj = new_builder

    def build_cheap_house(self, walls: int, windows: int, floors: int) -> House:
        """
        Builds a house with minimum set of features: no pool, garage, gates.
        Only the house itself.
        """
        self._builder_obj.set_walls(walls)
        self._builder_obj.set_windows(windows)
        self._builder_obj.set_floors(floors)
        return self._builder_obj.house

    def build_expensive_house(self, walls: int, windows: int, floors: int, roof_type: str = None) -> House:
        """
        Builds a fully featured house: pool, garage, gates.
        """
        self._builder_obj.set_walls(walls)
        self._builder_obj.set_windows(windows)
        self._builder_obj.set_floors(floors)
        self._builder_obj.set_pool()
        self._builder_obj.set_garage()
        self._builder_obj.set_gates()
        self._builder_obj.set_roof_type(roof_type)
        return self._builder_obj.house


if __name__ == "__main__":
    builder = HouseBuilder()
    builder_director = Director(builder)

    house: House = builder_director.build_expensive_house(4, 8, 2, "round")
    assert house.walls == 4
    assert house.floors == 2
    assert house.windows == 8
    assert house.roof_type == "round"
    assert house.has_pool
    assert house.has_gates
    assert house.has_garage
