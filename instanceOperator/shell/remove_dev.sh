#!/bin/bash
cd ../
export STAGE="dev"
export DOMAINNAME="dummy"
export HOSTZONEID="dummy"
export INSTANCEID="dummy"
export WEBHOOKURL="dummy"

read -p "アンデプロイを実施しますか？: " ANSWER

case $ANSWER in "Yes" | "yes" | "Y"  | "y" )
    serverless remove
    ;;
    * ) echo "アンデプロイは実施しません。"
esac