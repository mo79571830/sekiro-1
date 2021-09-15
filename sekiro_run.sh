#!/bin/bash

ps -ef | grep sekiro-service-demo | grep -v grep | awk '{print $2}' | xargs kill -9

echo "sekiro服务清除成功"

sleep 3

nohup sh /srv/sekiro/bin/sekiro.sh >>/srv/sekiro/logs/nohup_sekiro_server.log 2>&1 &

echo "sekiro服务启动成功 /srv/sekiro/logs/nohup_sekiro_server.log"

sleep 3
