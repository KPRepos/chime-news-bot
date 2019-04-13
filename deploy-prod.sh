sam build --use-container

sam package \
    --output-template-file packaged-prod.yaml \
    --s3-bucket shhorsfi-sam-deploy

sam deploy \
    --template-file packaged-prod.yaml \
    --stack-name chime-news-feed-prod \
    --capabilities CAPABILITY_IAM \
    --parameter-overrides \
    ChimeWebHookURL=https://hooks.chime.aws/incomingwebhooks/3a360fd3-83fc-4440-8953-9d833308efa6?token=ek9xbHducVl8MXxJUzdHWmRqMF9WX2VRUW8tUXJ5VDJfSGI1NHF3emxUU2RXOEV6U0Z5akp3