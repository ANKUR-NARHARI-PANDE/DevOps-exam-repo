# import os
# import json
# import requests

# def lambda_handler(event, context):
#     subnet_id = os.environ['SUBNET_ID']
#     payload = {
#         "subnet_id": aws_subnet.private.id,
#         "name": "Ankur Pande",
#         "email": "ankurrpande@gmail.com"
#     }
#     import pip
#     pip.main(['install', 'requests'])

#     headers = {'X-Siemens-Auth': 'test'}
#     response = requests.post(
#         'https://bc1yy8dzsg.execute-api.eu-west-1.amazonaws.com/v1/data',
#         json=payload,
#         headers=headers
#     )

#     print("Response Status Code:", response.status_code)
#     print("Response Body:", response.text)

#     return {
#         'statusCode': response.status_code,
#         'body': response.text
#     }

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