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

