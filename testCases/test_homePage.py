import pytest
from pageObjects.HomePage import HomePage
from utilities import elements
import os

class TestHomePage:
    baseURl =elements.url

    @pytest.mark.sanity
    def test_homePage(self,setup):
        self.driver =setup
        self.driver.get(self.baseURl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.baps_sso =HomePage(self.driver)
        self.baps_sso.Login_withSSo()



