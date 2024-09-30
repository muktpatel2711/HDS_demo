import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pytest
from test_login import Test_login

chrome_options=ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

firefox_options = FirefoxOptions()
firefox_options.add_argument("--headless")


class Test_serach_business:
    def __init__(self):
        self.login_test =Test_login()

    def test_search_business(self):
        driver =self.login_test.test_login_authorization()
        driver.implicitly_wait(50)
        driver.find_element(By.XPATH,"//span[text()='Manage Business']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[text()='Search Business']").click()
        driver.find_element(By.XPATH,"//button[text()='Search']").click()
        page_no = driver.find_element(By.XPATH, "//span[text()='10']")
        page_no_text=page_no.text
        assert page_no_text=="10"
        pass
        print("A business works fine")
        driver.quit()

if __name__ =="__main__":
    test_business=Test_serach_business()
    test_business.test_search_business()




