# -*- coding: utf-8 -*-
import unittest
import HTMLTestRunner
import os
from appium import webdriver
from time import sleep
import time
from test.test_decimal import file
from symbol import except_clause
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Dttest(unittest.TestCase):
   
    def __init__(self, methodName='runTest'):
        unittest.TestCase.__init__(self, methodName=methodName)
   
   
   
    def setUp(self):
        print('start setup')
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        #链接设备，使用adb devices命令去查询
        #荣耀7i的版本号是69T7N16719001974
        #华为p9的版本号是PBV7N16719012844
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['automationName'] = 'Uiautomator2'
        #通过adb shell logcat|findstr "Displayed"
        desired_caps['appPackage'] = 'com.zjmy.sxreader.studet'

        desired_caps['appActivity'] = 'com.zjmy.sxreader.studet.presenter.activity.login.LoginActivity'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        #desired_caps['autoGrantPermissions'] = True        
        
        #appium链接地址
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    def tearDown(self):
        self.driver.quit()
        print('tearDown')
    
    def test_login_success(self):#用例
        #self.always_allow()
        self.driver.find_element_by_id("com.zjmy.sxreader.studet:id/et_login_name").clear()
        self.driver.find_element_by_id("com.zjmy.sxreader.studet:id/et_login_name").send_keys("201808")
        self.driver.find_element_by_id("com.zjmy.sxreader.studet:id/et_login_psd").clear()
        self.driver.find_element_by_id("com.zjmy.sxreader.studet:id/et_login_psd").send_keys("201808")
        self.driver.find_element_by_id("com.zjmy.sxreader.studet:id/btn_login").click()
        sleep(3) #3秒登录检测
    '''    
    def always_allow(self):
        for i in range(3):
            #toast_loc = ("xpath", ".//*[contains(@text,'%s')]"%text)
            loc = ("xpath", ".//*[contains(@text,'始终允许')]")
            try:
                e = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                pass   
    '''   
if __name__ == '__main__':
    suite = unittest.TestSuite()#创建一个测试集合
    #需要测试的用例就addTest，不加的就不会运行
    #suite.addTest(Dttest('test_login_success'))
    suite.addTest(Dttest('test_login_failer'))
    #unittest.TextTestRunner(verbosity=1).run(suite)
    #timestr = time.strftime('%Y-%m-%d %X',time.localtime(time.time()))#本地日期时间作为测试报告的名字
   
    filename = 'D:\\appium\\report1.html'#这个路径改成自己的目录路径
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='result',
        description='report'
    )
 
    runner.run(suite)
    fp.close()
   