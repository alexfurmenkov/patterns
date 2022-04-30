# Singleton

### When to use the pattern?
Singleton is used when you need to be sure that only one instance of the class will be created. It can be handy when 
initialization of an object is very expensive. On the other hand, the pattern has several serious drawbacks:

* Mixes 2 responsibilities. Singleton class is responsible for 2 things: ensuring that only one instance is created and providing the functionality of a class.
* Introduces a global state to the application. The main problem with the global state is that it can be changed in any place in the program. This might also affect your tests. **A singleton must be immutable**.

You also need to consider that if your application is using multithreading, your singleton must be synchronized so that the same instance was reused in different threads. 

### Example
In the example, class `DBClient` acts like a Singleton that communicates with the DB server.
