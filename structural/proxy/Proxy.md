# Proxy

### When to use the pattern?
If you need to control access to a certain object. The proxy pattern allows to substitute the original object
with other proxy objects that control access to the original object.  


### Example
Proxy pattern has different use cases. For example, you can use it as a caching service for an object that performs 
heavy operations. Instead of loading these operations each time, you can ask proxy to do it once and keep the result.

Another example is when there is a need to limit the access to an object. Then, you create a proxy that intercepts calls
to the original object and checks the access before calling the original one. 