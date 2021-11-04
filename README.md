# dynatestjig
## Image Setup Instructions
### Set up a fresh SD Card
The image used is the light version of raspbian, Without a GUI.
https://downloads.raspberrypi.org/raspios_lite_armhf/images/raspios_lite_armhf-2021-05-28/2021-05-07-raspios-buster-armhf-lite.zip
Download, extract, flash with balena etcher onto a SD card.

Follow this guide to set up wireless and SSH. You need to add 2 files to the BOOT drive that shows up after the flashing is done.
https://desertbot.io/blog/headless-pi-zero-w-wifi-setup-windows

Insert the card into the pi.
The LCD display should be on and white. After 2 minutes you should be able to SSH in.

SSH into `fi-rasp-temp-22.dyn.wpi.edu` with the username pi and the password raspberry
run `sudo raspi-config`
navigate to (1) System Options -> (S3) Password.
select a new root password.
navigate to (1) System Options -> (S7) Splash Screen.
Set it to Yes, splash screen on boot.

### Setting up NTP
run `sudo nano /etc/systemd/timesyncd.conf` to edit the file
navigate to a line that begins with `#FallbackNTP=`
under it type
`FallbackNTP=ntp1.wpi.edu`
save the file by htting ctrl-x and then y and then enter
run `sudo timedatectl set-timezone America/New_York`
run `sudo timedatectl set-ntp true`
reboot the pi by running `sudo reboot`

log back in and make sure time and date is correct by rinning `date`


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

### Setting up auto-launch of Python testing app.

run `sudo raspi-config`
Select (1) System Options (S5) Boot / Auto Login (B2) Console Autologin
Finish and reboot.
run `sudo ./LCD35-show 90` and let pi reboot
run `sudo apt-get install --no-install-recommends xserver-xorg x11-xserver-utils xinit openbox`
edit `sudo nano /etc/xdg/openbox/autostart`
add the following to the bottom
```
xset -dpms            # turn off display power management system
xset s noblank        # turn off screen blanking
xset s off            # turn off screen saver
```





