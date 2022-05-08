# Command

### When to use the pattern?
The pattern allows you to separate different levels of the program so that they did not depend on each other. Also, when you
need to be able to undo an operation, the pattern is the most used approach. Overall, these are the pattern use cases:
* when you need to reuse the same operation that involves different layers of your application. The pattern suggests wrapping this operation into an object. 
* to make the different program layers less dependent on each other
* when you need to make the operation smarter: be able to undo it or have a queue of operations

Due to the fact that the sender class does not know anything about the receiver, the system becomes less coupled. Of course, we can
wrap an operation into a function and call it in different parts of the program. Advantage of the command pattern is that an object
can be intelligent enough to support undo operations whereas the function can't.

### Example
We are building a food delivery application which is built on microservices. When a new carrier signs up, we need to execute two steps:
1. Save his details to the DB;
2. Call microservice that assigns a geographical zone to a carrier.

You also need to do it in a transactional manner - if step 2 fails, step 1 must be rolled back. Each step should be wrapped into a command
with undo operation. 
