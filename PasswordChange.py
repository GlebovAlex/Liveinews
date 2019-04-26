import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PasswordChange(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(executable_path='/Users/magdalena/Desktop/python_automation/chromedriver')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://liveinews.com/login/")

    def test_password_change(self):
        self.driver.find_element_by_name("log").send_keys("u1qallab")
        self.driver.find_element_by_name("pwd").send_keys("u1qallab")
        self.driver.find_element_by_name("wp-submit").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("old_pass").send_keys("u1qallab")
        self.driver.find_element_by_id("new_pass").send_keys("qallab")
        self.driver.find_element_by_id("repeat_pass").send_keys("qallab")
        '''
        element_accept = driver.find_element_by_id('acceptterms')
       actions_accept = ActionChains(driver)
       actions_accept.move_to_element(element_accept).perform()
       element_accept.send_keys(Keys.END)

        from selenium.webdriver.common.action_chains import ActionChains
        
        '''
        self.driver.find_element_by_xpath("//*[@id='save_pass']")
        self.driver.find_element_by_xpath("//*[@id='save_pass']/div[4]/div/button").click()


def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()








