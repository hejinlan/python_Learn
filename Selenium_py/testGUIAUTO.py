import pyautogui
import time
"""
# 获取当前屏幕分辨率
screenWidth, screenHeight = pyautogui.size()

# 获取当前鼠标位置
currentMouseX, currentMouseY = pyautogui.position()

# 2秒钟鼠标移动坐标为100,100位置  绝对移动
#pyautogui.moveTo(100, 100,2)
pyautogui.moveTo(x=100, y=100,duration=2, tween=pyautogui.linear)

#鼠标移到屏幕中央。
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)

# 鼠标左击一次
#pyautogui.click()
# x 
# y 
# clicks 点击次数
# interval点击之间的间隔
# button 'left', 'middle', 'right' 对应鼠标 左 中 右或者取值(1, 2, or 3)
# tween 渐变函数
#
pyautogui.click(x=None, y=None, clicks=1, interval=0.0, button='left', duration=0.0, tween=pyautogui.linear)

# 鼠标相对移动 ,向下移动
#pyautogui.moveRel(None, 10)
#pyautogui.moveRel(xOffset=None, yOffset=10,duration=0.0, tween=pyautogui.linear)


# 鼠标当前位置0间隔双击
#pyautogui.doubleClick()
pyautogui.doubleClick(x=None, y=None, interval=0.0, button='left', duration=0.0, tween=pyautogui.linear)

# 鼠标当前位置3击
#pyautogui.tripleClick()
pyautogui.tripleClick(x=None, y=None, interval=0.0, button='left', duration=0.0, tween=pyautogui.linear)

#右击
pyautogui.rightClick()

#中击
pyautogui.middleClick()

#  用缓动/渐变函数让鼠标2秒后移动到(500,500)位置
#  use tweening/easing function to move mouse over 2 seconds.
pyautogui.moveTo(x=500, y=500, duration=2, tween=pyautogui.easeInOutQuad)

#鼠标拖拽
pyautogui.dragTo(x=427, y=535, duration=3,button='left')

#鼠标相对拖拽
#pyautogui.dragRel(xOffset=100,yOffset=100,duration=,button='left',mouseDownUp=False)

#鼠标移动到x=1796, y=778位置按下
pyautogui.mouseDown(x=1796, y=778, button='left')

#鼠标移动到x=2745, y=778位置松开（与mouseDown组合使用选中）
pyautogui.mouseUp(x=2745, y=778, button='left',duration=5)

time.sleep(5)
pyautogui.mouseDown(x=1150, y=769, button='left')
pyautogui.moveTo(x=1269, y=680, duration=2, tween=pyautogui.easeInOutQuad)

time.sleep(2)  region=[0,0,1440,900]
#pyautogui.click()
"""
time.sleep(5)
img = pyautogui.screenshot()
img.save('screenshot012cv.png')

#time.sleep(2)
#pyautogui.mouseUp(x=1269, y=680, button='left',duration=2)



