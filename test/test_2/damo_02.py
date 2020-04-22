
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
driver = webdriver.Chrome()

# 设置全局等待时间(隐形等待)
driver.implicitly_wait(30)

driver.get("http://www.baidu.com")
time.sleep(10)
driver.find_element_by_xpath('//div[@id="u1"]/a[@name="tj_login"]').click()

# 显性等待  等待+条件
# WebDriverWait类     WebDriverWait(driver,等待时长,轮询周期).until(条件)/until_not()
locator = (By.ID,"TANGRAM__PSP_10__footerULoginBtn")
WebDriverWait(driver,30).until(EC.visibility_of_element_located(locator))
driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
# driver.find_element(*locator).click()

# 元素存在
# 元素可见
# 元素可用
