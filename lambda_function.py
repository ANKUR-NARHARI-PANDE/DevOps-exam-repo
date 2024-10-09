import json
import os
import requests
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
    
        subnet_id = os.environ.get('SUBNET_ID')
        if not subnet_id:
            raise ValueError("SUBNET_ID environment variable is not set.")
        
      
        payload = {
            "subnet_id": subnet_id,
            "name": "Ankur Narhari Pande",
            "email": "ankurrpande@gmail.com"
        }
        headers = {'X-Siemens-Auth': 'test'}
        
    
        response = requests.post('https://bc1yy8dzsg.execute-api.eu-west-1.amazonaws.com/v1/data', json=payload, headers=headers)
        
 
        response.raise_for_status()  

       
        return {
            'statusCode': response.status_code,
            'body': response.json()  
        }

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
