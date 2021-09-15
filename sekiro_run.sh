#!/bin/bash

ps -ef | grep sekiro-service-demo | grep -v grep | awk '{print $2}' | xargs kill -9

sleep 3

nohup sh /srv/sekiro/bin/sekiro.sh >>/srv/sekiro/logs/nohup_sekiro_server.log 2>&1 &
