import os,time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common import set_driver
from common import login

class LoginSuccesse(unittest.TestCase):
    def setUp(self)->None: #把selenium的初始化配置放入
       self.driver = set_driver.setdriver()
    def tearDown(self)->None: #测试清理操作 浏览器关闭
        time.sleep(2)
        self.driver.close()
        self.driver.quit()

    def test_login_01(self):
        '''case01 使用正确账号admin  正确密码Lrh19960912能否登陆'''
        login.login(self.driver,'admin','Lrh19960912')
        self.assertTrue(EC.text_to_be_present_in_element((By.XPATH,'//span[@class="user-name"]'),'admin'),'test_login用例执行失败')
    def test_login_02(self):
        '''case02 使用正确账号test01  正确密码Lrh123456能否登陆'''
        login.login(self.driver,'test01','Lrh123456')
        actual_result = self.driver.find_element(By.XPATH, '//span[@class="user-name"]').text
        self.assertEqual(actual_result, '测试人员01', 'test_login用例执行失败')


if __name__ =='__main__':
   unittest.main()