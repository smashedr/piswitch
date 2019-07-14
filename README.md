# PiSwitch Core

Automagically enter Mario Maker 2 Level ID's into the Nintendo Switch.

## Client Setup

Currently in a .rtf to be printed and packaged.

## Troubleshooting

You can SSH to the device on port 22 with the provided username and password.

Some useful commands:

```
systemctl status piswitch
systemctl restart piswitch

journalctl -fu piswitch
```

## Installtion

1. Install system, connect network, enable ssh, update system.
   1. `raspi-config`
   1. `apt install -y vim autossh git`
   1. Set hostname, password, ssh keys, profile, etc.
1. Install https://github.com/jasbur/RaspiWiFi
   1. `python3 initial_setup.py`
   1. Enable Auto-Config mode
1. Install PiSwitch https://git.cssnr.com/shane/pi-switch
   1. `bash setup.sh`
   1. DO NOT REBOOT
   1. `vim /piswitch/settings.env`
1. Install pi-as-keyboard https://github.com/c4software/pi-as-keyboard
   1. `bash setup.sh`
   1. `reboot`
1. Install backdoor:
   1. Add autossh unit file
   1. Add private key from tunnel server
   1. Enable the tunnel service
1. Place device back in Configuration Mode
   1. `python3 /usr/lib/raspiwifi/reset_device/manual_reset.py`

## Sources

This project uses these projects:

- https://github.com/c4software/pi-as-keyboard
- https://github.com/jasbur/RaspiWiFi
