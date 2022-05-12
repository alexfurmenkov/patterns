# Visitor

### When to use the pattern?
When there is a need to extend existing hierarchy with new capabilities but the code of this hierarchy can't be changed.
Also, when the responsibility of the new capabilities differs from the hierarchy responsibility.

If you create a new class for the new functionality and include an object of the hierarchy to this class, you might end up
having a huge if/else block for handling different types of objects. In this case, the double dispatch technique might be a solution.

### Example
You have a set of classes that represent DB records (`DBUserModel`, `DBPostModel`) and need to add serialization capabilities.
You can't change the code of `DBUserModel`, `DBPostModel` because it is pretty stable and also do not want to extend it with unnecessary responsibilities.

What you can do is create a `SerializationVisitor` class. Of course, the class can have one generic method like `serialize` but 
we can end up having a large if/else block which will define the corresponding serialization logic for different types of objects. 

The pattern suggests the following approach: `SerializationVisitor` will have a set of methods for serializing each of the records
by accepting it: `serialize_user(user: DBUserModel)` or `serialize_post(post: DBPostModel)`. Then, we will use the double dispatch technique: `DBUserModel`, `DBPostModel` 
will implement an `AcceptVisitorInterface` with a public method `accept_visitor(visitor: SerializationVisitorInterface)` 
that will accept the visitor instance and call the corresponding serialization method. 
Finally, the client code will use model's `accept_visitor(visitor: SerializationVisitorInterface)` method for serialization.


**Advantage of the pattern is that we do not mix responsibilities, follow open/closed principle, and we are able to change the visitor on the fly.**

**The drawback is that it introduces circular dependencies: visitor depends on the model interface, model depends on the visitor interface.**
