import time

import pytest

from pageObjects.loginPage import LoginPage
from pageObjects.HomePage import HomePage
from pageObjects.PositionPage import PositionPage
from utilities import elements
import os
@pytest.mark.regression
class Test_001_LoginSSO:
    baseURl =elements.url

    def test_sso_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.baps_sso=HomePage(self.driver)
        self.baps_sso.Login_withSSo()
        self.login=LoginPage(self.driver)
        self.login.Enter_username()
        self.login.Enter_password()
        self.login.clickOnSign()
        self.position =PositionPage(self.driver)
        self.position.select_position()
        self.driver.save_screenshot(os.path.abspath(os.curdir)+"//screenShorts//"+"login.png")
        self.userName =self.position.confirmationmsg()
        if self.userName=="manish Patel1":
            assert True
        else:
            assert False
        self.driver.close()
