import json
import feedparser
import boto3
import os
import re
import urllib

feeds_table = boto3.resource('dynamodb').Table(os.environ['FEEDS_TABLE'])
items_table = boto3.resource('dynamodb').Table(os.environ['ITEMS_TABLE'])

def lambda_handler(event, context):
    print(event)

    response = feeds_table.scan()
    feeds = response['Items']

    for feed in feeds:
        print('Parsing Articles From: {}'.format(feed))
        feed_data = feedparser.parse(feed['url'])

        print(feed_data.version)
        
        if feed_data.version == 'rss20':
            for entry in feed_data.entries:
                print('Inserting Article: {}'.format(entry.title))

                data = {
                    'id': entry.link,
                    'name': re.sub('<[^<]+?>', '', urllib.parse.unquote(entry.title)),
                    'link': entry.link,
                    'feed': {
                        'title': feed['title'],
                        'icon': feed['icon']             
                    }
                }

                response = items_table.put_item(Item=data)
                print(response)                
        else:
            print('Feed Version Not Supported: {}'.format(feed_data.version))