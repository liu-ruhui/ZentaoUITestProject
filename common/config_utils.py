import os
import configparser
current_path = os.path.dirname(__file__)  # 获取路径
cfgpath =  os.path.join(current_path,'..\\conf\local_config.ini')
class ConfigUtils:
    def __init__(self,config_path=cfgpath):
        self.__conf = configparser.ConfigParser()
        self.__conf.read(config_path, encoding="utf-8")

    def read_ini(self,sec,option):
        return self.__conf.get(sec,option)

    @property
    def get_gecko_path(self):
        value = self.read_ini('geckodriver','location')
        return value

    @property
    def get_zentao_path(self):
        value = self.read_ini('zentao_url','location')
        return value

if __name__ =='__main__':
    conf_u = ConfigUtils()
    print(conf_u.get_zentao_path)
