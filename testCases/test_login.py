from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
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
class Test_login:
   def test_login_authorization(self):
       driver =webdriver.Chrome(service=Service(),options=chrome_options)
       driver.get("https://qa.baps.dev/mis/")
       driver.maximize_window()
       driver.implicitly_wait(10)
       driver.find_element(By.NAME,"submit").click()
       driver.find_element(By.ID,"userName").send_keys("hiteshpatel1487")
       driver.find_element(By.ID,"password").send_keys("Ims@0503")
       driver.find_element(By.XPATH,"//button[@class='btn btn-primary btn-submit']").click()
       driver.find_element(By.XPATH,"//button[text()='North America System Admin']").click()
       print("success")
       return driver




