DEPENDENCY:
-----------

sudo apt-get install python3-pil.imagetk


AUTOSTART:
----------

sudo nano /etc/xdg/lxsession/LXDE/autostart
Add
@/usr/bin/python3 /home/pi/pibooth/pibooth.py &

