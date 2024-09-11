from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities import elements


class LoginPage():

    def __init__(self,driver):
        self.driver = driver


    def Enter_username(self):
        self.driver.find_element(By.ID,elements.username_id).send_keys(elements.user_name)

    def Enter_password(self):
        self.driver.find_element(By.ID, elements.password_id).send_keys(elements.password)

    def clickOnSign(self):
        self.driver.find_element(By.XPATH,elements.sign_in_xpath).click()








