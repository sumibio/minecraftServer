#!/bin/bash
bash update_server.sh
SCREEN_NAME='minecraft'
screen -DmS $SCREEN_NAME java -Xms3G -Xmx3G -jar server.jar --nogui
