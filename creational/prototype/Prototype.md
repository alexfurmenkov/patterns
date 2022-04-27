# Prototype

### When to use the pattern?
The pattern is very handy when you need to make an object copyable without diving into its implementation.
When you just want to call `copy()` and expect to get a completely different object.

### Example
You are creating a conveyor that produces robots. So, when running then conveyor you expect that some number of different 
robots to be created. Of course, the robots can look and act the same, but they should be independent - point to different
memory locations.

What you can do is to create a robot prototype and copy it each time when creating a new one while the conveyor is running.