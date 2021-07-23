#!/bin/bash
cd ../
export STAGE="dev"
export WEBHOOK_URL="dummy"
export AVATAR_URL="dummy"

read -p "アンデプロイを実施しますか？: " ANSWER

case $ANSWER in "Yes" | "yes" | "Y"  | "y" )
    serverless remove
    ;;
    * ) echo "アンデプロイは実施しません。"
esac