import json
import requests
import os
import time
import cfnresponse

webhook = os.environ['CHIME_WEBHOOK']

def send_notification(action):

    payload = {}

    if action == 'Create':
        payload = {
            'Content': '{} {}\n{}'.format(':mailbox:', 'Bot Notification','Bot Created')
        }
    elif action == 'Update':
        payload = {
            'Content': '{} {}\n{}'.format(':mailbox:', 'Bot Notification','Bot Updated')
        }   
    elif action =='Delete':
        payload = {
            'Content': '{} {}\n{}'.format(':mailbox:', 'Bot Notification','Bot Removed')
        }

    response = requests.post(webhook, data=json.dumps(payload))
    print(response)

def lambda_handler(event, context):
    print(event)

    try:
        if event['RequestType'] == 'Create':
            send_notification('Create')
            response_data = {"Message": "Resource creation successful!", "Status": 'Create - Send Notifications'}
            cfnresponse.send(event, context, cfnresponse.SUCCESS, response_data)
        elif event['RequestType'] == 'Update':
            send_notification('Update')
            response_data = {"Message": "Resource creation successful!", "Status": 'Update - Send Notifications'}
            cfnresponse.send(event, context, cfnresponse.SUCCESS, response_data)
        elif event['RequestType'] == 'Delete':
            send_notification('Delete')
            response_data = {"Message": "Resource deletion successful!"}
            cfnresponse.send(event, context, cfnresponse.SUCCESS, response_data)
        else:
            response_data = {"Message": "Unexpected event received from CloudFormation"}
            cfnresponse.send(event, context, cfnresponse.SUCCESS, response_data)

    except Exception as error:         
        print(error)
        response_data = {"Message": "Unexpected error occured."}
        cfnresponse.send(event, context, cfnresponse.FAILED, response_data)