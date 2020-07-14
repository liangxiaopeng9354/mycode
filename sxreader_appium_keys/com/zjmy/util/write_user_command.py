# coding=utf-8
import yaml
import time


class WriteUserCommand:

    def read_data(self):
        print('1111111111111111')
        with open('../config/demo5.yaml') as fr:
            data = yaml.safe_load(fr)
            print(data)

        return data

    def get_value(self, user_info, key):

        data = self.read_data()
        value = data[user_info][key]
        return value

    def post_value(self, i, bp, deviceName, port):
        user_info = 'user_info_' + str(i)
        dict_var = {user_info: {'bp': bp, 'deviceName': deviceName, 'port': port}}
        print(yaml.dump(dict_var, ))  # 转为字符串，使用默认flow流格式

        with open('../config/demo5.yaml', 'a', encoding='utf-8') as f:
            yaml.dump(dict_var, f, default_flow_style=False)  # 写入文件，不是用flow流格式
        f.close()
        print('post_value方法中')
        time.sleep(3)

    def clear_data(self):
        with open('../config/demo5.yaml', 'w') as f:
            f.truncate()
        f.close()

    def get_data_lines(self):
        data = self.read_data()
        if data == None:
            return None
        else:
            res = len(data)
            return res


if __name__ == '__main__':
    write_file = WriteUserCommand()
    # write_file.post_value(1, 888, '12123werwe', 9909)
    print(write_file.read_data())
    print('this is get_data_lines value :', write_file.get_data_lines())
    print(write_file.get_value('user_info_0', 'deviceName'))
