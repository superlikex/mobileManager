#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import urllib
import re
import os
import subprocess
import time
import sqlite3
# *************************************************************
# Filename @ get_app_info.py
# Author @ Likex
# Create date @ 2016-01-06 11:11:50
# Description @ 
# *************************************************************
def get_package_list_3():
	cmd_getPackages_3 	= 'adb shell pm list package -3'
	packages			= subprocess.check_output(cmd_getPackages_3.split())
	packageList			= packages.split('\r\n')
	packageName 		= [ x.split(':')[1] for x in packageList[1:-1]]
	return packageName

class GET_APP_INFO:
	def __init__(self):
		self.conn = sqlite3.connect('./App.db')
		self.conn.text_factory = str
		self.url = 'http://www.coolapk.com/apk/'
		self.header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML,     like Gecko) Chrome/30.0.1599.101 Safari/537.36' }
		
	def open_page(self,packages):
		s = requests.session()
		for packageName in packages:
			response = s.get(self.url+packageName)
			if response.status_code == 200:
#				print response.content
				self.get_app_online(response.content,packageName)
			else:
				print packageName
		self.conn.close()	
	def get_app_online(self,page,packageName):
		pattern 		= re.compile('<h1 class="media-heading ex-apk-view-title">(.*?)<small>(.*?)</small></h1>',re.S)
		pattern_icon 	= re.compile('<img class="media-object img-rounded" src=(.*?) alt=(.*?)>')
		
		result 			= re.search(pattern,page)
		result_icon 	= re.search(pattern_icon,page)

		app_name		= result.group(1)		
		url_icon 		= result_icon.group(1)
		app_name 		= result_icon.group(2)
		icon_pos		= self.get_app_icon(packageName,url_icon.split("\"")[1])

		cursor = self.conn.cursor()
#		insert_cmd = 'insert into app(id) values (2)'
		cursor.execute('insert into app(package_name,app_name,app_icon_pos) values(?,?,?)', \
										(packageName,app_name,icon_pos));
		self.conn.commit()	
		cursor.close()
#		if result_icon:
#			print result_icon.group(2)
#			return result.group(1)
#		else:
#			return None

	def get_app_icon(self,packageName,url):
		pic	= urllib.urlopen(url).read()
#		pic = urllib.urlopen("http://image.coolapk.com/apk_logo/2015/0610/408649_1433917819_6148.png").read()
		file_name 	= 'icon/%s.png'%packageName
		f 	= file(file_name,"wb")
		f.write(pic)
		f.close()
		return file_name
		
packages	= get_package_list_3()
a 			= GET_APP_INFO()
a.open_page(packages)
