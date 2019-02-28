#!/usr/bin/env python
## -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re  
import subprocess
from subprocess import Popen, PIPE, call
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)
url_list = []
url_list.append("https://ru.betsapi.com/live/basketball")



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
    				subprocess.check_call([r"/home/ruzal/test.sh"])

driver.close();

