# Chain Of Responsibility


### When to use the pattern?
When you need to handle the incoming request with a sequence of steps and be able to build this sequence on the fly.

### Example
You have an object with multiple properties and need to have a way to check its validity. For example, your web application
handles the incoming requests and needs to execute the checks in the given order:
1. Check authentication token.
2. Check user's group.
3. Check user's role.
4. Check request payload.

What you can do is write a program that executes the checks step-by-step. While it is a suitable solution, imagine a situation
when you need to change the order of checks, say check request payload before checking the group. Then, you will need to rewrite
the algorithm. 

By using Chain Of Responsibility pattern, you get the opportunity to change the order of checks based on the runtime conditions
without changing the code of the algorithm. 