# Bridge

### When to use the pattern?
The ideal use case is when you need to split abstraction and implementation into two separate hierarchies.
In other words, if you feel that your program starts to develop in multiple separate directions (two or more), 
split it into several hierarchies and "bridge" them together.


### Example
You are building a web service which should provide rate of a certain cryptocurrency from different cryptocurrency 
exchanges like Binance, Coinbase etc.
Besides, your service is going to have different clients: some of them are going to use JSON, others require XML, HTML or CSV.
In order to avoid the large amount of classes like XMLBinanceClient, HTMLCoinbaseClient, JSONBinanceClient the pattern suggests
that you split the program in two hierarchies: one is responsible for communicating with cryptocurrency exchanges and another 
is responsible for returning the data in the format that the client needs. 
