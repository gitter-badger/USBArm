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

# Start of setup.py

from distutils.core import setup

setup(name='USBArm',
      version='1.0',
      maintainer='InverseSandwich',
      url='http://github.com/inversesandwich/USBArm',
      description = ("A simple to use Python module for controlling USB robotic arm devices on Linux PCs, including the Raspberry Pi."),
      license = "Public Domain",
      package_dir={'usbarm': 'src'},
      packages=['usbarm'],
      install_requires=['pyusb'],
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Operating System :: POSIX :: Linux",
    	],
     )

# End of setup.py
