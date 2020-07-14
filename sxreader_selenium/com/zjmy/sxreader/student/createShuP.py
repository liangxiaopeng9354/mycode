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
from builtins import str, print
from test.test_struct import integer_codes
from sqlite3 import Time


class sxreader_com(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()   
        self.driver.maximize_window()    
        self.driver.implicitly_wait(30)
        #正式环境
        self.base_url = "https://sxreader.com/"
        #测试环境
        #self.base_url = "http://192.168.10.166"
        
        self.verificationErrors = []
        self.accept_next_alert = True
        
    
    def test_1(self):
        
        
        my_file="C:\login_stu.csv"
        
        driver = self.driver
        data=csv.reader(open(my_file))
        for shup_data in data:
            username=shup_data[0]
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
                print(shup_data[0]+" login is successful")
            except Exception as e:
                print(shup_data[0]+" login is fail")
            #点击精品书城模块
            driver.find_element_by_xpath(".//*[@id='app-body']/div[1]/div/div[2]/div[1]/div/a[4]").click()
            time.sleep(4)
            #点击搜索框
            driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/div/div[1]/div[2]/div[1]/input").click()
            driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/div/div[1]/div[2]/div[1]/input").clear()
            time.sleep(4)
            bookname=shup_data[1]
            driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/div/div[1]/div[2]/div[1]/input").send_keys(bookname)
            #点击搜索按钮
            driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/div/div[1]/div[2]/div[1]/span").click()
        
            #点击其中第一本书
            driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/div/div/ul/li[1]/div[1]/a/img").click()
            time.sleep(4)
            js="var q=document.documentElement.scrollTop=10000"
            driver.execute_script(js)
            #点击评论按钮
            driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/div/div/div[2]/div[3]/p/button").click()
            time.sleep(4)
            print("现在书点击评星阶段")
            #点击5颗星
            driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/div/div/div[2]/div[3]/form/div[1]/div/span/ul/li[5]").click()
            time.sleep(4)
            #点击书评输入框
            print("现在输入书评内容阶段")
            driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/div/div/div[2]/div[3]/form/div[1]/textarea").click()
            driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/div/div/div[2]/div[3]/form/div[1]/textarea").clear()
            time.sleep(4)
                    
            neirong=shup_data[2]                    
            driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/div/div/div[2]/div[3]/form/div[1]/textarea").send_keys(neirong)
            #点击提交按钮
            driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/div/div/div[2]/div[3]/form/div[2]/button").click()
        
            #退出页面
            driver.find_element_by_xpath(".//*[@id='app-body']/div[1]/div/div[2]/div[2]/a[2]/img").click()
            time.sleep(4)
            #点击退出登录按钮
            driver.find_element_by_xpath("html/body/drop-down-menu/ng-include/ul/li/a").click()
            time.sleep(4)
            #点击确定
            driver.find_element_by_xpath("html/body/div[3]/div[7]/div/button").click()
    
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
