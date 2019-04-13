# chime-news-feed

Posts relevant news to a Chime chat channel

## Deploy

### Build

```
sam build --template src/template.yaml --use-container
```

### Package

Replace [YOUR_S3_BUCKET] with the bucket you'll use to hold deployment artifacts.

```
sam package \
    --template-file src/template.yaml \
    --output-template-file src/packaged.yaml \
    --s3-bucket [YOUR_S3_BUCKET]
```

### Deploy

```
sam deploy \
    --template-file src/packaged.yaml \
    --stack-name chime-news-feed \
    --capabilities CAPABILITY_IAM
```

### Post Deploy

Update the Feeds DynamoDB table with the RSS feeds you want to monitor. The tables take two fields, name and icon where icon is a Chime emoticon, ie: :shoe:

```
http://news.nike.com/feed
https://medium.com/feed/nikeengineering
https://www.google.com/alerts/feeds/07210583599130068765/9196744403596228241 
```