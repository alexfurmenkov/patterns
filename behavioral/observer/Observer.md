# Observer

The pattern allows to "subscribe" objects to the events that happen in other objects. When a state of one object (Publisher)
changes, it notifies all Subscribers.

### When to use the pattern?
When after changing the state of one object you automatically need to handle this change in other objects. A subscriber can
unsubscribe from the changes if needed.

### Example
A currency exchange allows the users to be notified when a ticker price changes. In this case, `Exchange` class acts as a Publisher
which should notify its users when a ticker price changes. `Exchange` class does not depend on the subscriber's classes, it only knows
about their interface - `SubscriberInterface`.