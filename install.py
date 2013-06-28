# USBArm Instaler by Nathan Bookham

from subprocess import call
from time import sleep
import urllib2

def check_internet_connection():
    try:
        response=urllib2.urlopen('http://github.com',timeout=15)
        return True
    except urllib2.URLError as err: pass
    return False

print "USBArm Dependancy Installer"
sleep(1)

print ""
print "Checking internet connection..."
connection_active = check_internet_connection()
if connection_active == False:
    print "Connection failed! Check your connection and proxy setings."
    exit()
elif connection_active == True:
    print "Connection is active!"

print ""
print "Getting latest package lists... (This may take a while)"
call (["sudo apt-get update"], shell=True)
print "Package lists retrived!"

print ""
print "Updating packages... (This may take a while)"
call (["sudo apt-get -y upgrade"])
print "Packages updated!"

print ""
print "Installing dependencies..."
call (["sudo apt-get -y install wget libusb-1.0-0 python-setuptools"])
call (["sudo easy_install pyusb"])
print "Dependencies installed!"

print ""
print "Downloading USBArm module..."
call (["wget -O /tmp/usbarm.py.tmp https://raw.github.com/inversesandwich/USBArm/master/usbarm.py"])
print "Module downloaded!"

print ""
print "Preparing module..."
call (["mv /tmp/usbarm.py.tmp ~/usbarm.py"])
print "Preparation complete!"

print ""
print "The USBArm module is stored in your home directory."
print "See the readme on GitHub at http://github.com/inversesandwich/USBArm for information on usage."
raw_input("Press enter to close...")
