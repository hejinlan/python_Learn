# coding=utf-8


import os
from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
time.sleep(10)
to_element =  driver.find_element_by_xpath('//*[contains(text(),"百度热搜")]' )
ActionChains(driver).move_to_element_with_offset(to_element, 200, 300).context_click().perform()
ActionChains(driver).move_by_offset(x=1150, y=769).click_and_hold().perform() # 鼠标左键点击， 200为x坐标， 100为y坐标
ActionChains(driver).move_by_offset(x=1150, y=769).context_click().perform() # 鼠标右键点击

"""
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
#driver.get("https://npm.taobao.org/mirrors/chromedriver")#http://chromedriver.storage.googleapis.com/index.html
driver.get("http://chromedriver.storage.googleapis.com/index.html")
time.sleep(5)
driVers = driver.find_element_by_partial_link_text("92.0.4515.").click()
#driVers =  driver.find_element_by_xpath('//*[contains(text(),"92.0.4515.")]' )
print(driVers)
#driver.find_element_by_partial_link_text("92.0.4515.").click()
#driver.find_element_by_xpath("//a[contains@href,'92.0.4515.107']").click()
time.sleep(5)
 
#选择下载文件
driver.find_element_by_xpath("//a[contains(@href,'chromedriver_win32.zip')]").click()
time.sleep(30)


import zipfile
def un_zip(file_name):
    #unzip zip file
    zip_file = zipfile.ZipFile(file_name)

    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")

    for names in zip_file.namelist():
        zip_file.extract(names,file_name + "_files/")
un_zip('d:\\Chrome\\webdriver\\chromedriver_win32.zip')
time.sleep(10)

from shutil import copyfile
if os.path.isfile('d:\\Chrome\\webdriver\\chromedriver.exe'):
    os.remove('d:\\Chrome\\webdriver\\chromedriver.exe')

try:
   copyfile('d:\\Chrome\\webdriver\\chromedriver_win32.zip_files\\chromedriver.exe', 'D:\\Chrome\\webdriver\\chromedriver.exe')
except IOError as e:
   print("Unable to copy file. %s" % e)
   exit(1)
except:
   print("Unexpected error:", sys.exc_info())
   exit(1)
 """
#driver.quit()

