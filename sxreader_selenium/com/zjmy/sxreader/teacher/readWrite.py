# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import csv
import random
from _socket import close

class ReadWrite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
         #正式环境
        #self.base_url = "https://sxreader.com/"
        
        #测试环境
        self.base_url = "http://192.168.10.166/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_read_write(self):
        
         for i in range(0,1):
            print(i)
            my_file="C:\login.csv"
            
            driver = self.driver
            openf=open(my_file)

            data=csv.reader(openf)
            
            for user in data:
        
                #登录
                driver.get(self.base_url + "/signin.html#/loginInfo")
                driver.find_element_by_id("username").clear()
                driver.find_element_by_id("username").send_keys("13810089226")
                driver.find_element_by_id("password").click()
                driver.find_element_by_id("password").clear()
                driver.find_element_by_id("password").send_keys("123456")
                time.sleep(1)
                driver.find_element_by_css_selector("button[type=\"submit\"]").click()
                openf.close()
                
                #断言检测用户是否登录成功，并且能够成功跳转到首页
                try:
                    assert driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]").text == "班级："
                    print(user[0]+" login is successful")
                except Exception as e:
                    print(user[0]+" login is fail")
            
                    
            
                #点击任务按钮跳转到任务模块
                driver.find_element_by_link_text("任务").click()
                time.sleep(1)
                driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/section/div[1]/div[2]/span[2]").click()
                time.sleep(1)
                
                a=random.randint(0,1000)
                print(a)
                #点击任务标题        
                driver.find_element_by_name("taskTitle").clear()
                driver.find_element_by_name("taskTitle").send_keys("Write读写任务"+str(a))
                print("Write读写任务"+str(a))
                time.sleep(3)
                #置入附件
                driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/ui-view/section/div[1]/form/div[2]/div[2]/span").click()
                time.sleep(1)
                #搜索一本书
                driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/ui-view/section/ui-view/div[1]/div/input").click()
                driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/ui-view/section/ui-view/div[1]/div/input").send_keys("聊斋")
                time.sleep(1)
                #点击搜索按钮
                driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/ui-view/section/ui-view/div[1]/div/span/i").click()
                time.sleep(2)
                #选择这本书
                driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/ui-view/section/ui-view/div[2]/ul/div[1]/li/div/span").click()
                time.sleep(1)
                #选择时间
                driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/ui-view/section/div[1]/form/div[3]/div[2]/div/div/datepicker[2]/input").click()
                driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/ui-view/section/div[1]/form/div[3]/div[2]/div/div/datepicker[2]/div/div[4]/a[30]").click()
                #输入内容
                driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/ui-view/section/div[1]/form/div[5]/div[2]/textarea").click()
                driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/ui-view/section/div[1]/form/div[5]/div[2]/textarea").send_keys("任务内容无所谓")
                time.sleep(1)
                #点击发布按钮
                driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/ui-view/section/div[4]/div[2]/span[2]").click()
                time.sleep(1)
                #关闭文件
                close(my_file)
                    #退出页面
            driver.find_element_by_xpath(".//*[@id='app-body']/div[1]/div/div[2]/div[2]/a[2]/img").click()
            time.sleep(1)
            driver.find_element_by_xpath(".//*[@id='app-body']/div[1]/div/div[2]/div[2]/ul/li/a").click()
            time.sleep(1)
            driver.find_element_by_xpath("html/body/div[3]/div[7]/div/button").click()
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
