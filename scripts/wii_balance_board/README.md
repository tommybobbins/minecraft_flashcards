Use xwiimote and Minecraft API to steer Steve with a balance board:

Install the prerequisite packages:

    $ sudo apt-get install bluez bluez-tools bluez-utils obex-data-server
    $ sudo apt-get install libtool libudev-dev libudev-dev libncurses5-dev
    $ sudo apt-get install autoconf jstest-gtk

Build: 

    $ git clone "https://github.com/dvdhrm/xwiimote"
    $ cd xwiimote
    $ ./autogen.sh 
    $ make
    $ sudo make install
    $ sudo cp res/50-xorg-fix-xwiimote.conf /usr/share/X11/xorg.conf.d
    $ sudo cp 70-udev-xwiimote.rules /etc/udev/rules.d/
    $ sudo reboot


Using blueman and the little red button underneath the balance board, pair the board. Ensure that the key and the star are ticked in blueman.
Inside xwiimote is a useful utility called xwiishow. Make sure that the LXTerminal is full screen before running.
jstest-gtk is another utility to test the axes of the balance board are being detected.

