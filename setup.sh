#!/usr/bin/env bash

set -e

if [[ $(id -u) -ne 0 ]];then
    echo "Please run as root"
    exit 1
fi

id -u piswitch >/dev/null 2>&1
if [[ "$?" != "0" ]];then
    /usr/bin/env useradd piswitch
fi

if [[ ! -d /piswitch ]];then
    mkdir -p /piswitch
fi

if [[ ! -f /piswitch/piswitch.py ]];then
    cp ./piswitch.py /piswitch/piswitch.py
fi

if [[ ! -f /piswitch/keyboard.py ]];then
    cp ./piswitch.py /piswitch/keyboard.py
fi

if [[ ! -f /etc/systemd/system/piswitch.service ]];then
    cp ./piswitch.service /etc/systemd/system/piswitch.service
    /usr/bin/env systemctl daemon-reload
fi

/usr/bin/env systemctl is-enabled piswitch.service
if [[ "$?" != "0" ]];then
    /usr/bin/env systemctl enable piswitch.service
fi

echo "Setup was successful. The service will start on reboot."
