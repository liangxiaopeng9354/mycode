# coding = utf-8
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sxreader_appium_po.com.zjmy.page.login_page import LoginPage

def get_drvier():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "127.0.0.1:62001",
        "platformVersion":"5.1.1",
        "app": "D:\sxreader_teacher.apk",
        "appActivity": "com.zjmy.sxreader.teacher.presenter.activity.login.LoginActivity",
        "noReset": "true",
        "automationName":"uiautomator2"
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver


driver = get_drvier()


def login():
    login_page = LoginPage(driver)
    login_page.get_login_element().send_keys('201999')
    login_page.get_password_element().send_keys('qqqqqqq1')
    sleep(1)
    login_page.get_login_button_element().click()
    sleep(1)


def login_by_node():
    element = driver.find_element_by_id("com.zjmy.sxreader.teacher:id/container")
    elements = element.find_elements_by_class_name("android.widget.EditText")
    elements[0].send_keys('201999')
    elements[1].send_keys('qqqqqqq1')
    driver.find_element_by_id("com.zjmy.sxreader.teacher:id/btn_login").click()
    sleep(1)

def login_by_uiatomator():
    driver.find_element_by_android_uiautomator('text(\"201999\")').clear()
    driver.find_element_by_android_uiautomator('text(\"用户名\")').send_keys('098098')
    driver.find_element_by_id('com.zjmy.sxreader.teacher:id/et_login_psd').send_keys('098098')
    driver.find_element_by_id("com.zjmy.sxreader.teacher:id/btn_login").click()
    sleep(1)

def get_toast():
    sleep(2)
    driver.find_element_by_id('com.zjmy.sxreader.teacher:id/et_login_name').send_keys('201999')
    driver.find_element_by_id('com.zjmy.sxreader.teacher:id/btn_login').click()

    toast_element = ("xpath","//*[contains(@text,'请输入密码')]")
    print(WebDriverWait(driver,10,0.1).until(EC.presence_of_all_elements_located(toast_element)))

#get_toast()
login()
#login_by_uiatomator()

#
# driver = get_drvier()
#
#
# def get_size():
#
#   size = driver.get_window_size()
#   width = size['width']
#   height = size ['height']
#   return width,height
#
# def swipe_left():
#   x1 = get_size()[0]/10*9
#   y1 = get_size()[1]/2
#   x = get_size()[0]/10
#   driver.swipe(x1,y1,x,y1)
# #向右滑动
# def swipe_right():
#   x1 = get_size()[0]/10
#   y1 = get_size()[1]/2
#   x = get_size()[0]/10*9
#   driver.swipe(x1,y1,x,y1)
#
#
# #向上滑动
# def swipe_up():
#   x1 = get_size()[0]/2
#   y1 = get_size()[1]/10*9
#   y = get_size()[1]/10
#   driver.swipe(x1,y1,x1,y)
#
#
# #向下滑动
# def swipe_down():
#   x1 = get_size()[0]/2
#   y1 = get_size()[1]/10
#   y = get_size()[1]/10*9
#   driver.swipe(x1,y1,x1,y)
#
#
# def swipe_on(direction):
#   if direction == 'up':
#     swipe_up()
#   elif direction == 'down':
#     swipe_down()
#   elif direction == 'left':
#     swipe_left()
#   else:
#     swipe_right()
#
# swipe_on('up')
