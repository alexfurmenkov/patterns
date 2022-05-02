# Simple Factory, Factory Method and Abstract Factory

There are 3 types of factory-related patterns: Simple Factory, Factory Method and Abstract Factory. All patterns have 
similarities and differences. 

Similarities:
* The purpose is object creation;
* Implements the instantiation logic under the hood, encapsulates it.

## Simple Factory pattern

### When to use the pattern?
When you need to create an object for a certain purpose but don't care about the object type. You just expect an object
with a particular interface to be created. A factory can produce different types of objects. A factory is usually represented 
by one class. You also don't mind changing the factory code when the new type of objects is created.

### Example
You are building an application that supports caching. The application supports 2 types of caching: in-memory or redis. 
Caching type will be defined in the application config. When calling the caching object, the result should be the same - a given data is cached. 
You don't care where it will be cached, you just need to cache the data and be able to pull it from the cache later.

Then, create a caching service interface `CachingServiceInterface` which will be implemented by concrete caching services: 
`InMemoryCachingService` and `RedisCachingService` in the example. Finally, `CachingServiceFactory` will provide a public method
`get_caching_service()` that returns a caching service based on the app configuration.

**The drawback of having only one factory class is that you will have to modify its code as the new type of objects is created.**


## Factory method pattern
In this case, a factory class is responsible for producing object of one type only. 
_One factory is specialized in creating only one kind of object. The pattern separates the classes into products and classes that create these products._
The creator class usually has a public method like `create_product()` that creates an object of a particular type. 
Important to understand - `create_product()` method is located not in the product class but in the creator class. This explains the pattern name.
Usually, child classes are used to overwrite the type of the created product.

### When to use the pattern?
The pattern is useful when: 
* you want to separate object creation from its usage (might later evolve into Builder pattern).
* all objects of a certain hierarchy need to have the same creation method.  
* each object from the hierarchy requires its own input parameters.
* you want to allow extension of your code without making changes to the original factory (solution of the problem introduced by simple factory). 


### Example
You are building an application that represents the structure of a company:
* A company consists of several departments;
* Each departament hires the employees independently.

Let's assume that each employee has a certain interface (`EmployeeInterface`) which is implemented by concrete staff members like
`Programmer`, `Manager`, `Architect` etc. When a departament hires a new employee, it creates a new object with `EmployeeInterface` interface.
We will have a base departament class with abstract `create_employee()` factory method and all departament classes will be derived from this class.
Each time when you need to create a new employee and departament types, you just inherit from `BaseDepartament` class, and it gives you a new factory.

If you want to have more convenience in the client code, you can create a class which accepts an employee type and returns the needed instance - `EmployeeFactory`.
This class should also support adding new employee type to avoid changing the code.


## Abstract factory pattern
Abstract factory is handy when you want to have several families of objects.

### Example
You are building a cloud-based application which can work with different cloud providers: AWS and Azure. You need to be able
to send messages to the queue and also be able to have logging. You are going to have the following classes: `AWSLogger`, `AzureLogger`, `AWSQueueClient` and `AzureQueueClient`.

Instead of checking the configuration each time you need to send a message to the queue or log something, 
create logger and queue client interfaces (`QueueClientInterface`, `LoggingClientInterface`) and a factory that produces concrete objects. 
Since you are supporting several cloud services, create a factory interface `FactoryInterface` with `get_queue_client` and `get_logger` methods
and 2 concreate factories: one for each cloud service.


## Factory to use case matrix

| Factory type     | Use case                                                                                                                                        |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Simple factory   | 1. You don't mind changing the factory code when the new type of objects is created<br/> 2. You want to understand the idea of factory pattern. |
| Factory method   | 1. You want your code to be extensible without changing the code of original factory.                                                           |
| Abstract factory | 1. You need to work with different families of objects and don't want to depend on their implementations.                                       |
