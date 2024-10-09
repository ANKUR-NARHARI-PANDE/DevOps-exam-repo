import boto3
import json
import os

def lambda_handler(event, context):
    subnet_id = os.environ['SUBNET_ID']
    name = "Ankur Pande"
    email = "ankurrpande@gmail.com"

    client = boto3.client('lambda')

    response = client.invoke(
        FunctionName="my_lambda_function_new",
        Payload=json.dumps({
            "subnet_id": subnet_id,
            "name": name,
            "email": email
        })
    )

    payload = json.loads(response['Payload']['Payload'].read().decode('utf-8'))
    print(payload)

    return {
        'statusCode': 200,
        'body': json.dumps(payload)
    }
