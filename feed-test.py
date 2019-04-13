import feedparser
import re

feeds = [
    {
        'name': 'http://aws.amazon.com/new/feed/',
        'icon': 'shoe'
    }
]

for url in feeds:
    print('Parsing Articles From: {}'.format(url))
    feed_data = feedparser.parse(url['name'])

    print(feed_data.version)
     
    if feed_data.version == 'rss20':
        for entry in feed_data.entries:
            print('Inserting Article: {}'.format(entry.title))

            data = {
                'id': entry.title,
                'name': re.sub('<[^<]+?>', '', entry.title),
                'link': entry.link,
                'feed': {
                    'title': feed_data.feed.title,
                    'icon': url['icon']             
                }
            }

            print(data)
    else:
        print('Feed Version Not Supported: {}'.format(feed_data.version))