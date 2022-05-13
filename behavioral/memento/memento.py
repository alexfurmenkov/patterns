import uuid
from abc import ABC, abstractmethod
from typing import List, Optional

from behavioral.memento.db_models import DBModelInterface, User


class MementoInterface(ABC):
    """
    The interface for all snapshots.
    """

    @property
    @abstractmethod
    def state(self) -> float:
        """
        Returns a snapshot state which is used for restoring.
        """


class ModelBalanceMemento(MementoInterface):
    """
    Creates a snapshot of DB model balance
    """

    def __init__(self, db_model_balance: float):
        self._state = db_model_balance

    @property
    def state(self) -> float:
        return self._state


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


class BaseBalanceCommand(CommandInterface, ABC):
    """
    Base command class that contains the common code behavior all commands.
    """

    def __init__(self, db_model: DBModelInterface, new_balance: float):
        self._db_model = db_model
        self._new_balance = new_balance


class UpdateBalanceCommand(BaseBalanceCommand):
    """
    Updates a balance.
    """
    def __init__(self, db_model: DBModelInterface, new_balance: float):
        super(UpdateBalanceCommand, self).__init__(db_model, new_balance)
        self._balance_before_update: Optional[MementoInterface] = None

    def execute(self):
        """
        Saves the snapshot of user's balance before the update.
        """
        self._balance_before_update = ModelBalanceMemento(self._db_model.balance)
        self._db_model.update(balance=self._new_balance)

    def undo(self):
        """
        Restores the user's balance from the snapshot.
        """
        self._db_model.update(balance=self._balance_before_update.state)


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
    # client code

    # create 2 users
    bob = User(str(uuid.uuid4()), "Bob", "bob_pass", 100)
    alice = User(str(uuid.uuid4()), "Alice", "alice_pass", 50)

    # create 2 commands: one for each user
    update_bob_balance_command = UpdateBalanceCommand(bob, 70)
    update_alice_balance_command = UpdateBalanceCommand(alice, 80)

    # create a transaction and register commands
    transaction = Transaction()
    transaction.register_command(update_bob_balance_command)
    transaction.register_command(update_alice_balance_command)

    # execute the transaction
    transaction.execute()
