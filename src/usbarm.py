#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Nathan Bookham
#
# USBArm is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Start of usbarm.py

'''
A Python module that allows control of a USB arm with a Unix PC.
PyUSB must be installed for this module to work.
To initialise a connection to the arm, use the command 'usbarm.connect()'.
To send instructions to the arm, use the command 'usbarm.ctrl(duration, command)'.
The duration sets how long the command runs for, and the command tells the arm what to do.
'''

# Define commands to control arm
rotate_ccw = [0,1,0] # Rotate base counter-clockwise
rotate_cw = [0,2,0] # Rotate base clockwise
shoulder_up = [64,0,0] # Shoulder up
shoulder_down = [128,0,0] # Shoulder down
elbow_up = [16,0,0] # Elbow up
elbow_down = [32,0,0] # Elbow down
wrist_up = [4,0,0] # Wrist up
wrist_down = [8,0,0] # Wrist down
grip_open = [2,0,0] # Open grip
grip_close = [1,0,0] # Close grip
light_on = [0,0,1] # Light on

# Define a procedure to connect to the arm via USB
def connect():
    '''
    Connect to the USB arm.
    '''
    global usb_arm
    # Attempt to import the USB, Paralel processing and time libraries into Python
    try:
        from time import sleep
    except:
        raise Exception("Time library not found")
    try:
        import usb.core, usb.util
    except:
        raise Exception("USB library not found")
    try:
        import multiprocessing
    except:
        raise Exception("Paralel processing library not found")
    usb_arm = usb.core.find(idVendor=0x1267, idProduct=0x000)
    # Check if the arm is detected and warn if not
    if usb_arm == None:
        raise Exception("Robotic arm not found")
    else:
        return True

# Define a procedure to create processes to enable paralel commands
def ctrl(duration, command):
    '''
    Creates processes to control arm
    '''
    # Define a command queue
    queue = []
    # Define a process to pass commands to ctrl_worker
    process = multiprocessing.Process(target=ctrl_worker, args=(duration, command,))
    # Add command to the queue
    queue.append(process)
    # Start process using items in the queue
    process.start()

# Define a procedure to transfer commands via USB to the arm
def ctrl_worker(duration, command):
    '''
    Handles command transmission over USB
    '''
    if usb_arm == None:
        raise Exception("Robotic arm not connected")
    # Start the movement
    usb_arm.ctrl_transfer(0x40,6,0x100,0,command,1000)
    # Stop the movement after waiting a specified duration
    sleep(duration)
    usb_arm.ctrl_transfer(0x40,6,0x100,0,[0,0,0],1000)
    return True

if __name__ == "__main__":
	# Show GNU copyright notice
	print "USBArm Copyright (C) 2013 Nathan Bookham"
	print "This program comes with ABSOLUTELY NO WARRANTY."
	print "This is free software, and you are welcome to redistribute it under certain conditions."
	
    raise Exception("Cannot run standalone - use 'import usbarm' to utilise this module")
    exit()

# End of usbarm.py
