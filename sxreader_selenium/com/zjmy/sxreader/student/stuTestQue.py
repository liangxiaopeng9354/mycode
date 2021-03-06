#书香阅读登录功能测试

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from setuptools.unicode_utils import try_encode
import csv
from builtins import str
from test.test_struct import integer_codes
from sqlite3 import Time


class sxreader_com(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()   
        self.driver.maximize_window()    
        self.driver.implicitly_wait(30)
        
        self.base_url = "http://192.168.10.166"
        
        self.verificationErrors = []
        self.accept_next_alert = True
        
    
    def test_1(self):
        
        
        my_file="C:\login_stu.csv"
        
        driver = self.driver
        data=csv.reader(open(my_file))
        for user in data:
            username=user[0]
            driver.get(self.base_url + "/signin.html#/loginInfo")
            driver.find_element_by_xpath(".//*[@id='username']").clear()            
            driver.find_element_by_xpath(".//*[@id='username']").send_keys(username)
            passwd=username[-6:]
            print(passwd)
            
            driver.find_element_by_xpath(".//*[@id='password']").clear()
            driver.find_element_by_xpath(".//*[@id='password']").send_keys(passwd)
            driver.find_element_by_css_selector(".loginBoxBtn>button").click()
       
            #添加断言验证是否登录成功
            
            try:
                assert driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/div[2]/div[1]/h3/span").text == "本周成果"
                print(user[0]+" login is successful")
            except Exception as e:
                print(user[0]+" login is fail")
            #点击我的任务模块
            driver.find_element_by_xpath(".//*[@id='app-body']/div[1]/div/div[2]/div[1]/div/a[2]").click()
            #点击写作品的按钮
            
            driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/div/div[4]/ul/li[1]/div/div[2]/a[2]/span").click()
            time.sleep(1)
            
            for i in range(0,5):
            #选择一个选项，并且点击下一题
                driver.find_element_by_xpath(".//*[@id='app']/div[2]/div/div[2]/div[2]/p[1]").click()
                time.sleep(1)
                driver.find_element_by_xpath(".//*[@id='app']/div[2]/div/div[3]").click()
                time.sleep(1)
            
                
        #退出页面
        driver.find_element_by_xpath(".//*[@id='app']/div[1]/div[1]/div[2]/div/img").click()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='app']/div[1]/div[2]/div").click()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='app']/div[1]/div[2]/div/div/div[2]").click()
        time.sleep(2)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
