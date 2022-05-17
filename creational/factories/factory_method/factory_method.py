from abc import ABC, abstractmethod

from creational.factories.factory_method.employees import (
    EmployeeInterface,
    Programmer,
    Manager,
)


class BaseDepartament(ABC):
    """
    Base class that represents a departament.
    Provides an abstract factory method.
    """

    @classmethod
    @abstractmethod
    def create_employee(cls, name: str, surname: str, **kwargs) -> EmployeeInterface:
        """
        Creates a new employee. An employee implements EmployeeInterface.
        """

    # some other methods that are common for all factory classes


class SoftwareDepartament(BaseDepartament):
    """
    The class represents the software development departament.
    """

    @classmethod
    def create_employee(cls, name: str, surname: str, **kwargs) -> Programmer:
        return Programmer(name, surname)


class ManagementDepartament(BaseDepartament):
    """
    The class represents the management departament.
    """

    @classmethod
    def create_employee(cls, name: str, surname: str, **kwargs) -> Manager:
        return Manager(name, surname, kwargs["experience"])


class EmployeeFactory:
    """
    The class is for client convenience.
    You just specify the employee type and details to create a new object.
    The factory also supports dynamic extension.
    """

    def __init__(self):
        self._departments = {}

    def register_department(self, name: str, department: BaseDepartament):
        self._departments[name] = department

    def create_employee(
        self, departament_name: str, employee_name: str, employee_surname: str, **kwargs
    ):
        departament: BaseDepartament = self._departments.get(departament_name)
        if not departament:
            raise ValueError(f"Unknown departament: {departament_name}")
        return departament.create_employee(employee_name, employee_surname, **kwargs)


if __name__ == "__main__":
    factory = EmployeeFactory()
    factory.register_department("Software", SoftwareDepartament())
    # adding a new departament and employee types does not require changing the factory code
    factory.register_department("Management", ManagementDepartament())

    programmer = factory.create_employee("Software", "Aleksei", "Furmenkov")
    assert isinstance(programmer, Programmer)

    manager = factory.create_employee("Management", "John", "Doe", experience=10)
    assert isinstance(manager, Manager)
