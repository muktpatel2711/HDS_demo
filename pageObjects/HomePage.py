from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities import elements


class HomePage():

    def __init__(self,driver):
        self.driver = driver


    def Login_withSSo(self):
        self.driver.find_element(By.NAME,elements.login_button_name).click()








