import pytest
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import Loginpage
from utilities import elements

import os
class TestHomepage:
    baseURl = elements.url

    @pytest.fixture(autouse=True)
    def setup_home_page(self, setup):
        """Fixture to set up the homepage before tests."""
        self.driver = setup
        self.driver.get(self.baseURl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.baps_sso = HomePage(self.driver)
        self.baps_sso.Login_withSSo()

    class TestLogin:
        @pytest.mark.sanity
        def test_login(self, setup):
            self.driver = setup  # Use the same driver
            self.login = Loginpage(self.driver)
            # Perform login actions
            self.login.EnterUserName()
            self.login.EnterPassword()
            self.login.submit()



