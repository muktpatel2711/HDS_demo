import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.baps.org/")
driver.maximize_window()
driver.implicitly_wait(10)

time.sleep(10000000)

