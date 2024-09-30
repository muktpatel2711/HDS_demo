from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
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


class Test_Add_person:
    def __init__(self):
        self.login_test =Test_login()

    def test_add_person(self):
        driver =self.login_test.test_login_authorization()
        driver.find_element(By.XPATH,"//span[text()='Manage Person']").click()
        driver.find_element(By.XPATH, "//span[text()='Add Person']").click()


        print("person_add")
        driver.quit()

if __name__ =="__main__":
    test_add =Test_Add_person()
    test_add.test_add_person()





