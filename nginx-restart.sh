#! /bin/bash
#Rommel Nginx maintenance restart 
# The point of this is to provide restart once a day  at 12 AM every midnight 
# will provided in a crontab

echo "-- NGIINX MIDNIGHT RESTART IN PROGRESS --"  
date
systemctl restart nginx

ps -ef |grep -i nginx |grep -v grep
