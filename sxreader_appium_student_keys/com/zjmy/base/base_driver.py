# coding = utf -8

import time
from appium import webdriver
from util.write_user_command import WriteUserCommand
from util.server import Server


class BaseDrvier:
    def __init__(self):
        self.write_file = WriteUserCommand()
        self.server = Server()

    def android_driver(self,i):
        # devices_name
        # port
        #
        # self.server.main_server()
        print('wait.... this is androd_driver:',i)
        time.sleep(10)
        self.device_name = self.write_file.get_value('user_info_'+str(i), 'deviceName')
        self.port = self.write_file.get_value('user_info_'+str(i), 'port')
        print(self.device_name, '-------devices_name')
        print(self.port, '-------port')

        desired_caps = {
            "platformName": "Android",
            "deviceName": self.device_name,
            "platformVersion": "5.1.1",
            "app": "D:\sxreader_teacher.apk",
            "appActivity": "com.zjmy.sxreader.teacher.presenter.activity.login.LoginActivity",
            "noReset": "true",
            "automationName": "uiautomator2"
        }
        driver = webdriver.Remote('http://127.0.0.1:' + str(self.port) + '/wd/hub', desired_caps)
        time.sleep(3)
        return driver

    def ios_drvier(self):
        pass

    def get_drvier(self):
        pass


if __name__ == '__main__':
    baseDr = BaseDrvier()
    baseDr.android_driver()
