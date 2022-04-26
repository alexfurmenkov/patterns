# Flyweight

### When to use the pattern?
When there is a need to create A LOT of similar objects and save RAM. According to the pattern, you need to identify
common attributes between all the objects (so-called internal state) and move them to another **immutable flyweight class** so that it could be reused. 
After that, you will be creating only one instance of this flyweight.  

Of course, there can be some attributes that are unique for each object. The idea is to have a separate context object that
will hold this attributes and a reference to the flyweight. Despite the fact that you will have to store the context objects,
a context object + reference to the flyweight will take much less space than having an internal state in each object. 
Usually, a factory is used to control the creation of flyweights. 

### Example
Imagine we are building a shooter game where a huge number of players can be created. Each player has its unique attributes (external state) like
weapon, name. At the same time, all players have a set of common attributes (internal state): team and mission. 

If we create 1000000 instances storing internal and external states, we can run out of memory. So, we will create a separate class for storing internal state - `PlayerType`
and external state will be stored in the `Player` class which will also hold a reference to `PlayerType`. Finally, the `PlayerFactory` class
will ensure that only one instance of `PlayerType` has been created during the program execution.