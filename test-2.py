from pyvirtualdisplay import Display
from selenium import webdriver
import pandas as pd
import datetime

display = Display(visible=0, size=(800, 600))
display.start()

url = 'http://www.detik.com/'

print 'THIS IS TEST UMAR (browsing with chrome), ', url

driver = webdriver.Chrome()

### result ###
result = []

limitation = driver.find_element_by_id('newsfeed-container')
limitation = limitation.find_elements_by_tag_name('article')

for idx in range(len(limitation)):
    ### Temporary Result ###
    dict_data = {}

    a = limitation[idx].find_element_by_class_name('desc_nhl')
    a = a.find_element_by_tag_name('a')
    
    ### for printing ###
    print a.text
    
    ### Title ###
    dict_data.update({'title':a.text})
    
    ### Link ###
    dict_data.update({'title':a.get_attribute('href')})
    
    ### Store the data ###
    result.append(dict_data)
    
result = pd.DataFrame(result)


file_name = 'detik - '+datetime.datetime.now().year+datetime.datetime.now().month+datetime.datetime.now().date
writer = pd.ExcelWriter('~/gcloud-test-1/dataset/'+file_name+'.xlsx')
result.to_excel(writer,'Sheet1')
writer.save()

display.stop()
