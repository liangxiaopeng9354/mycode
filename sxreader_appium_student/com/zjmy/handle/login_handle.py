#coding=utf-8
from page.login_page import LoginPage
class LoginHandle:
    def __init__(self,i):
        self.login_page=LoginPage(i)

    '''
    操作登录页面的元素
    '''
    #输入用户名
    def send_username(self,user):
        self.login_page.get_username_element().send_keys(user)
    #输入密码
    def send_password(self,password):
        self.login_page.get_password_element().send_keys(password)
    #点击登录按钮
    def clink_login(self):
        self.login_page.get_login_button_element().click()

    def get_fail_toast(self,message):
        toast_element = self.login_page.get_toast_element(message)
        if toast_element:
            return True
        else:
            return False