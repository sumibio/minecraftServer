#!/bin/bash

. ./env/.env_prd

if [ -z $webhook_url ]; then
    echo "webhook_urlを指定してください"
    exit 1
fi
echo "webhook_url："$webhook_url

if [ -z $avatar_url ]; then
    echo "avatar_urlを指定してください"
    exit 1
fi
echo "avatar_url："$avatar_url

cd ../
read -p "デプロイを実施しますか？: " ANSWER
case $ANSWER in "Yes")
    echo "デプロイを実施します。"
    export STAGE="prd"
    export WEBHOOK_URL=$webhook_url
    export AVATAR_URL=$avatar_url
    serverless deploy
    ;;
    * ) echo "デプロイは実施しません。"
esac