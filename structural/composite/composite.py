from abc import ABC, abstractmethod
from typing import Set


class EmployeeInterface(ABC):
    """
    The class defines an interface which has to be
    implemented by all employees of a tree.
    """

    @abstractmethod
    def print_details(self):
        """
        Prints the employee details
        """


class Employee(EmployeeInterface):
    def __init__(self, name: str, job: str, salary: int):
        self.name = name
        self.job = job
        self.salary = salary

    def print_details(self):
        print(f"Name: {self.name}, Job: {self.job}, Salary: {self.salary}")


class Manager(EmployeeInterface):
    def __init__(self, name: str, job: str, salary: int):
        self.name = name
        self.job = job
        self.salary = salary
        self._subordinates: Set[EmployeeInterface] = set()

    def print_details(self):
        for subordinate in self._subordinates:
            subordinate.print_details()
        print(f"Name: {self.name}, Job: {self.job}, Salary: {self.salary}")

    def add_subordinate(self, subordinate: EmployeeInterface):
        self._subordinates.add(subordinate)


if __name__ == "__main__":
    java_dev = Employee("Alex", "Java Developer", 50000)
    python_dev = Employee("James", "Python Developer", 75000)

    project_manager = Manager("Tom", "Project Manager", 100000)
    project_manager.add_subordinate(java_dev)
    project_manager.add_subordinate(python_dev)

    unit_manager = Manager("Ann", "Unit Manager", 150000)
    unit_manager.add_subordinate(project_manager)

    ceo = Manager("Jeff", "CEO", 500000)
    ceo.add_subordinate(unit_manager)

    ceo.print_details()
