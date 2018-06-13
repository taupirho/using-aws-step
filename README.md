# aws-step-functions

Just a quick intro to AWS step functions and how they can be called via a Lambda function to orchestrate other lambda functions. 
In 2016 Amazon introduced a new service called Amazon Step Functions. They are a way to build and coordinate the flow of distributed 
lambdas using a visual work flow toolset and state machines. Step functions differ from lambda functions in that they can be long 
running processes (up to a  year) rather than the 5 minute max run time of a regular AWS lambda function. 

The workflow description is as follows. let's say we have a file on AWS S3 that we want to process. The first thing we want to do is 
check some meta data ofthe file - in this case its size in bytes. If the file size is > 2Mb we will do some further processing on
the file. If the file size is < 2Mb we will simply notfiy the user that the file is too small to process. If for 
some reason neither of these conditions exist we notify the user that a problem has occurred. To implement the above we need 
the following:

1) A step function state machine
2) A lambda function (startStep) to call the start state of the state machine (there are other ways to do this too)

3) A lambda function (checkSize) that gets the size in bytes of the required file. We set environment variables to hold the target 
bucket and filename and read these from within our lambda. It returns this value into the $ path variable.
   
4) A lambda function (ProcessFile) which processes the file if it is of sufficient size


In terms of IAM roles for this we just used the default lambda_basic_exection for the lambdas that are called by the step function.
For the lambda function that calls the step function we created a new IAM role with two built-in policies:-  CloudWatchLogsFullAccess 
and AwsStepFunctionsFullAccess

A representation of the state machine is shown below.

![AWS State Machine](https://github.com/taupirho/aws-step-functions/blob/master/sm1.png)

It's pretty simple and the only things I haven't talked about are the NotifyOk and NotifyNotOk nodes. These are called PASS states in AWS Step. 
They are basically do nothing or No Op states taht simply pass their input to their output. They are just used to end our state machine 
run and output a message. The DefaultState is a catch all that deals with the scenario if for whatever reason we can't get the file size  
