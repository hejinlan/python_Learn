# coding=utf-8

import os
from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
import time
driver=webdriver.Chrome('F:\05.Python\chromeDriver\chromedriver.exe')
driver.get("http://www.baidu.com")
driver.maximize_window()
time.sleep(10)
to_element =  driver.find_element_by_xpath('//*[contains(text(),"百度热搜")]' )
ActionChains(driver).move_to_element_with_offset(to_element, 200, 300).context_click().perform()
ActionChains(driver).move_by_offset(x=1150, y=769).click_and_hold().perform() # 鼠标左键点击， 200为x坐标， 100为y坐标
ActionChains(driver).move_by_offset(x=1150, y=769).context_click().perform() # 鼠标右键点击
