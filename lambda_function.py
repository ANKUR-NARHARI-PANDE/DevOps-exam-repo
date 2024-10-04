import os
import json
import requests

def lambda_handler(event, context):
    subnet_id = os.environ['SUBNET_ID']
    payload = {
        "subnet_id": aws_subnet.private.id,
        "name": "Ankur Pande",
        "email": "amkurrpande@gmail.com"
    }

    headers = {'X-Siemens-Auth': 'test'}
    response = requests.post(
        'https://bc1yy8dzsg.execute-api.eu-west-1.amazonaws.com/v1/data',
        json=payload,
        headers=headers
    )

    print("Response Status Code:", response.status_code)
    print("Response Body:", response.text)

    return {
        'statusCode': response.status_code,
        'body': response.text
    }
