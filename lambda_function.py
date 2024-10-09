import json
import os
import requests

def lambda_handler(event, context):
    # Get the subnet ID from the environment variable
    subnet_id = os.environ['SUBNET_ID']
    
    # Create the payload
    payload = {
        "subnet_id": subnet_id,
        "name": "Ankur Narhari Pande",  
        "email": "ankurrpande@gmail.com" 
    }
    
    # Set the headers
    headers = {'X-Siemens-Auth': 'test'}
    
    # Send the POST request
    try:
        response = requests.post('https://bc1yy8dzsg.execute-api.eu-west-1.amazonaws.com/v1/data', json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
    
    # Return the response from the API
    return {
        'statusCode': response.status_code,
        'body': response.text
    }
