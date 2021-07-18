#!/bin/bash

cd ../

instanceid=$(cat shell/env/dev/instanceid.txt)
export STAGE="dev"
export INSTANCEID=$instanceid

serverless invoke local --function ec2Operator --path test/ec2operator_stop.json
