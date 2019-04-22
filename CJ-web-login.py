import unittest
import time
from selenium import webdriver


class Login(unittest.TestCase):
    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome(executable_path="chromedriver")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://liveinews.com/login/")

    def test_cred_login(self):
        #login to the LIVEiNEWS url
        self.driver.find_element_by_name('log').send_keys('u3.qallab')
        self.driver.find_element_by_name('pwd').send_keys('Test@1234')
        self.driver.find_element_by_name("wp-submit").click()
        time.sleep(4)

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


