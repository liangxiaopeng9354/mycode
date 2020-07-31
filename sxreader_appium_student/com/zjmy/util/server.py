# -*- coding: utf-8 -*-
from dos_cmd import DosCmd
from port import *
import threading
import time
from write_user_command import WriteUserCommand


class Server:
    '''
    获取设备信息
    '''

    def __init__(self):
        self.write_file = WriteUserCommand()
        self.dos = DosCmd()
        self.device_list = self.get_devices()


    def get_devices(self):
        device_list = []
        result_list = self.dos.excute_cmd_result('adb devices')
        if len(result_list) > 1:
            for i in result_list:
                if 'List' in i:
                    continue
                device_info = i.split('\t')
                if device_info[1] == 'device':
                    device_list.append(device_info[0])
            return device_list
        else:
            return None

    def create_port_list(self, start_port):
        port = Port()
        port_list = []
        port_list = port.create_port_list(start_port, self.device_list)
        return port_list

    def create_command_list(self,i):
        '''
        appium -p 4700 -bp 4701 -U 127.0.0.1:62001
        :return:
        '''
        command_list = []
        appium_port_list = self.create_port_list(4700)
        bootstrap_port_list = self.create_port_list(4800)
        deivce_list = self.device_list

        self.write_file.post_value(i,bootstrap_port_list[i],deivce_list[i],appium_port_list[i])
        command = 'appium -p ' + str(appium_port_list[i]) + ' -bp ' + str(bootstrap_port_list[i]) + ' -U ' + \
                  deivce_list[i] + ' --no-reset --session-override'
        command_list.append(command)
        if len(command_list) == 0:
            print('当前无可用设备')
        else:
            print(command_list)
        return command_list

    # 启动程序服务
    def start_server(self, i):
        self.start_list = self.create_command_list(i)
        self.dos.excute_cmd(self.start_list[0])

    # 杀掉进程
    def kill_server(self):
        server_list = self.dos.excute_cmd_result('tasklist | find "node.exe"')
        if len(server_list) > 0:
            self.dos.excute_cmd('taskkill -F -PID node.exe')
        else:
            print('没有找到相关进程')

    # 主函数使用多线程去调用start_server
    def main_server(self):
        self.kill_server()
        self.write_file.clear_data()
        for i in range(len(self.device_list)):
            appium_start = threading.Thread(target=self.start_server, args=(i,))
            appium_start.start()
        time.sleep(5)


if __name__ == '__main__':
    server = Server()
    print(server.main_server())
