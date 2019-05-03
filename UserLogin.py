import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class UserLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(executable_path='/Users/magdalena/Desktop/python_automation/chromedriver')
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








