from __future__ import print_function

import json
import urllib
import boto3
import os

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    # uncomment the 2 lines below here if this lambda is going to be run
    # in response to an S3 PUT event
    #bucket = event['Records'][0]['s3']['bucket']['name']
    #key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
    
    bucket = os.environ['bucket']
    key = os.environ['file']
  
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print("CONTENT Length (bytes): " + str(response['ContentLength']))
        # This goes into the $ path variable
        return response['ContentLength']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

