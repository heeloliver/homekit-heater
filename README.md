# homekit-heater
Raspberry Pi code for controlling a heater in my room. 

# overview
A heater in my room can be turned on or off by twisting a knob on the side. The idea is to enable a servo motor to twist the knob via the GPIO pins on a Raspberry Pi. The Raspberry Pi will run this command via Homebridge, so I'll be able to control this action via the Homekit platform remotely. 

# setup
I used [this](https://github.com/nfarina/homebridge/wiki/Install-Homebridge-on-Raspbian) guide to setup homebridge on my pi.

I used [this](https://www.npmjs.com/package/homebridge-gpio-cmd) npm package to enable gpio pin editing.

# location of homebridge files
/var/lib/homebridge/

# common commands
restart - systemctl restart homebridge

stop - systemctl stop homebridge

start - systemctl start homebridge

view logs - journalctl -f -n 100 -u homebridge
