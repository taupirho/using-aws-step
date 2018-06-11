# aws-step-functions

Just a quick intro to AWS step functions and how they can be called via a Lambda function. In 2016 Amazon introduced a new 
service called Amazon Step Functions. There are a way to coordinate the the flow of distributed applications using a visual 
work flow toolset and state machines. Step functions normally call lambda functions but they differ in that they can be long 
running processes (up to a  year) rather than the 5 minute max run time of a regular AWS lambda function. 

This will be a very simple example. We will have 1 step function that will print out the text "Hello World". We will 
have two lambda functions, one called by the step function to print out the # Hello World string and one that 
will call the step function itself.
