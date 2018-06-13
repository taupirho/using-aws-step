# This doesn't do anything useful just now
# Just prints out a message
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    print("Processing input file")
