#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# *************************************************************
# Filename @ test1.py
# Author @ Likex
# Create date @ 2016-01-05 10:00:12
# Description @ 
# *************************************************************



# Script starts from here

import subprocess

cmd = 'adb -d devices'
s = subprocess.check_output(cmd.split())
print s.split('\r\n')
cmd_getBrandName = 'adb -d shell getprop ro.product.brand'
cmd_getModel = 'adb -d shell getprop ro.product.model'
cmd_getBuildRelease = 'adb -d shell getprop ro.build.version.release'
cmd_getIMEI = 'adb -d shell dumpsys iphonesubinfo'
cmd_getMAC = 'adb -d shell cat /sys/class/net/wlan0/address'
brandName 	= subprocess.check_output(cmd_getBrandName.split())
model 		= subprocess.check_output(cmd_getModel.split())
buildRelease = subprocess.check_output(cmd_getBuildRelease.split())
IMEI		= subprocess.check_output(cmd_getIMEI.split())
MAC			= subprocess.check_output(cmd_getMAC.split())

print brandName.split('\r\n')
print model.split('\r\n')
print buildRelease.split('\r\n')
print IMEI.split('\r\n')
print MAC.split('\r\n')

