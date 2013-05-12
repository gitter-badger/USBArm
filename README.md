USB Robotic Arm Control Python Module
===============================================

A simple to use Python module for controlling USB robotic arm devices on Unix PCs, including the Raspberry Pi.

Robotic Arm Compatibility
-------------------------
![ArmPicture](http://img211.imageshack.us/img211/7640/a37jnhighres.jpg)

The only model currently compatible is the Velleman KSR10 with USB inteface board. In the UK it is sold exclusivly at Maplin. If it looks like the arm in the image above, it should work.

How to use
----------
First of all, we need to make sure that PyUSB is installed. You can download PyUSB from [Sourceforge](http://sourceforge.net/projects/pyusb/files/latest/download?source=directory). Once extracted just run `sudo python setup.py install` in the pyusb directory to install PyUSB. You'll need to install libusb for it to work. Just use your distriutions package manager such as apt, yum, rpm, etc.

We now need to download the module. In unix, use `wget https://raw.github.com/inversesandwich/USBArm/master/usbarm.py` to download the latest version.
Then create a Python script using your favorite text editor/IDE in the same folder as the script you just downloaded. Then use the following commands to import the module and connect to a robotic arm.
    
    import usbarm
    usbarm.connect()
    
It's as simple as that! Now we need to tell the arm what to do. To send a command, we use the following code:

    usbarm.ctrl(duration, command)
    
'command' tells which part of the arm to move, and 'duration' is how long the command runs for. The duration can either be an interger or a float.

The commands that you can use are;
* usbarm.rotate_ccw
* usbarm.rotate_cw
* usbarm.shoulder_up
* usbarm.shoulder_down
* usbarm.elbow_up
* usbarm.elbow_down
* usbarm.wrist_up
* usbarm.wrist_down
* usbarm.grip_open
* usbarm.grip_close
* usbarm.light_on
