# State

### When to use the pattern?
When the behavior of the object should change depending on its internal "state". By internal state I mean the values of the object's attributes.
Also, when you need to avoid a large if/else block which defines the behavior based on the object's attribute values. The pattern also allows
removing duplication of some common code by implementing it in a base state class.


### Example
You are an application admin and want to block a user. A blocked user can't display his friends and posts - only username. At the same time,
friends and posts of a normal user can be seen. So, we will have 2 states: `NormalUserState` and `BlockedUserState` which implement the
same interface but behave differently. We also have a `UserController` class which holds a reference to the state and delegates to it some of its work.
`UserController` does not depend on the concrete state, it only depends on the state's interface and has a public state setter.
