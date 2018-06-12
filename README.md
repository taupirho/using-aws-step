# aws-step-functions

Just a quick intro to AWS step functions and how they can be called via a Lambda function. In 2016 Amazon introduced a new 
service called Amazon Step Functions. They are a way build and coordinate the flow of distributed lambdas using a visual 
work flow toolset and state machines. Step functions differ from lambda functions in that they can be long 
running processes (up to a  year) rather than the 5 minute max run time of a regular AWS lambda function. 

This will start off as a very simple example but I hope to increase its complexity over time to do something thats 
actually useful. Initially we will have 1 step function in JSON format that will print out the text "Hello World". We will 
create two lambda python functions, one called by the step function to print out the Hello World string and one that 
will call the step function itself.

In terms of IAM roles for this we just used the default lambda_basic_exection for the lambda that is called by the step function.
For the lambda function that calls the step function we created a new IAM role with two built-in policies:-  CloudWatchLogsFullAccess 
and AwsStepFunctionsFullAccess
