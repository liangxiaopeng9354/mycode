# coding=utf-8

from handle.login_handle import LoginHandle
import time
import os
from page.login_page import LoginPage
from handle.bookself_handle import BookSelfHandle
from page.bookself_page import BookSelfPage


class LoginBusiness:
    def __init__(self,i):
        self.login_handle = LoginHandle(i)

    def login_success(self):
        self.login_handle.send_username('100005')
        self.login_handle.send_password('qqqqqqq1')
        print("login_handle.clink_login()...............")
        self.login_handle.clink_login()



    def login_fail(self):
        self.login_handle.send_username('208911')
        self.login_handle.send_password('qqqqqqq1')
        self.login_handle.clink_login()
        user_flag = self.login_handle.get_fail_toast('该账号不存在')
        if user_flag:
            return True
        else:
            return False

    def login_password_error(self):
        self.login_handle.send_username('100006')
        self.login_handle.send_password('100007')
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

