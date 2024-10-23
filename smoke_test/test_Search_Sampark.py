import time

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from smoke_test.test_login import Test_login

chrome_options=ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

firefox_options = FirefoxOptions()
firefox_options.add_argument("--headless")


class Test_serach_sampark:
    def __init__(self):
        self.login_test =Test_login()

    def test_search_sampark(self):
        driver =self.login_test.test_login_authorization()
        driver.implicitly_wait(50)
        driver.find_element(By.XPATH,"//span[text()='Manage Sampark']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[text()='Sampark Karyakar']").click()
        driver.find_element(By.XPATH,"//button[text()=' Search ']").click()
        pagr_no =driver.find_element(By.XPATH,"//span[text()='10']")
        page_no_text=pagr_no.text
        assert page_no_text=="10"
        pass
        print("seach_sampark works fine")
        driver.quit()

if __name__ =="__main__":
    test_search =Test_serach_sampark()
    test_search.test_search_sampark()





