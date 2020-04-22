
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
driver = webdriver.Chrome()
time.sleep(5)
# 打开一个网址
driver.get("http://www.baidu.com")
# 设置一个窗口大小
driver.set_window_size(1440,900)

driver.find_element_by_id("kw").send_keys("学神IT教育")
driver.find_element_by_id("su").click()

locator = (By.XPATH,'//a[text()="_腾讯课堂"]')
WebDriverWait(driver,30).until(EC.visibility_of_element_located(locator))
# 获取一下窗口数量
handles = driver.window_handles   # 1个
# 打开新的窗口  带来了一个新窗口的出现  2个窗口
driver.find_element(*locator).click()
# 确认新窗口真的出现了    然后再去获取窗口句柄   自己会再获取一次窗口数量 2个
WebDriverWait(driver,20).until(EC.new_window_is_opened(handles))  # 2 > 1
# 再次获取窗口的handles   获取了两个窗口的句柄
handles = driver.window_handles
print(handles)
#切换窗口
driver.switch_to.window(handles[-1])# 传入一个句柄

locator = (By.XPATH,'//section[@class="section-main"]//h2[text()="课程(99)"]')
WebDriverWait(driver,30).until(EC.visibility_of_element_located(locator))
driver.find_element(*locator).click()


