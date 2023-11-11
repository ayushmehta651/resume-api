import json
import boto3

dynamodb = boto3.resource("dynamodb")
table=dynamodb.Table('Resumes')

def handler(event, context):

    # fetch the json resume data using the id
    response = table.get_item(
        Key={
            'resume_id': '1',
        }
    )
    print(response)

    if 'Item' not in response:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Resume content not present in Database', 'resume_content': ""})
        }

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Resume content fetched succesfully', 'resume_content': response['Item']})
    }
    
