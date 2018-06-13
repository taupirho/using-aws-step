import boto3
def lambda_handler(event, context):
    client = boto3.client('stepfunctions')
    response = client.start_execution(
        stateMachineArn='arn:aws:states:eu-west-2:696353118745:stateMachine:Mychoice',
        name="startStep",
        input="{\"bucket\":\"taupirho\",\"file\":\"iholding/issueholding.txt\",\"fsize\":\"0\"}"
        ) 
