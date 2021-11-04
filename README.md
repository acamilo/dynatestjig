# dynatestjig
## Image Setup Instructions
### Set up a fresh SD Card
The image used is the light version of raspbian, Without a GUI.
https://downloads.raspberrypi.org/raspios_lite_armhf/images/raspios_lite_armhf-2021-05-28/2021-05-07-raspios-buster-armhf-lite.zip
Download, extract, flash with balena etcher (or Disks in ubuntu) onto a SD card.

Follow this guide to set up wireless and SSH. You need to add 2 files to the BOOT drive that shows up after the flashing is done.


windows instructions can be found here 
https://desertbot.io/blog/headless-pi-zero-w-wifi-setup-windows

For ubuntu, on the host PC,after flashing the image, cd to the boot partition (/media/<<username>>/boot) and
run `touch ssh`
run `nano wpa_supplicant.conf`
change contents to this
```
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
  ssid="RBE"
  psk="<<youshouldknowthis>>"
}
```
save, eject, insert SD card into pi.


Insert the card into the pi.
The LCD display should be on and white. After 2 minutes you should be able to SSH in.

SSH into `fi-rasp-temp-22.dyn.wpi.edu` with the username pi and the password raspberry
run `sudo raspi-config`
navigate to (1) System Options -> (S3) Password.
select a new root password.
navigate to (1) System Options -> (S7) Splash Screen.
Set it to Yes, splash screen on boot.

### Setting up NTP and dependancies
run `sudo nano /etc/systemd/timesyncd.conf` to edit the file
navigate to a line that begins with `#FallbackNTP=`
under it type
`FallbackNTP=ntp1.wpi.edu`
save the file by htting ctrl-x and then y and then enter
run `sudo timedatectl set-timezone America/New_York`
run `sudo timedatectl set-ntp true`
reboot the pi by running `sudo reboot`

log back in and make sure time and date is correct by rinning `date`
then, run `sudo apt-get update` and finally `sudo apt-get install git`
  
### Setting up auto-launch of Python testing app.
run `sudo apt-get install --no-install-recommends xserver-xorg x11-xserver-utils xinit openbox`
run `sudo apt-get install libgtk-3-dev`
run `sudo apt install python3-gi gobject-introspection gir1.2-gtk-3.0`
edit `sudo nano /etc/xdg/openbox/autostart`
add the following to the bottom
```
xset -dpms            # turn off display power management system
xset s noblank        # turn off screen blanking
xset s off            # turn off screen saver
/home/pi/dynatestjig/launch.sh
```

clone the script
`cd ~/`
`git clone https://github.com/acamilo/dynatestjig.git`
  run `cd ~/dynatestjig/` and run `chmod a+x launch.sh ui.py `
run `touch ~/.bash_profile`
edit `sudo nano ~/.bash_profile`

add the following line and save
`[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && startx -- -nocursor`

run `sudo raspi-config`
Select (1) System Options (S5) Boot / Auto Login (B2) Console Autologin
Finish and reboot.

  

### Setting up the LCD Display

run `sudo apt-get update`
run `sudo apt-get install cmake`

run `git clone https://github.com/goodtft/LCD-show.git`
run `chmod -R 755 LCD-show`
run `cd LCD-show/`
run `sudo ./LCD35-show`

the pi should reboot and after a few min you should see stuff on the LCD.

SSH back into the pi and run the following commands
run `cd LCD-show/`
run `sudo ./LCD35-show 90`

The PI will reboot again and the display will be correctly oriented.

Note: instructions come from http://www.lcdwiki.com/3.5inch_RPi_Display




