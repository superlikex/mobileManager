#!/usr/bin/env python
# -*- coding: utf-8 -*-

# *************************************************************
# Filename @ get_app.py
# Author @ Likex
# Create date @ 2016-01-05 17:14:04
# Description @ 
# *************************************************************



# Script starts from here

import os
import subprocess

print "Content-type: text/html\r\n\r\n";

cmd_getPackages = 'adb shell pm list package'
packages 	= subprocess.check_output(cmd_getPackages.split('\r\n'))

