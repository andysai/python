from gevent import monkey
monkey.patch_all()
from selenium import webdriver
from bs4 import BeautifulSoup
import time
driver = webdriver.Chrome()
driver.get('http://www.mtime.com/top/tv/top100/')
time.sleep(2)
list = driver.find_element_by_class_name('top_list').text
print(list)
driver.close()