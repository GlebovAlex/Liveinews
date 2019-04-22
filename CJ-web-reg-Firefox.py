import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select



class Registration(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox(executable_path="geckodriver")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://liveinews.com/login/")

    def test_web_registeration(self):
        # enter the registration details
        select_role = Select(self.driver.find_element_by_id("i-e-type"))
        select_role.select_by_visible_text("Citizen Journalist")
        self.driver.find_element_by_id("i-e-name").send_keys("u3.qallab")
        self.driver.find_element_by_id("reg_password").send_keys("Test@1234")
        self.driver.find_element_by_id("reg_email").send_keys("u3.qallab@gmail.com")
        self.driver.find_element_by_id("creg_password").send_keys("Test@1234")
        self.driver.find_element_by_id("i-e-name").send_keys("u3.qallab")
        self.driver.find_element_by_id("i-e-first").send_keys("u3")
        self.driver.find_element_by_id("i-e-last").send_keys("qallab")
        self.driver.find_element_by_id("i-e-address").send_keys("123 apt 123")
        self.driver.find_element_by_id("i-e-phone").send_keys("123-456-7890")
        self.driver.find_element_by_id("i-e-zip").send_keys("95008")
        select_country = Select(self.driver.find_element_by_id("countryId"))
        select_country.select_by_visible_text("USA")
        select_state = Select(self.driver.find_element_by_id("stateId"))
        select_state.select_by_visible_text("California")
        select_city = Select(self.driver.find_element_by_id("cityId"))
        select_city.select_by_visible_text("San Jose, Santa Clara County")
        self.driver.find_element_by_id("i-e-paypal").send_keys("u3.qallab@gmail.com")
        self.driver.find_element_by_name("register").click()
        time.sleep(5)
        self.driver.find_element_by_id("acceptterms").click()
        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Terms of Service'])[1]/following::span[1]").click()
        self.driver.find_element_by_name("wp-submit").click()
        time.sleep(5)

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()