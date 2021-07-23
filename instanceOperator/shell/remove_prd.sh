#!/bin/bash
cd ../
export STAGE="prd"
export DOMAIN_NAME="dummy"
export HOSTZONE_ID="dummy"
export INSTANCE_ID="dummy"
export WEBHOOK_URL="dummy"
export AVATAR_URL="dummy"

read -p "アンデプロイを実施しますか？: " ANSWER

case $ANSWER in "Yes")
    serverless remove
    ;;
    * ) echo "アンデプロイは実施しません。"
esac