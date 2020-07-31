# coding=utf-8

from handle.bookself_handle import BookSelfHandle
from page.login_page import LoginPage
import time
from page.bookself_page import BookSelfPage
import os

class BookSelfBusiness:
    def __init__(self,i):
        self.book_self_handle = BookSelfHandle(i)

    #切换书架按钮
    def begin_book_self(self):
        self.book_self_handle.click_begin_book_self()
        time.sleep(2)

    #打开一本书
    def open_book(self):
        self.book_self_handle.click_book()
        time.sleep(2)

    #点击搜索按钮
    def click_search_suc(self):
        self.book_self_handle.click_search()
        time.sleep(2)

    def click_cloud_suc(self):
        self.book_self_handle.click_cloud()
        time.sleep(2)


    def get_page_login_img(self):
        bookself_page = BookSelfPage()
        res = bookself_page.getImage()
        return res

