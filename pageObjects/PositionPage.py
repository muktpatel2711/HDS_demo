from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities import elements
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



class PositionPage():

    def __init__(self,driver):
        self.driver = driver


    def select_position(self):
        self.driver.find_element(By.XPATH,elements.select_pisition_xpath).click()
        drop_down  = self.driver.find_element(By.XPATH,elements.enter_position_name_xpath)
        drop_down.send_keys("System Admin 8")
        name= self.driver.find_element(By.XPATH,elements.select_name)
        action = ActionChains(self.driver)
        action.click(name).click().perform()
        self.driver.find_element(By.XPATH,elements.continue_button_xpath).click()
        self.driver.find_element(By.ID,elements.user_manu_id).click()

    def confirmationmsg(self):
        try:
            self.driver.find_element(By.XPATH,elements.user).text
            return
        except:
            None











