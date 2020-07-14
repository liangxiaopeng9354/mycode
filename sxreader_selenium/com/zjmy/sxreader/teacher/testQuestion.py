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
from fileinput import close

class TestQuestion(unittest.TestCase):
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
    
    def test_question(self):
        
        for i in range(0,2):
            print(i)
            my_file="C:\login.csv"
            driver = self.driver
            data=csv.reader(open(my_file))
            
            for user in data:
                #用户登录
                driver.get(self.base_url + "/signin.html#/loginInfo")
                driver.find_element_by_id("username").clear()
                driver.find_element_by_id("username").send_keys(user[0])
                driver.find_element_by_id("password").clear()
                driver.find_element_by_id("password").send_keys("123456")
                driver.find_element_by_css_selector("button[type=\"submit\"]").click()
                time.sleep(1)
                
                #断言检测用户是否登录成功，并且能够成功跳转到首页
                try:
                    assert driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]").text == "班级："
                    print(user[0]+" login is successful")
                except Exception as e:
                    print(user[0]+" login is fail")
                
                driver.find_element_by_link_text("任务").click()
                driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/section/div[1]/div[2]/span[2]").click()
                time.sleep(1)
                
                a=random.randint(0,1000)
                print(a)
                
                
                driver.find_element_by_name("taskTitle").clear()
                driver.find_element_by_name("taskTitle").send_keys("Question有题任务"+str(a))
                print("Question有题任务"+str(a))
                time.sleep(1)
                driver.find_element_by_css_selector("span.whiteBtn").click()
                #搜索一本书，点击置入
                driver.find_element_by_xpath("//input[@type='text']").clear()
                driver.find_element_by_xpath("//input[@type='text']").send_keys("草房子")
                driver.find_element_by_css_selector("i.fa.fa-search").click()
                time.sleep(2)
                driver.find_element_by_css_selector("span.commonBtn").click()
                time.sleep(2)
                driver.find_element_by_xpath("(//input[@type='text'])[3]").click()
                driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/ui-view/section/div[2]/form/div[3]/div[2]/div/div/datepicker[2]/div/div[4]/a[30]").click()
                time.sleep(0.5)
                driver.find_element_by_xpath("//div[@id='app-body']/div[2]/div/div/div/ui-view/section/div[2]/form/div[5]/div[2]/textarea").clear()
                driver.find_element_by_xpath("//div[@id='app-body']/div[2]/div/div/div/ui-view/section/div[2]/form/div[5]/div[2]/textarea").send_keys("有题")
                time.sleep(1)
                #点击下一步
                driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/ui-view/section/div[5]/div[2]/span").click()
                #选择题目
                time.sleep(0.5)
                driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/ui-view/section/div[3]/div[3]/div[2]/span").click()
                time.sleep(0.5)
                driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/ui-view/section/div[3]/div[4]/div[2]/span").click()
                time.sleep(0.5)
                driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/ui-view/section/div[3]/div[5]/div[2]/span").click()
                time.sleep(0.5)
                driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/ui-view/section/div[3]/div[6]/div[2]/span").click()
                time.sleep(0.5)
                driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/ui-view/section/div[3]/div[7]/div[2]/span").click()
                time.sleep(0.5)
                #点击下一步
                driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/ui-view/section/div[5]/div[2]/span[3]").click()
                time.sleep(0.5)
                #点击发布按钮
                driver.find_element_by_xpath(".//*[@id='app-body']/div[2]/div/div/div/ui-view/section/div[5]/div[2]/span[2]").click()
                time.sleep(0.5)
            
            open(my_file).close()
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
