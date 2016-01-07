#!/usr/bin/env python
# -*- coding: utf-8 -*-

# *************************************************************
# Filename @ sqltest.py
# Author @ Likex
# Create date @ 2016-01-06 14:07:27
# Description @ 
# *************************************************************



# Script starts from here

import sqlite3
conn = sqlite3.connect('App.db')
conn.execute("insert into app(id) values(10)");
conn.commit()
conn.close()

