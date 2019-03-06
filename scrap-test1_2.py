#!/usr/bin/env python
## -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from subprocess import Popen, PIPE, call
from selenium.webdriver.firefox.options import Options
import re  
import subprocess
import os
import time

# module for include browser-specific webdriver

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)
url_list = []
url_list.append("https://ru.betsapi.com/live/basketball")
url_target_list = []
url_target_list_final = []

#end

#module for run by match pages in betsapi.com

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
			try:
				element = driver.find_element_by_xpath("*//table[contains(@class,'table table-sm')]/tbody/tr[6]")
				if (element):
					src = element.text

					# if found anything exept 0,1,2,3 - get alert
					found = re.search('(0|1|2|3)',src)
					found = bool(found)
					found = not found
					print(found)

					if (bool(found)):
							url_target_list.append(i)
			except BaseException:
				print('There are match without statistics')

#end

#module for save and read previous matches and remove duplicate matches,for alert only new matches
#
if os.path.exists('url_target_list.txt'):
	f = open('url_target_list.txt')
	url_target_list_old = f.read()
	f.seek(0) # clear file
	url_target_list_old = url_target_list_old.split(',') # convert str to list
else:
	url_target_list_old = []
	url_target_list_old.append('addition') #if file does not exist
	f = open('url_target_list.txt','w')
	f.write('addition')


##this for exit from out of range

len_url = len(url_target_list)
len_url_old = len(url_target_list_old)
end = len_url + len_url_old
for i in range(len_url_old,end):
	url_target_list_old.append('addition') # add items to url_target_list_old for exit from case when len(url_target_list_old) < len(url_target_list)

## print final result - new target matches
	
end = len(url_target_list)
for el in range(end):
	if (url_target_list[el] != url_target_list_old[el]): # because in betsapi.com live matches in order and when order changes also our list changes and got alert
		url_target_list_final.append(url_target_list[el])  

# save url_target_list for compare in next run

if os.path.exists('url_target_list.txt'):
	f = open('url_target_list.txt','r+')
	f.truncate(0) # need 0 when using r+ ; for clear content when file was opened
	url_target_list_str = ','.join(url_target_list) #convert list to str
	f.write(url_target_list_str)
else:
	f = open('url_target_list.txt','w')
	f.write('addition')

#end
driver.quit()
#module for get alert

## disable headless mode

driver = webdriver.Firefox()
print url_target_list_final
if (len(url_target_list_final)!=0):
	subprocess.check_call([r"/home/ruzal/test.sh"])

end = len(url_target_list_final)
for i in range(0,end):
	print url_target_list_final[i]
	driver.get(url_target_list_final[i])
	time.sleep(20)

driver.quit()
#end


#exit


#other
#url_target_str = ','.join(url_target_list)

#subprocess.check_call([r"/home/ruzal/test.sh"])

