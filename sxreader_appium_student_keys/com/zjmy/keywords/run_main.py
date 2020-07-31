# -*- coding: utf-8 -*-
# @Time    : 2020-6-19 22:05
# @Author  : liangxiaopeng
# @File    : run_main.py

from get_data import GetData
from action_method import ActionMethod
from sxreader_appium_keys.com.zjmy.util.server import Server


class RunMain:
    def run_method(self):
        server = Server()
        server.main_server()
        data = GetData()
        action_method = ActionMethod()
        lines = data.get_case_lines()
        for i in range(1,lines):
            #步骤
            handle_step = data.get_handle_step(i)
            #元素
            element_key = data.get_element_key(i)
            #操作值
            handle_value = data.get_handle_value(i)
            print('this is handle_value -------',handle_value)
            #预期元素
            expect_key = data.get_expect_element(i)
            #预期步骤
            expect_step = data.get_expect_handle(i)
            #input() login_button
            #input str

            excute_method = getattr(action_method,handle_step)
            if element_key != None:
                excute_method(element_key,handle_value)
            else:
                excute_method(handle_value)

            if expect_step != None:
                expect_result = getattr(action_method,expect_step)
                expect_result(expect_key)



if __name__ == '__main__':
    run = RunMain()
    run.run_method()


