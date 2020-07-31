# coding=utf-8
from page.bookself_page import BookSelfPage


class BookSelfHandle:
    def __init__(self,i):
        self.bookself_page = BookSelfPage(i)

    '''
    操作登录页面的元素
    '''

    # 点击书架图书
    def click_book(self):
        self.bookself_page.get_book_element().click()

    # 点击搜索按钮
    def click_search(self):
        self.bookself_page.get_bookself_search_element().click()

    # 点击小云
    def click_cloud(self):
        self.bookself_page.get_bookself_cloud_element().click()

    # 点击切换书架功能按钮
    def click_begin_book_self(self):
        self.bookself_page.get_begin_book_self_element().click()

    # 获取toast
    def get_fail_toast(self, message):
        toast_element = self.bookself_page.get_toast_element(message)
        if toast_element:
            return True
        else:
            return False
