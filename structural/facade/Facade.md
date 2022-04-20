# Facade

### When to use the pattern?
The ideal use case is when you need to implement a simple interface to a complex system.


### Example
There is an authentication system which allows creating new users, authenticating existing users, logging them in, etc.
The problem is that this system consists of several classes whereas the client does not want to interact with all these 
classes. He only needs to be able to signup and login.

The solution is to create a class (facade) which will provide a simple interface to this complex system.

In our example, the authentication system is represented by a class AuthenticationSystem. It is responsible for 
handling authentication, authorization, hashing passwords and generating authentication tokens. AuthenticationSystem 
class interacts with another class - UserDBModel. This class is responsible for saving new users to the DB and 
retrieving them from this DB. Finally, the facade which provides a convenient interface is implemented by 
AuthenticationSystemFacade class.

**Important note - in this example the database is a python list because the idea is just to show the 
pattern, so launching the whole DB server would be too much.**  