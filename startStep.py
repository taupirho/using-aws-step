# Call a step function called sm1 from lambda 
import boto3
def lambda_handler(event, context):
    client = boto3.client('stepfunctions')
    response = client.start_execution(
        stateMachineArn='arn:aws:states:eu-west-2:XXXXXXXXXXXX:stateMachine:sm1',
        name="startStep",
        input="{}"
        ) 
