sam build --use-container

sam package \
    --output-template-file packaged.yaml \
    --s3-bucket shhorsfi-sam-deploy

sam deploy \
    --template-file packaged.yaml \
    --stack-name nike-news-feed \
    --capabilities CAPABILITY_IAM