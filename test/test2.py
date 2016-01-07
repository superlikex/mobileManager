#!/usr/bin/env python
# -*- coding: utf-8 -*-

# *************************************************************
# Filename @ test2.py
# Author @ Likex
# Create date @ 2016-01-05 14:35:02
# Description @ 
# *************************************************************



# Script starts from here

import subprocess
COMMOND1 = "aapt dump badging "
COMMOND2 = " | grep application-label-zh-CN:"
def get_apk_name(commond):
    p = subprocess.Popen(commond, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           stdin=subprocess.PIPE,shell=True)
    (output, err) = p.communicate()
    if output != "":
        try:
            result = output[19:-2]
            return result
        except Exception,e:
            return ""
    return ""
apk_path = "./Apps/base.apk"
commond = COMMOND1+apk_path+COMMOND2
get_apk_name(commond)
