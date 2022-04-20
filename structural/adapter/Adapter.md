# Adapter

### When to use the pattern?
The ideal use case is when you have a client which can use a certain interface, and a service class which has an interface
which is incompatible with the client interface.
In this case, you create a class adapter which implements a client interface and uses a service class under the hood.

### Example
You have a class which is responsible for communicating with a certain file storage FileStorage. 
Besides, there is a certain client interface of this file storage which is different from the interface of FileStorage class.
You cannot change the interface of FileStorage class, so you create a new class - FileStorageAdapter which implements
a client interface and delegates all work to FileStorage class. 

### Difference between Adapter and Facade
Facade creates a completely new interface whereas Adapter reuses the old one.