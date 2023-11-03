#!/bin/bash

count=0
while true; do
    sudo systemctl stop dhcpcd
    sleep 5

    sudo systemctl start dhcpcd

    curl http://ipv4.download.thinkbroadband.com/20MB.zip> 20MB.zip
    rm 20MB.zip
    
    count=$(expr $count + 1)
    current_date=$(date '+%Y-%m-%d %H:%M:%S')
    echo "$current_date,$count" >> "count.csv"
done
