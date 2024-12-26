import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


class Test_verify_ChekBox_On_Role:
    def __init__(self):
        self.driver =webdriver.Chrome()

    def test_browser(self):
        self.driver.get("https://qa.baps.dev/mis")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_login(self):
        self.driver.find_element(By.NAME,"submit").click()
        self.driver.find_element(By.NAME, "userName").send_keys("hiteshpatel1487")
        self.driver.find_element(By.NAME, "password").send_keys("Ims@0503")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-submit']").click()
        self.driver.find_element(By.XPATH,"(//button[text()='North America System Admin'])[1]").click()

    def test_Manage_Karyakar(self):
        self.driver.find_element(By.XPATH,"(//span[text()='Manage Karyakar'])").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH,"(//span[text()='Role'])").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//button[@class='table-icon']").click()
        time.sleep(5)
        seva_email =self.driver.find_element(By.XPATH,"(//div[@class='mat-checkbox-inner-container'])[6]")
        if seva_email.is_enabled():
            print("Exclude Seva Title from M365 Profile is available on role page and it's not marked")
        else:
            print("Exclude Seva Title from M365 Profile is not available on role page")
