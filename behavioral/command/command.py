import os
from abc import ABC, abstractmethod
from typing import List

from behavioral.command.carrier import Carrier


class CommandInterface(ABC):
    """
    The interface must be implemented by all commands.
    Defines 2 methods: execute and undo.
    """

    @abstractmethod
    def execute(self):
        """
        Executes the command
        """

    @abstractmethod
    def undo(self):
        """
        Rolls the command result back.
        """


class BaseCarrierCommand(CommandInterface, ABC):
    """
    Base command class that contains the common code behavior all commands.
    """

    def __init__(self, carrier: Carrier):
        self._carrier = carrier


class SaveCarrierCommand(BaseCarrierCommand):
    """
    Calls the carrier model to create a new
    record in the database.
    """

    def execute(self):
        self._carrier.save_to_db()

    def undo(self):
        self._carrier.delete()


class AssignCarrierToZoneCommand(BaseCarrierCommand):
    """
    Calls the microservice that assigns carriers to geographical zones.
    """
    def __init__(self, carrier: Carrier):
        super(AssignCarrierToZoneCommand, self).__init__(carrier)
        self._url: str = os.getenv("GEOGRAPHICAL_API_URL")

    def execute(self):
        request_body: dict = {
            "latitude": self._carrier.latitude,
            "longitude": self._carrier.longitude,
        }
        self._send("PUT", uri=f"zones/{self._carrier.carrier_id}", body=request_body)

    def undo(self):
        self._send("DELETE", uri=f"zones/{self._carrier.carrier_id}")

    def _send(self, method: str, uri: str = None, body: dict = None):
        print(f"Sending {method} request to {self._url}/{uri}. Body={body}")


class Transaction:
    """
    The class is an invoker of registered commands
    which wraps their execution into a transaction:
    if any of the commands fail -> all executed commands are rolled back.
    """

    def __init__(self):
        self._commands_to_execute: List[CommandInterface] = []
        self._executed_commands: List[CommandInterface] = []

    def register_command(self, command: CommandInterface):
        self._commands_to_execute.append(command)

    def execute(self):
        """
        Executes all commands one after another.
        if any of the commands fail -> all executed commands are rolled back.
        """
        for command in self._commands_to_execute:
            try:
                # execute the command
                command.execute()
            except Exception as e:
                # if any exception occurs -> rollback all previously executed commands
                print(f"Error occurred while executing a command: {e}")
                self._rollback()
                break

            self._executed_commands.append(command)

    def _rollback(self):
        """
        Rolls back all previously executed commands.
        """
        for command in self._executed_commands:
            command.undo()


if __name__ == "__main__":
    # create a carrier object
    new_carrier = Carrier("John", "Doe", 12.32, 54.21)

    # create commands
    save_carrier_command = SaveCarrierCommand(new_carrier)
    assign_carrier_to_zone_command = AssignCarrierToZoneCommand(new_carrier)

    # create a transaction
    transaction = Transaction()
    transaction.register_command(save_carrier_command)
    transaction.register_command(assign_carrier_to_zone_command)

    # execute the transaction
    transaction.execute()
