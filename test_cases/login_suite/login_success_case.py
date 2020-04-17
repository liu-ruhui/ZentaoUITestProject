import os,time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common import set_driver

class LoginSuccesse(unittest.TestCase):
    def setUp(self)->None: #把selenium的初始化配置放入
       self.driver = set_driver.setdriver()
    def tearDown(self)->None: #测试清理操作 浏览器关闭
        time.sleep(2)
        self.driver.close()
        self.driver.quit()

    def test_login_01(self):
        '''case01 使用admin  Lrh19960912能否登陆'''
        self.driver.find_element(By.XPATH,'//input[@id="account"]').send_keys('admin')
        self.driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('Lrh19960912')
        self.driver.find_element(By.XPATH,'//button[@id="submit"]').click()
        self.assertTrue(EC.text_to_be_present_in_element((By.XPATH,'//span[@class="user-name"]'),'admin'),'test_login用例执行失败')
    def test_login_02(self):
        '''case02 使用admin Lrh123456能否登陆'''
        self.driver.find_element(By.XPATH, '//input[@id="account"]').send_keys('test01')
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('Lrh123456')
        self.driver.find_element(By.XPATH, '//button[@id="submit"]').click()
        actual_result = self.driver.find_element(By.XPATH, '//span[@class="user-name"]').text
        self.assertEqual(actual_result, '测试人员01', 'test_login用例执行失败')


if __name__ =='__main__':
   unittest.main()