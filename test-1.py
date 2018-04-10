#!/usr/bin/env python

from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(800, 600))
display.start()

url = 'http://www.ilmuonedata.com/about/'

print 'THIS IS TEST UMAR (browsing with chrome), ', url
try:
  browser = webdriver.Chrome()
  browser.get(url)
  print browser.title
  test_text = browser.find_element_by_css_selector('#block-0497bd540a1b86052db6 > div > h2 > em')
  print test_text.text
  browser.quit()
except Exception as e:
  print e

display.stop()
