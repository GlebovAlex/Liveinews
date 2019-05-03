#!/usr/bin/python3
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class UserLogin(unittest.TestCase):
    def setUp(self):
        global options
        options = Options()
        options.headless = True
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.binary_location = '/usr/bin/google-chrome'

        driver = webdriver.Chrome(options=options, executable_path='/usr/bin/chromedriver')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://liveinews.com/login/")

    def test_password_change(self):
        self.driver.find_element_by_name("log").send_keys("u31.qallab")
        self.driver.find_element_by_name("pwd").send_keys("Test@1234")
        self.driver.find_element_by_name("wp-submit").click()
        self.driver.implicitly_wait(10)


    def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()








