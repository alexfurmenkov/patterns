# Memento

The pattern allows taking snapshots of objects and restoring using these snapshots.

### When to use the pattern?
When you need to be able to restore the object state after a certain event, e.g. when a transaction fails.


### Example
The DB doesn't support transactional mechanism and the developers have to implement it on their own. For example, when sending money
from Bob to Alice, we need to execute two operations in a transactional manner: decrease Bob's account and increase Alice's account, if any operation fails - rollback all changes.

We can wrap this updates into a command (see Command pattern for reference) and keep snapshots of Bob's and Alice's accounts. 
If any of the commands fails -> we are restoring their accounts from the snapshots.

A command class `UpdateBalanceCommand` updates the user's balance in the DB and has an `undo` operation which restores the user's
balance to the state before the update. This state is being stored in a memento object `ModelBalanceMemento`.
