import os,time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common import set_driver
class MenuLinkCase(unittest.TestCase):
    def setUp(self)->None: #把selenium的初始化配置放入
       self.driver = set_driver.setdriver()
    def tearDown(self)->None: #测试清理操作 浏览器关闭
        time.sleep(2)
        self.driver.quit()

    def test_my_link(self):
        '''case01 验证我的地盘菜单能否正确链接'''
        self.driver.find_element(By.XPATH,'//input[@id="account"]').send_keys('admin')
        self.driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('Lrh19960912')
        self.driver.find_element(By.XPATH,'//button[@id="submit"]').click()
        self.driver.find_element(By.XPATH,'//li[@data-id="my"]').click()
        self.assertTrue(EC.title_is("我的地盘 - 禅道"))

    def test_product_link(self):
        '''case02 验证产品菜单能否正确链接'''
        self.driver.find_element(By.XPATH, '//input[@id="account"]').send_keys('admin')
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('Lrh19960912')
        self.driver.find_element(By.XPATH, '//button[@id="submit"]').click()
        self.driver.find_element(By.XPATH, '//li[@data-id="product"]').click()
        self.assertTrue(EC.title_is("产品主页 - 禅道"))


if __name__ =='__main__':
   unittest.main()