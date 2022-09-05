import json
import boto3
import numbers

def lambda_handler(event, context):
    username = event['username']
    email = event['email']
    contect = event['contact']
    sns = boto3.client('sns')
    response = sns.publish(
        TopicArn='arn:aws:sns:eu-central-1:601641875992:topic',
        Message='it works!'
        )
        
    numbers='{"num1":30,"num2":8}'
    result=json.loads(numbers)
    return {
        'statusCode': 200,
        'body': (result["num1"]+result["num2"])
    }
    
    return response
