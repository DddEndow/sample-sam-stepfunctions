import os
import json
import boto3

BUCKET_NAME = os.environ['BUCKET_NAME']


def lambda_handler(event, context):
    """ 
        S3にユーザーデータを保存し、ユーザーのIDのリストを返す。
    """

    json_key = "key"
    s3 = boto3.resource('s3')
    obj = s3.Object(BUCKET_NAME, json_key)

    user_list_json = {
        1: {
            'name': 'user1',
            'age': 21
        },
        2: {
            'name': 'user2',
            'age': 22
        },
        3: {
            'name': 'user3',
            'age': 23
        }
    }

    r = obj.put(Body = json.dumps(user_list_json))

    obj.get()['Body'].read()

    return {
        's3_key': json_key,
        'user_id_list': [1, 2, 3]
    }
