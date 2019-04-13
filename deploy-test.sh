sam build --use-container

sam package \
    --output-template-file packaged-test.yaml \
    --s3-bucket shhorsfi-sam-deploy

sam deploy \
    --template-file packaged-test.yaml \
    --stack-name chime-news-feed-test-env \
    --capabilities CAPABILITY_IAM \
    --parameter-overrides \
    ChimeWebHookURL=https://hooks.chime.aws/incomingwebhooks/c79f0167-47fc-4fea-8744-5dd87d520462?token=MmRHcVg1SDB8MXxxMndjT3BBWlB5S2ZHR0ZvczYwZzgxX1dmQlRQTU9qVE9rd18wVUwtdGdv
