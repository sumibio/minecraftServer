#!/bin/bash

instanceid=$(cat env/prd/instanceid.txt)

if [ -z $instanceid ]; then
    echo "インスタンスIDを指定してください"
    exit 1
fi
echo "インスタンスID："$instanceid

hostzoneid=$(cat env/prd/hostzoneid.txt)
if [ -z $hostzoneid ]; then
    echo "ホストゾーンIDを指定してください"
    exit 1
fi
echo "ホストゾーンID："$hostzoneid

domainname=$(cat env/prd/domainname.txt)
if [ -z $domainname ]; then
    echo "ドメインネームを指定してください"
    exit 1
fi
echo "ドメインネーム："$domainname

webhookurl=$(cat env/prd/webhookurl.txt)
if [ -z $webhookurl ]; then
    echo "webhookurlを指定してください"
    exit 1
fi
echo "webhookurl："$webhookurl

cd ../
read -p "デプロイを実施しますか？: " ANSWER
case $ANSWER in "Yes")
    echo "デプロイを実施します。"
    export STAGE="prd"
    export WEBHOOKURL=$webhookurl
    export DOMAINNAME=$domainname
    export HOSTZONEID=$hostzoneid
    export INSTANCEID=$instanceid
    serverless deploy
    ;;
    * ) echo "デプロイは実施しません。"
esac