# Mediator 


### When to use the pattern?
When you want to decouple different objects that communicate to each other and make them depend on one interface only. 
In this case, you create a mediator class that only accepts the message from the sender object and knows where to send it. The communication now becomes centralized.


### Example
You are building a parking app. You don't want the cars to communicate to each other because the communication will be very chaotic.
You can create a mediator class (`ParkingAssistant`) which will manage the parking and assign parking positions to each newly arrived car.
