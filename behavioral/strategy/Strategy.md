# Strategy

### When to use the pattern?
Strategy pattern is a good alternative to if/else blocks. Instead of writing complex if/else conditions, the pattern suggests 
transforming each block into a class with a common interface and delegate the work to this class.

### Example
You are building a tool for extracting contents from datasets. A dataset is just a .xpt file. Your clients need to be able to
extract not only the dataset contents but its metadata as well. You expect the client to provide the desired type (contents or metadata)
and the program should do the trick. Of course, you can start with if/else but each time when you need to add a new feature, 
you will have to extend this if/else block. 

Instead, create a set of classes called strategies. The classes will implement the same interface and will perform the actual data extraction
under the hood. 