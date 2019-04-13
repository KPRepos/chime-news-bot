import json
import requests
import os
import time

webhook = os.environ['CHIME_WEBHOOK']

def lambda_handler(event, context):
    print(event)
    for record in event['Records']:
        if record['eventName'] == 'INSERT':
            item = record['dynamodb']['NewImage']

            print('New Item Detected: {} '.format(item))

            payload = {
                'Content': '{} {}\n{}\n{}'.format(item['feed']['M']['icon']['S'], item['feed']['M']['title']['S'], item['name']['S'], item['link']['S'])
            }

            response = requests.post(webhook, data=json.dumps(payload))
            print(response)
            time.sleep(1)