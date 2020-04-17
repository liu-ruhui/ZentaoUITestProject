import time
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common import set_driver
from common import login

class LoginFailCase(unittest.TestCase):
    def setUp(self)->None: #把selenium的初始化配置放入
      self.driver = set_driver.setdriver()
    def tearDown(self)->None: #测试清理操作 浏览器关闭
        time.sleep(2)
        self.driver.quit()

    def test_login(self):
        '''case01使用正确账号：admin 错误密码123456'''
        login.login(self.driver,'admin','123456')
        self.assertTrue(WebDriverWait(self.driver,10).until(EC.alert_is_present()))

if __name__ =='__main__':
   unittest.main()