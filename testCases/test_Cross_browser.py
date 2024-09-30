from selenium import webdriver
import pytest

Browser = {
    "Chrome","Firefox"
}
class Test_Browser:
   def test_cross_browser(self):
        for browser in Browser:
            if browser=="Chrome":
                driver = webdriver.Chrome()
                print(f"An Application works on {browser}")
                driver.close()
            elif browser=="Firefox":
                driver =webdriver.Firefox()
                print(f"An Application works on {browser}")
                driver.close()
browser =Test_Browser()
browser.test_cross_browser()

