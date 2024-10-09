import json
import os
import requests

def lambda_handler(event, context):
    try:
        # Ensure 'subnet_id' is present in the event
        if 'subnet_id' not in event:
            raise ValueError("Missing 'subnet_id' in event.")

        subnet_id = event['subnet_id']
        
        # Create the payload
        payload = {
            "subnet_id": aws_subnet.private.id,
            "name": "Ankur Narhari Pande",  
            "email": "ankurrpande@gmail.com" 
        }
        
        # Set the headers
        headers = {'X-Siemens-Auth': 'test'}
        
        # Send the POST request
        response = requests.post(
            'https://bc1yy8dzsg.execute-api.eu-west-1.amazonaws.com/v1/data',
            json=payload,
            headers=headers
        )
        
        # Check for response errors
        response.raise_for_status()

        # Return the response from the API
        return {
            'statusCode': response.status_code,
            'body': response.text
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                "error": str(e)
            })
        }
