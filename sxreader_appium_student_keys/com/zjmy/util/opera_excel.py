# -*- coding: utf-8 -*-
# @Time    : 2020-6-18 20:52
# @Author  : liangxiaopeng
# @File    : opera_excel.py

import xlrd


class OperaExcel:

    def __init__(self, filepath=None, i=None):
        if filepath == None:
            self.filepath = 'D:/case_key.xlsx'
        else:
            self.filepath = filepath
        if i == None:
            self.i = 0
        else:
            self.i = i
        self.excel = self.get_excel()
        self.data = self.get_sheets(self.i)

    def get_excel(self):
        '''
        获取Excel
        :return:
        '''

        excel = xlrd.open_workbook(self.filepath)
        return excel

    def get_sheets(self, i):
        '''
        获取sheet内容
        :param i:
        :return:
        '''
        tables = self.excel.sheets()[i]
        return tables

    def get_lines(self):
        '''
        获取Excel行数
        :return:
        '''
        lines = self.data.nrows
        return lines

    def get_cell(self, row, cell):
        data = self.data.cell(row, cell).value
        return data


