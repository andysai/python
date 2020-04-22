
# selenium安装  pip install selenium
from selenium import webdriver
import time

# 开启一个会话
driver = webdriver.Chrome()
time.sleep(5)
# 打开一个网址
driver.get("http://www.baidu.com")
# 设置一个窗口大小
driver.set_window_size(1440,900)
print("打开课堂派网页之前:",driver.current_window_handle)

driver.get("https://www.ketangpai.com")
# 获取当前窗口的句柄
print("打开课堂派网页之后:",driver.current_window_handle)
time.sleep(2)
# 后退
driver.back()
print("回到百度网页之后:",driver.current_window_handle)
# 前进
time.sleep(2)
driver.forward()

# 关闭浏览器
# driver.close()  关闭当前活跃的窗口
# driver.quite()  1、关闭一个chromedriver.exe进程   2、关闭浏览器  3、恢复数据环境








