import time
import unittest
from common import set_driver
from common import login,exit
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Exit(unittest.TestCase):
    def setUp(self):
        self.driver = set_driver.setdriver()
        login.login(self.driver,'admin','Lrh19960912')
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
    def test_exit(self):
        '''case04 退出登录操作'''
        exit.exit(self.driver)
        WebDriverWait(self.driver,10).until(EC.title_is('用户登录 - 禅道'))
if __name__ =='__main__':
    unittest.main()