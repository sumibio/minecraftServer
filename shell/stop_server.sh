#!/bin/sh

# screenの名前
SCREEN_NAME='minecraft'

if [ -n "$(screen -list | grep -o "${SCREEN_NAME}")" ]; then
    echo [date '+%F %T'] 'server stop script start'
    screen -S $SCREEN_NAME -X stuff 'say 30秒後にサーバーを停止します\015'
    sleep 30s
    screen -S $SCREEN_NAME -X stuff 'save-all\015'
    sleep 5s
    screen -S $SCREEN_NAME -X stuff 'stop\015'
else
    echo [date '+%F %T']  'server is not runnning'
fi