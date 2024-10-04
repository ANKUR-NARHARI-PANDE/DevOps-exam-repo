import json
import boto3
import requests
import os

def lambda_handler(event, context):
    subnet_id = os.environ['SUBNET_ID']  # Set this in Terraform
    payload = {
        "subnet_id": aws_subnet.private.id,
        "name": "Ankur Pande",
        "email": "ankurrpande@gmail.com"
    }

    headers = {'X-Siemens-Auth': 'test'}
    response = requests.post('https://bc1yy8dzsg.execute-api.eu-west-1.amazonaws.com/v1/data', json=payload, headers=headers)
    
    return {
        'statusCode': response.status_code,
        'body': response.text
    }
