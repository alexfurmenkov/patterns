# Composite

### When to use the pattern?
Composite pattern is useful when a group of different objects should be treated uniformly.
Say, when you need to do the same operation for each object in a group, and you don't want to distinguish their types,
you just need to call the same method for each object. When you are handling nested objects and do not know in advance 
if an object is nested or no.

### Example
The easiest and most explicit example would be a company with an employee hierarchy.
There can be software developers which are subordinates of a project manager. At the same time,
the manager is headed by a unit manager which is a subordinate of a company CEO.

The idea of the pattern is to create a tree-like structure where the root is a composite object (CEO in our example) 
which includes the child nodes (managers and developers in our example).
Imagine the situation when we need to list the details of each company employee. Instead of iterating through all employees 
and requesting the details for an individual person, we are calling CEO's `get_details()` method which prints all subordinates' details.  

**The pattern has several key principles:**
* Component interface. Defines an interface which is implemented by all node of the tree.
* Leaf node. A primitive object (developer in the example).
* Composite node. Stores the list of child components and implements the component interface for each child (Manager in the example).
