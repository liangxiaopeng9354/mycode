# coding=utf-8
import os
import subprocess
class DosCmd:
    def excute_cmd_result(self,dos):
        res_list = []
        res = os.popen(dos).readlines()
        for i in res:
            # print(i)
            if i == '\n':
                continue
            res_list.append(i.strip('\n'))

        return res_list

    def excute_cmd(self,command):
        os.system(command)
        #subprocess.run(command)


if __name__ == '__main__':
    res = DosCmd().excute_cmd(' appium -p 4668 -bp 5003 -U 127.0.0.1:62001 ')
    res2 = DosCmd().excute_cmd('dir')


    print(res)
    print(res2)
