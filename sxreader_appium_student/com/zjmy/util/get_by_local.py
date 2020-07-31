# coding = utf-8
from util.read_ini import ReadIni


class GetByLocal:

    def __init__(self, driver=None):
        self.driver = driver

    def get_element(self, page_element, key):
        read_ini = ReadIni()
        local = read_ini.get_value(page_element, key)
        by = local.split('>')[0]
        local_by = local.split('>')[1]
        if local != None:
            if by == 'id':
                return self.driver.find_element_by_id(local_by)
            elif by == 'className':
                return self.driver.find_elements_by_class_name(local_by)
            else:
                return self.driver.find_element_by_android_uiautomator(local_by)

        else:
            return None
