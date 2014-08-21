Use PS3 controller to steer Steve

Install the prerequisite packages:

     $ sudo apt-get install xserver-xorg-input-joystick
     $ git clone "https://github.com/tommybobbins/PS3-SixAxis-RaspberryPi"     
     $ sudo cp PS3-SixAxis-RaspberryPi/50-joystick.conf /usr/share/X11/xorg.conf.d/

