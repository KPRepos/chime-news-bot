import json
import feedparser
import boto3
import os
import re

def lambda_handler(event, context):
    feeds_table = boto3.resource('dynamodb').Table(os.environ['FEEDS_TABLE'])
    items_table = boto3.resource('dynamodb').Table(os.environ['ITEMS_TABLE'])

    response = feeds_table.scan()
    feeds = response['Items']

    for url in feeds:
        print('Parsing Articles From: {}'.format(url))
        feed_data = feedparser.parse(url['name'])
        
        for entry in feed_data['entries']:
            print('Inserting Article: {}'.format(entry['title']))

            data = {
                'id': entry['title'],
                'name': re.sub('<[^<]+?>', '', entry['title']),
                'link': entry['link'],
                'feed': {
                    'title': feed_data['feed']['title'],
                    'icon': url['icon']             
                }
            }

            response = items_table.put_item(Item=data)
            print(response)