# coding=utf-8

from dos_cmd import DosCmd
from server import *


class Port:
    def port_is_used(self, port_num):
        '''
        判断端口是否被占用
        :return:
        '''
        flag = True
        self.dos_cmd = DosCmd()
        result = self.dos_cmd.excute_cmd_result('netstat -ano | findstr ' + str(port_num))
        if len(result) > 0:
            flag = True
        else:
            flag = False
        return flag

    def create_port_list(self, start_port, device_list):
        '''
        生成可用端口
        :param start_port:
        :param device_list:
        :return:
        '''
        port_list = []
        if device_list != None:
            while len(port_list) != len(device_list):
                if self.port_is_used(start_port) != True:
                    port_list.append(start_port)
                start_port = start_port + 1
            return port_list
        else:
            print('端口生成失败')


if __name__ == '__main__':
    port = Port()
    server = Server()
    li = server.get_devices()
    res = port.create_port_list(4060, li)
    print(res)
