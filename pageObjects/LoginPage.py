from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities import elements

class Loginpage:

    def __init__(self,driver):
        self.driver = driver

    def EnterUserName(self):
        self.driver.find_element(By.NAME, elements.username_id).send_keys(elements.user_name)

    def EnterPassword(self):
        self.driver.find_element(By.NAME, elements.password_id).send_keys(elements.password)

    def submit(self):
        self.driver.find_element(By.NAME, elements.sign_in_xpath).click()