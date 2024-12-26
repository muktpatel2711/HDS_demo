import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


class Test_verify_ChekBox_On_editRole:
    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()

    def test_url(self):
        self.driver.get("https://qa.baps.dev/mis")
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
        self.driver.find_element(By.XPATH,"(//button[text()='Search'])[1]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"(//button[@class='single-icon mr-1 ng-star-inserted'])[1]").click()
        seva_email =self.driver.find_element(By.XPATH,"(//div[@class='mat-checkbox-inner-container'])[6]")
        if seva_email.is_enabled():
            print("Exclude Seva Title from M365 Profile is available on role_edit page and it's not marked")
        else:
            print("Exclude Seva Title from M365 Profile is not available on role_edit page ")

