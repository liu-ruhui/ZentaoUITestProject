from selenium.webdriver.common.by import By
import time
def exit(driver):
     time.sleep(2)
     driver.find_element(By.XPATH,'//a[@class="dropdown-toggle"]').click()
     driver.find_element(By.XPATH,'//a[@href="/zentao/user-logout.html"]').click()
