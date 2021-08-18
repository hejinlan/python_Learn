pip install pypiwin32

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
time.sleep(8)
# 拖拽移动网页到副屏
pyautogui.mouseDown(x=1, y=1, button='left')
pyautogui.moveTo(x=1500, y=1, duration=2, tween=pyautogui.easeInOutQuad)
time.sleep(5)
pyautogui.mouseUp(x=1500, y=1, button='left')

#
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

# 获取当前屏幕分辨率
screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)


# -*- coding: utf-8 -*-
"""
功能：识别两块显示器各自的分辨率
"""
"""模块导入"""  ClipCursor
from win32api import GetSystemMetrics
from win32con import SM_CMONITORS, SM_CXVIRTUALSCREEN, SM_CYVIRTUALSCREEN

# 进入消息循环
win.mainloop()
def Display_Detection():
    # 显示器数量检测
    MonitorNumber = GetSystemMetrics(SM_CMONITORS)
    # 主屏幕尺寸检测
    MajorScreenWidth = GetSystemMetrics(0)  # 主屏幕宽
    MajorScreenHeight = GetSystemMetrics(1)  # 主屏幕高
    # print("主屏幕尺寸：", GetSystemMetrics(0), "*", GetSystemMetrics(1))
    # 屏幕最大尺寸
    aScreenWidth = GetSystemMetrics(SM_CXVIRTUALSCREEN)  # 屏幕最大宽度
    aScreenHeight = GetSystemMetrics(SM_CYVIRTUALSCREEN)  # 屏幕最大高度
    AllScreen=(aScreenWidth, aScreenHeight)
    # print("屏幕总尺寸:", aScreenWidth, "*", aScreenHeight)
    # 当前主流的分辨率基数是宽，偶数是高
    ResolvingPower = [1280, 720, 1920, 1080, 2560, 1440, 3840, 2160, 4096, 2160, 7680, 4320]
    if MonitorNumber > 1:  # 屏幕数量判断print(MonitorNumber)就可以知道有多少块屏幕
        SecondaryScreenWidth = aScreenWidth - MajorScreenWidth  # 副屏宽=总屏幕宽-当前屏幕宽
        # print("副屏宽",SecondaryScreenWidth)
        # 主屏横竖屏检测
        if GetSystemMetrics(0) > GetSystemMetrics(1):
            MianScreen = (GetSystemMetrics(0), GetSystemMetrics(1))
            print("主屏(横屏)尺寸：", GetSystemMetrics(0), "*", GetSystemMetrics(1))
        else:
            MianScreen = (GetSystemMetrics(0), GetSystemMetrics(1))
            print("主屏(竖屏)尺寸：", GetSystemMetrics(0), "*", GetSystemMetrics(1))
        # 横屏状态
        for i in range(0, len(ResolvingPower) - 1, 2):
            # print("i",ResolvingPower[i])
            if SecondaryScreenWidth == ResolvingPower[i]:
                SecondaryScreen = (ResolvingPower[i], ResolvingPower[i + 1])
                print("副屏(横屏)尺寸：", ResolvingPower[i], ResolvingPower[i + 1])
                #return "副屏(竖屏)尺寸：",SecondaryScreen
                break
        # 竖屏状态
        for i in range(1, len(ResolvingPower) - 1, 2):
            print("i",ResolvingPower[i])
            if SecondaryScreenWidth == ResolvingPower[i]:
                SecondaryScreen = (ResolvingPower[i], ResolvingPower[i + 1])
                print("副屏(竖屏)尺寸：", ResolvingPower[i], ResolvingPower[i - 1])
                # return "副屏(竖屏)尺寸",SecondaryScreen
                break
    return MonitorNumber,AllScreen,MianScreen,SecondaryScreen
#调用
a=Display_Detection()
print(a)#a可以任意遍历其中的内容a[0]代表屏幕数量等等...
#(2, (4480, 1440), (2560, 1440), (1920, 1080))#运行结果：屏幕数量、总屏幕尺寸、主屏幕尺寸、副屏尺寸
"""
import os
import time
#import  wx
from ctypes import windll
import win32gui,win32con
import win32api
from  win32api  import  GetSystemMetrics

from logprint import errorMsg
print("sdfasdf")
print(win32api.GetCursorPos())
#win32api.MessageBox(0,"Hello PYwin32","MessageBox",win32con.MB_OK | win32con.MB_ICONWARNING)
windll.user32.SetCursorPos(1152, 770)  # 点击当前坐标
time.sleep(2)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 1156, 766, 0, 0)

win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,1156, 766, 0, 0)
rect=(0,0,1440,900)
#win32api.ClipCursor(rect)
#time.sleep(8)
rect=(0,0,10,10)
win32api.ClipCursor(rect)
time.sleep(3)
win32api.ClipCursor()
errorMsg('运行了主文件')

time.sleep(3)
print("qqqqqq")
