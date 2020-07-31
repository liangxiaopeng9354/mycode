# -*- coding: utf-8 -*-
# @Time    : 2020-6-18 21:41
# @Author  : liangxiaopeng
# @File    : action_method.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDrvier
from util.get_by_local import GetByLocal
import os
import time


class ActionMethod:

    def __init__(self):
        basedriver = BaseDrvier()
        self.driver = basedriver.android_driver(0)
        self.get_by_local = GetByLocal(self.driver)

    def input(self, *args):
        '''
        输入值
        :param element_key:
        :param value:
        :return:
        '''
        element = self.get_by_local.get_element(args[0])
        if element == None:
            return args[0], "元素没找到"
        element.send_keys(args[1])

    def on_click(self, *args):
        '''
        元素点击
        :param element_key:
        :return:
        '''
        if args[0] == None:
            return False
        else:
            element = self.get_by_local.get_element(args[0])
            if element == None:
                return args[0], "元素没找到"
            element.click()

    def sleep_time(self, *args):

        time.sleep(int(args[0]))

    def get_size(self, *args):

        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    def swipe_left(self, *args):
        x1 = self.get_size()[0] / 10 * 9
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10
        self.driver.swipe(x1, y1, x, y1)

    # 向右滑动
    def swipe_right(self, *args):
        x1 = self.get_size()[0] / 10
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10 * 9
        self.driver.swipe(x1, y1, x, y1)

    # 向上滑动
    def swipe_up(self, *args):
        print('开始执行向上滑动的方法')
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 6
        y = self.get_size()[1] / 10 * 2
        self.driver.swipe(x1, y1, x1, y, 1000)

    # 向下滑动
    def swipe_down(self, *args):
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10
        y = self.get_size()[1] / 10 * 9
        self.driver.swipe(x1, y1, x1, y)

    def swipe_on(self, direction):
        if direction == 'up':
            self.swipe_up()
        elif direction == 'down':
            self.swipe_down()
        elif direction == 'left':
            self.swipe_left()
        else:
            self.swipe_right()

    def get_element(self, *args):
        element = self.get_by_local.get_element(args[0])
        if element == '':
            return None
        return element

    def get_toast(self, *args):
        '''
        获取toast用来断言
        :return:
        '''
        print('获取到toast的预期元素-------', args[0])

        toast_element = ("xpath", "//*[contains(@text,'%s')]" % args[0])
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
