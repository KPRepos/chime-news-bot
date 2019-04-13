import cfnresponse
import boto3
import os

feeds_table = boto3.resource('dynamodb').Table(os.environ['FEEDS_TABLE'])

feeds_to_load = [
    {
        'title': 'AWS Updates',
        'url': 'http://aws.amazon.com/new/feed/',
        'icon': ':cloud:'
    }
]

def load_feeds(feeds):
    print(feeds)

    for feed in feeds:
        print(feed)
        response = feeds_table.put_item(Item=feed)
        print(response)

def lambda_handler(event, context):
    print(event)

    try:
        if event['RequestType'] == 'Create':
            load_feeds(feeds_to_load)
            response_data = {"Message": "Resource creation successful!", "Status": 'Create - Feeds Loaded'}
            cfnresponse.send(event, context, cfnresponse.SUCCESS, response_data)
        elif event['RequestType'] == 'Update':
            load_feeds(feeds_to_load)
            response_data = {"Message": "Resource creation successful!", "Status": 'Update - Feeds Loaded'}
            cfnresponse.send(event, context, cfnresponse.SUCCESS, response_data)
        elif event['RequestType'] == 'Delete':
            response_data = {"Message": "Resource deletion successful!"}
            cfnresponse.send(event, context, cfnresponse.SUCCESS, response_data)
        else:
            response_data = {"Message": "Unexpected event received from CloudFormation"}
            cfnresponse.send(event, context, cfnresponse.SUCCESS, response_data)

    except Exception as error:         
        print(error)
        response_data = {"Message": "Unexpected error occured."}
        cfnresponse.send(event, context, cfnresponse.FAILED, response_data)