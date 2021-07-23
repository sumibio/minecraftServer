#!/bin/bash
sudo chown ec2-user:ec2-user ./*
mkdir /home/ec2-user/minecraft/
mv /home/ec2-user/start_server.sh /home/ec2-user/minecraft/
mv /home/ec2-user/stop_server.sh /home/ec2-user/minecraft/
mv /home/ec2-user/update_server.sh /home/ec2-user/minecraft/

cd /home/ec2-user/minecraft

MANIFEST_URL=https://launchermeta.mojang.com/mc/game/version_manifest.json
MANIFEST=$(curl $MANIFEST_URL)
LATEST_RELEASE=$(echo $MANIFEST | jq -r '.latest.release')
echo $LATEST_RELEASE > .server_current

URL_ARGUMENTS=$(echo $MANIFEST | jq -r ".versions | map(select(.id == \"${LATEST_RELEASE}\"))[0].url")
URL_SERVER_DL=$(curl $URL_ARGUMENTS | jq -r "select(.id == \"${LATEST_RELEASE}\").downloads.server.url")
wget -q $URL_SERVER_DL -O server.jar

java -Xms1024M -Xmx1024M -jar server.jar --nogui
echo 'eula=true' > eula.txt

sudo chown -R ec2-user:ec2-user ./*

cd /home/ec2-user/

sudo chown root:root minecraft_server.service
sudo mv minecraft_server.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable minecraft_server
