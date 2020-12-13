import os
import json
import boto3

BUCKET_NAME = os.environ['BUCKET_NAME']

json_key = "key"
s3 = boto3.resource('s3')
obj = s3.Object(BUCKET_NAME, json_key)


def lambda_handler(event, context):
    user_list = json.loads(obj.get()['Body'].read())

    print(user_list)

    user = user_list.get(str(event['user_id']))

    print(user)

    return {
        'user_id': event['user_id'],
        'user': user
    }
