from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pytest

chrome_options=ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

firefox_options = FirefoxOptions()
firefox_options.add_argument("--headless")

Browser = {
    "Chrome","Firefox"
}
class Test_Browser:
   def test_cross_browser(self):
        for browser in Browser:
            if browser=="Chrome":
                driver = webdriver.Chrome(service=Service(),options=chrome_options)
                print(f"An Application works on {browser}")
                driver.close()
            elif browser=="Firefox":
                driver =webdriver.Firefox(service=FirefoxService(),options=firefox_options)
                print(f"An Application works on {browser}")
                driver.close()
browser =Test_Browser()
browser.test_cross_browser()

