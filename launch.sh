#!/bin/bash
xset s noblank
xset -dpms
xset -s off

cd /home/pi/dynatestjig
/usr/bin/python3 ui.py

