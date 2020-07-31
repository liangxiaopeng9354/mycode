# coding = utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util.get_by_local import GetByLocal
from time import sleep
from base.base_driver import *
import os
from login_page import LoginPage


class BookSelfPage(LoginPage):
    def __init__(self,i):
        print(i,"..............................")



    def get_driver(self):
        print(self.driver)
        self.get_by_local = GetByLocal(self.driver)

    def get_book_element(self):
        '''
        获取书架一本书的元素
        :return:
        '''
        self.get_driver()
        return self.get_by_local.get_element('bookself_element', 'book')

    def get_bookself_search_element(self):
        '''
        获取书架搜索框的元素
        :return:
        '''
        self.get_driver()
        return self.get_by_local.get_element('bookself_element', 'bookself_search')

    def get_bookself_cloud_element(self):
        '''
        获取书架上小云的元素
        :return:
        '''
        self.get_driver()
        return self.get_by_local.get_element('bookself_element', 'bookself_cloud')

    def get_begin_book_self_element(self):
        '''
        获取begin_bookself下面几个按钮的书架按钮
        '''
        self.get_driver()
        return self.get_by_local.get_element('bookself_element', 'begin_bookself')

    def get_toast_element(self, msg):
        '''
        获取toast用来断言
        :return:
        '''
        sleep(2)
        toast_element = ("xpath", "//*[contains(@text,'%s')]" % msg)
        self.getImage()
        return WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_all_elements_located(toast_element))

    def getImage(self):
        '''
        截取图片,并保存在images文件夹
        :return: 无
        '''
        timestrmap = time.strftime('%Y%m%d_%H.%M.%S')
        imgPath = os.path.join('../report/', '%s.png' % str(timestrmap))
        print('this is imgPath:-----', imgPath)
        self.driver.save_screenshot(imgPath)
        print('screenshot:', timestrmap, '.png')
