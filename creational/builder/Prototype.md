# Builder

### When to use the pattern?
The pattern allows you to fill the objects with the properties step by step. It is especially useful when a certain class
has a huge constructor, e.g. 10 obligatory parameters which are not always needed, and you use 4 of them in the majority of cases. 
In order to avoid passing other parameters as nulls, the idea is to move the creation process behind the original class 
and delegate this work to a separate Builder class. The builder class does not have a huge constructor, it provides a number 
of convenient setter methods which can be called independently - to create the needed configuration of the object. 
This way, you can construct your objects only with the necessary properties.

You can also go one step further and create a Director class that encapsulates a Builder object and acts like a wrapper over
the Builder with an already defined building logic which is commonly used across your program. 


### Example
In the example, a `House` class is a class with a large set of input parameters. `HouseBuilderInterface` is an interface that
must be implemented by all concrete builders in order to be interchangeable in `Director` class. An example of a concrete builder 
is a `Builder` class.

**Python note:** the pattern might be replaced with a built-in language feature: Python supports default values of arguments. 