# Chain Of Responsibility

### When to use the pattern?
When you need to handle the incoming request with a sequence of steps and:
* you want to be able to build this sequence on the fly based on the runtime parameters;
* or you want to have a strict sequence of steps;
* or you don't know in advance what exactly should be done to handle the request, e.g. which part of the request should be validated.

### Example
You have an object with multiple properties and need to have a way to check its validity. For example, your web application
handles the incoming requests and needs to execute the checks in the given order:
1. Check the validity of authentication token.
2. Check that user's group is admin.
3. Check request payload.

What you can do is write a program that executes the checks step-by-step. While it is a suitable solution, imagine a situation
when you need to change the order of checks, say check request payload before checking the group. Then, you will need to rewrite
the algorithm. 

By using Chain Of Responsibility pattern, you are splitting each check into its own class and chain this classes together. 
This gives you the opportunity to change the order of checks based on the runtime conditions without changing the code of the algorithm. 
