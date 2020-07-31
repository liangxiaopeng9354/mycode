# coding = utf-8
import configparser


class ReadIni:
    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = '../config/localElement.ini'

        else:
            self.file_path = file_path
        self.data = self.read_ini()

    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path)

        return read_ini

    def get_value(self,page_element, key, section=None):
        if section == None:
            return self.data.get(page_element, key)

        try:
            value = self.data.get(section, key)
        except:
            value = None
        return value


if __name__ == '__main__':
    readini = ReadIni()
    print(readini.get_value('bookself_element','book'))
