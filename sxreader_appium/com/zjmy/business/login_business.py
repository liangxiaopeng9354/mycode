# coding=utf-8

from sxreader_appium_po.com.zjmy.handle.login_handle import LoginHandle
import time
import os
from page.login_page import LoginPage


class LoginBusiness:
    def __init__(self,i):
        self.login_handle = LoginHandle(i)

    def login_success(self):
        self.login_handle.send_username('201999')
        self.login_handle.send_password('qqqqqqq1')
        self.login_handle.clink_login()
        time.sleep(3)

    def login_fail(self):
        self.login_handle.send_username('208911')
        self.login_handle.send_password('qqqqqqq1')
        self.login_handle.clink_login()
        user_flag = self.login_handle.get_fail_toast('该账号不存在1')
        if user_flag:
            return True
        else:
            return False

    def login_password_error(self):
        self.login_handle.send_username('201999')
        self.login_handle.send_password('qqqqqqq')
        self.login_handle.clink_login()
        user_flag = self.login_handle.get_fail_toast('账号或密码错误，请重新输入')
        if user_flag:
            return True
        else:
            return False
    def get_page_login_img(self):
        login_page = LoginPage()
        res = login_page.getImage()
        return res

