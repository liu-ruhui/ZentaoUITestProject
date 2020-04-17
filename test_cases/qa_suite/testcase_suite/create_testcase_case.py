import time
import unittest
from common import set_driver,exit,login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CreateCase(unittest.TestCase):
    def setUp(self):
        self.driver = set_driver.setdriver()
        login.login(self.driver,'admin','Lrh19960912')
    def tearDown(self):
        exit.exit(self.driver)
        self.driver.quit()
    def test_create_case(self):
        '''case01  创建一条新的用例'''
        # 创建用例
        self.driver.find_element_by_link_text('测试').click()
        self.driver.find_element_by_xpath('//li[@data-id="testcase"]').click()
        self.driver.find_element_by_xpath('//a[@href="/zentao/testcase-create-1-0-0.html"]').click()
        time.sleep(2)
        # 输入信息
        a = '用例04'
        self.driver.find_element_by_xpath('//div[@id="stage_chosen"]').click()
        self.driver.find_element_by_xpath('//li[@title="单元测试阶段"]').click()
        self.driver.find_element_by_xpath('//input[@id="title"]').send_keys(a)
        self.driver.find_element_by_xpath('//textarea[@id="precondition"]').send_keys('这是前置条件')
        self.driver.find_element_by_xpath('//textarea[@name="steps[1]"]').send_keys('步骤1')
        self.driver.find_element_by_xpath('//tbody[@id="steps"]/tr[1]/td[2]/div/span/div/input').click()
        self.driver.find_element_by_xpath('//tbody[@id="steps"]/tr[2]/td[3]/textarea').send_keys('我是预期')
        self.driver.find_element_by_xpath('//tbody[@id="steps"]/tr[2]/td[4]/div/button[1]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//tbody[@id="steps"]/tr[2]/td[4]/div/button[2]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//tbody[@id="steps"]/tr[3]/td[4]/div/button[3]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//input[@id="keywords"]').send_keys('关键词')
        time.sleep(2)
        self.driver.find_element_by_xpath('//form[@id="dataform"]').submit()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH,'//td[@class="c-title text-left"]'), a))
if __name__ =='__main__':
    unittest.main()