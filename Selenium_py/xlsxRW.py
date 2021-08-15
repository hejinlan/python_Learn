from openpyxl  import load_workbook

import pyautogui
#import cv2
#import numpy as np

img = pyautogui.screenshot(region=[0,0,500,600]) # x,y,w,h

#img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)
img.save('screenshot0cv.png')
//cv2.imwrite('screenshot0cv.png',img)
