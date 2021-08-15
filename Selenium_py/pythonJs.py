from selenium import webdriver
import time
import pyautogui
from ctypes import windll
import win32gui,win32con
import win32api
from  win32api  import  GetSystemMetrics
import webbrowser
import execjs



from winreg import HKEY_CURRENT_USER, OpenKey, QueryValueEx

webbrowser.register("chrome",None,webbrowser.GenericBrowser(u"C:\\ProgramFiles(x86)\\Google\\Chrome\\Application\\chrome.exe"))
chromePath = r'C:\\ProgramFiles(x86)\\Google\\Chrome\\Application\\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
#这里的'chrome'可以用其它任意名字，如testB，这里将想打开的浏览器保存到'chrome'
#webbrowser.get('chrome').open('www.baidu.com',new=1,autoraise=True)
webbrowser.open('www.baidu.com',new=2,autoraise=False)

# 调用js文件
def get_js():  
    # f = open("D:/WorkSpace/MyWorkSpace/jsdemo/js/des_rsa.js",'r',encoding='UTF-8')  
    f = open("./chromeVer.js", 'r', encoding='UTF-8')  
    line = f.readline()  
    htmlstr = ''  
    while line:  
        htmlstr = htmlstr + line  
        line = f.readline()  
    return htmlstr  
   
jsstr = get_js()  
ctx = execjs.compile(jsstr)  
print(ctx.call('getChromeVersion',''))
