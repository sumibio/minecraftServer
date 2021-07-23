#!/bin/bash

cd ../

. ./shell/env/.env_dev
export STAGE="dev"
export WEBHOOK_URL=$webhook_url
export AVATAR_URL=$avatar_url
export DOMAIN_NAME=$domain_name
export HOSTEDZONE_ID=$hostedzone_id
export INSTANCE_ID=$instance_id

serverless invoke local --function ec2Operator --path test/ec2operator_start.json
