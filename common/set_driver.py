import os
from selenium import webdriver
from common.config_utils import ConfigUtils
conf = ConfigUtils()

def setdriver():
    current = os.path.dirname(__file__)
    chrome_driver = os.path.join(current, conf.get_gecko_path)
    driver = webdriver.Firefox(executable_path=chrome_driver)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(conf.get_zentao_path)
    return driver

if __name__ =='__main__':
   setdriver()
