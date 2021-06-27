#!/bin/bash
cd ../
export STAGE="prd"
export DOMAINNAME="dummy"
export HOSTZONEID="dummy"
export INSTANSID="dummy"
export WEBHOOKURL="dummy"

read -p "アンデプロイを実施しますか？: " ANSWER

case $ANSWER in "Yes")
    serverless remove
    ;;
    * ) echo "アンデプロイは実施しません。"
esac