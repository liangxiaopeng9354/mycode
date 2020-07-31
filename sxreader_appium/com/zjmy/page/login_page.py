#coding = utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sxreader_appium.com.zjmy.util.get_by_local import GetByLocal
from time import sleep
from sxreader_appium.com.zjmy.base.base_driver import *
import os

class LoginPage:
    def __init__(self,i):

        base_driver = BaseDrvier()
        self.driver = base_driver.android_driver(i)
        self.get_by_local = GetByLocal(self.driver)



    def get_username_element(self):
        '''
        获取登录的元素
        :return:
        '''

        return self.get_by_local.get_element('username')

    def get_password_element(self):
        '''
        获取密码元素
        :return:
        '''
        return self.get_by_local.get_element('password')
    def get_login_button_element(self):
        '''
        获取登录按钮元素
        :return:
        '''
        return self.get_by_local.get_element('login_button')

    def get_toast_element(self,msg):
        '''
        获取toast用来断言
        :return:
        '''
        sleep(2)
        toast_element = ("xpath", "//*[contains(@text,'%s')]"%msg)
        self.getImage()
        return WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_all_elements_located(toast_element))

    def getImage(self):
        '''
        截取图片,并保存在images文件夹
        :return: 无
        '''
        timestrmap = time.strftime('%Y%m%d_%H.%M.%S')
        imgPath = os.path.join('../report/', '%s.png' % str(timestrmap))
        print('this is imgPath:-----',imgPath)
        self.driver.save_screenshot(imgPath)
        print('screenshot:', timestrmap, '.png')








