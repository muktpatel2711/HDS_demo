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


class Test_serach_reports:
    def __init__(self):
        self.login_test =Test_login()

    def test_search_report(self):
        driver =self.login_test.test_login_authorization()
        driver.implicitly_wait(50)
        driver.find_element(By.XPATH,"//span[text()='Reports']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[@class='ng-arrow-wrapper']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//span[text()='Person Report']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"(//span[@class='ng-arrow-wrapper'])[2]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[text()='Satsang Network']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"(//span[@class='ng-arrow-wrapper'])[3]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[text()='Center']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//button[text()=' Search ']").click()
        time.sleep(2)
        pagr_no =driver.find_element(By.XPATH,"//span[text()='10']")
        page_no_text=pagr_no.text
        assert page_no_text=="10"
        pass
        print("A person reports works fine")
        driver.quit()

if __name__ =="__main__":
    test_report =Test_serach_reports()
    test_report.test_search_report()




