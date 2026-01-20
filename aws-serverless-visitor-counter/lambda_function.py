import json
import boto3

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCount')

def lambda_handler(event, context):
    # Update the item in DynamoDB
    response = table.update_item(
        Key={'id': 'total_visits'},
        UpdateExpression='SET #c = #c + :val',
        ExpressionAttributeNames={'#c': 'count'},
        ExpressionAttributeValues={':val': 1},
        ReturnValues="UPDATED_NEW"
    )
    
    # Get the new count
    new_count = response['Attributes']['count']
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*', # Useful for later if you build a website
            'Content-Type': 'application/json'
        },
        'body': json.dumps({'total_visits': int(new_count)})
    }