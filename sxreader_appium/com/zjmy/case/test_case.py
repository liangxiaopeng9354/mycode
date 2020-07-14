# coding = utf-8
import unittest
import HTMLTestRunner
import time
from util.server import Server
from multiprocessing import Process
from util.write_user_command import WriteUserCommand
from login_business import LoginBusiness


class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        global parames
        parames = parame


class CaseTest(ParameTestCase):

    @classmethod
    def setUpClass(cls):
        print('this is setupClass', parames)

        cls.login_bus = LoginBusiness(parames)

    def setUp(self):
        print('this is setup')

    def tearDown(self):
        print('this is teardown')

    def test_fail(self):
        self.login_bus.login_fail()
        # self.assertEquals('1','1')

    def test_suc(self):
        self.login_bus.login_success()
        print('this is case1')
        # self.assertEqual('1','2','数据错误')


def appium_init():
    server = Server()
    server.main_server()


def get_suite(i):
    suite = unittest.TestSuite()
    # suite.addTest(CaseTest('test_01'))
    print('this is get suite 中的 i ：', i)
    suite.addTest(CaseTest('test_fail', parame=i))
    suite.addTest(CaseTest('test_suc', parame=i))
    # unittest.TextTestRunner().run(suite)
    html_file = "../report/report%s.html" % i
    fp = open(html_file, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp)
    runner.run(suite)
    fp.close()


if __name__ == '__main__':
    # unittest.main()
    appium_init()
    write_file = WriteUserCommand()
    lines = write_file.get_data_lines()
    if lines != None:

        print('this is lines value: ', lines)
        threads = []
        for i in range(lines):
            t = Process(target=get_suite, args=(i,))
            threads.append(t)

        for j in threads:
            j.start()
            time.sleep(1)
    else:
        print('当前条件没有测试机！！！')
