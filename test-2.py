#!/usr/bin/env python

from pyvirtualdisplay import Display
from selenium import webdriver
import datetime
import json

display = Display(visible=0, size=(800, 600))
display.start()

url = 'http://www.detik.com/'

print('THIS IS TEST UMAR (browsing with chrome) for:', url)
print()

driver = webdriver.Chrome()
driver.get(url)

### result ###
result = []

limitation = driver.find_element_by_tag_name('body')
limitation = limitation.find_element_by_class_name('container')
limitation = limitation.find_element_by_class_name('content')
limitation = limitation.find_element_by_class_name('m_content')
limitation = limitation.find_element_by_id('newsfeed-container')
limitation = limitation.find_elements_by_tag_name('article')

for idx in range(len(limitation)):
    try:
        ### Temporary Result ###
        dict_data = {}
        
        a = limitation[idx].find_element_by_class_name('desc_nhl')
        a = a.find_element_by_tag_name('a')
        
        print(a.text)
        
        ### Title ###
        dict_data.update({'title':a.text})
        
        ### Link ###
        dict_data.update({'title':a.get_attribute('href')})
        
        ### Store the data ###
        result.append(dict_data)
    except:
        pass

file_name = 'detik - '+str(datetime.datetime.now().year)+str(datetime.datetime.now().month)+str(datetime.datetime.now().date)
with open('~/gcloud-test-1/'+file_name+'.txt', 'w') as outfile:
    json.dump(result, outfile)

display.stop()
