import json
import os
import requests
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        # Get the subnet ID from environment variables
        subnet_id = os.environ.get('SUBNET_ID')
        if not subnet_id:
            raise ValueError("SUBNET_ID environment variable is not set.")
        
        # Create the payload
        payload = {
            "subnet_id": subnet_id,
            "name": "Ankur Narhari Pande",
            "email": "ankurrpande@gmail.com"
        }
        
        # Set the headers
        headers = {'X-Siemens-Auth': 'test'}
        
        # Send the POST request
        response = requests.post('https://bc1yy8dzsg.execute-api.eu-west-1.amazonaws.com/v1/data', json=payload, headers=headers)
        
        # Check for successful response
        response.raise_for_status()  # Raises an error for bad responses (4xx and 5xx)

        # Return the response from the API
        return {
            'statusCode': response.status_code,
            'body': response.json()  # Use .json() for JSON response
        }

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
