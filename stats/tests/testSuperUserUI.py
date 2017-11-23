from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class SuperUserUI(unittest.TestCase):
    def setUp(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', "text/csv")

        self.selenium = webdriver.Firefox(profile)
        #self.selenium = webdriver.Firefox()

    def test_get_standard_csv_file(self):
        self.check_login_stats()
        self.selenium.implicitly_wait(10)
        self.selenium.find_element_by_name("csv_export_button").click()

    def test_get_european_csv_file(self):
        self.check_login_stats()
        self.selenium.implicitly_wait(10)
        list = self.selenium.find_elements_by_name("csv_type")
        list[1].click()
        #self.selenium.find_element_by_xpath("//input[value='euro']").click()
        self.selenium.find_element_by_name("csv_export_button").click()

    def check_login_stats(self):
        self.go_to_super_user_template()
        # login stats checkbox
        self.selenium.find_element_by_name("loginStats").click()
        # check some user types
        self.selenium.find_element_by_name("professor").click()
        self.selenium.find_element_by_name("admin").click()

        #TODO Months increase by 1 and days decrease by 1
        self.selenium.execute_script("document.getElementById('startDateLS').valueAsDate = new Date(2017, 10, 02);")
        self.selenium.execute_script("document.getElementById('endDateLS').valueAsDate = new Date(2017, 10, 23);")

        time.sleep(2)

        # using the JavaScriptExecutor to scroll down to bottom of window
        self.selenium.implicitly_wait(30)
        self.selenium.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def go_to_super_user_template(self):
        #it's necessary to login as professor
        #use a existing login and password
        self.selenium.get("http://127.0.0.1:8000/accounts/usernamelogin/")
        self.selenium.find_element_by_id("id_username").click()
        self.selenium.find_element_by_id("id_username").clear()
        self.selenium.find_element_by_id("id_username").send_keys("aude.oscar")
        self.selenium.find_element_by_css_selector("input.btn.btn-primary").click()
        self.selenium.find_element_by_id("id_password").click()
        self.selenium.find_element_by_id("id_password").clear()
        self.selenium.find_element_by_id("id_password").send_keys("oscar")
        self.selenium.find_element_by_css_selector("input.btn.btn-primary").click()
        self.selenium.get("http://127.0.0.1:8000/stats/superuser/")

if __name__ == "__main__":
    unittest.main()