#!/usr/bin/env python
## -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from subprocess import Popen, PIPE, call
from selenium.webdriver.firefox.options import Options
import re  
import subprocess
import os


options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)
url_list = []
url_list.append("https://ru.betsapi.com/live/basketball")
url_target_list = []


while (url_list):
	driver.get(url_list[0])
	match = driver.find_elements_by_xpath("*//i[contains(@class,'fa fa-play-circle float-right')]/following::a[1]")
	options = [x for x in match]
	for element in options:
		url_list.append(element.get_attribute("href"))

	print(url_list)
	print(len(url_list))


	url_list_save = url_list
	url_list = None

for i in url_list_save:
			print(i)
			driver.get(i)
			element = driver.find_element_by_xpath("*//table[contains(@class,'table table-sm')]/tbody/tr[6]")
			src = element.text

			# if found anything exept 0,1,2,3 - get alert
			found = re.search('(0|1|2|3)',src)
			found = bool(found)
			found = not found
			print(found)

			if (bool(found)):
    				url_target_list.append(i)


# check if url_target_list[0] == url_target_list_old[0] then delete url_target_list[0], url_target_list_old[0]

if os.path.exists('url_target_list.txt'):
	f = open('url_target_list.txt')
	url_target_list_old = f.read()
	f.seek(0)
	url_target_list_old = url_target_list_old.split(',')
	end = len(url_target_list)
	for el in range(end):
		if (url_target_list_old[el] != url_target_list[el]):
			print url_target_list[el]
else:
	url_target_list_old = url_target_list



# save url_target_list for compare in next run

if os.path.exists('url_target_list.txt'):
	f = open('url_target_list.txt','r+')
	f.truncate(0) # need 0 when using r+ ; for clear content when file was opened
else:
	f = open('url_target_list.txt','w')

url_target_list_str = ','.join(url_target_list)

f.write(url_target_list_str)

driver.close();


#url_target_str = ','.join(url_target_list)

#subprocess.check_call([r"/home/ruzal/test.sh"])

