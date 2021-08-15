# coding=utf-8

from selenium import webdriver
import time
import pyautogui
from ctypes import windll
import win32gui,win32con
import win32api
from  win32api  import  GetSystemMetrics
import webbrowser



from winreg import HKEY_CURRENT_USER, OpenKey, QueryValueEx

webbrowser.register("chrome",None,webbrowser.GenericBrowser(u"C:\\ProgramFiles(x86)\\Google\\Chrome\\Application\\chrome.exe"))
chromePath = r'C:\\ProgramFiles(x86)\\Google\\Chrome\\Application\\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
#这里的'chrome'可以用其它任意名字，如testB，这里将想打开的浏览器保存到'chrome'
webbrowser.get('chrome').open('www.baidu.com',new=0,autoraise=True)

"""
reg_path = r'Software\Microsoft\Windows\Shell\Associations\UrlAssociations\https\UserChoice'

with OpenKey(HKEY_CURRENT_USER, reg_path) as key:
    print(QueryValueEx(key, 'ProgId'))

from tkinter import *
import webbrowser

root = Tk()

text = Text(root,width=30,height = 5)
text.pack()

text.insert(INSERT, "百度一下，你就知道")

text.tag_add("link","1.0","1.4")
text.tag_config("link", foreground="blue", underline = True)

def click(event):
    webbrowser.open("http://www.baidu.com")

text.tag_bind("link","<Button-1>",click)

mainloop()    

  
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
time.sleep(8)
pyautogui.mouseDown(x=1, y=1, button='left')
pyautogui.moveTo(x=1500, y=1, duration=2, tween=pyautogui.easeInOutQuad)
time.sleep(5)
pyautogui.mouseUp(x=1500, y=1, button='left')



#########百度输入框的定位方式##########
#通过id方式定位
browser.find_element_by_id("kw").send_keys("selenium")
#通过name方式定位
browser.find_element_by_name("wd").send_keys("selenium")
#通过tag name方式定位
browser.find_element_by_tag_name("input").send_keys("selenium")
#通过class name方式定位
browser.find_element_by_class_name("s_ipt").send_keys("selenium")
#通过CSS方式定位
browser.find_element_by_css_selector("#kw").send_keys("selenium")
#通过xpath方式定位
browser.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")
############################################
browser.find_element_by_id("su").click()
time.sleep(3)
browser.quit()


time.sleep(1)
print(driver.capabilities['version'])

import os
from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Chrome()
 
driver.get("http://www.baidu.com")
 
time.sleep(1)
 
#获取浏览器版本号
try:
    print('获取浏览器版本号:',driver.capabilities['version'])
except KeyError:
    print('未获取到浏览器版本号???')
 
#获取网页尺寸
print('获取网页尺寸:',driver.get_window_size())
 
#获取当前url
print('获取当前url:',driver.current_url)
 
#获取当前页面标题
print('获取当前页面标题:',driver.title)

str1 = driver.capabilities['browserVersion']
str2 = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
print(str1)
print(str2)
print(str1[0:2])
print(str2[0:2])
if str1[0:2] != str2[0:2]: 
  print("please download correct chromedriver version")
def mkdir(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)

    if not isExists:
        os.makedirs(path) 
        print(path+' 创建成功')
        return True
    else:
        print( path+' 目录已存在')
        return False
 
mkpath="d:\\Chrome\\webdriver\\"
mkdir(mkpath)

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'h:\\'}
options.add_experimental_option('prefs', prefs)
 
driver = webdriver.Chrome(executable_path='D:\Chrome\webdriver\chromedriver.exe', options=options)
driver.get("https://npm.taobao.org/mirrors/chromedriver")
driver.find_element_by_xpath('//*[contains(text(),"92.0.4515.107")]' ).click()
#driver.find_element_by_xpath("//a[contains@href,'92.0.4515.107']").click()
time.sleep(5)
 
#选择下载文件
driver.find_element_by_xpath("//a[contains(@href,'chromedriver_win32.zip')]").click()
time.sleep(30)
 
driver.quit()
"""
