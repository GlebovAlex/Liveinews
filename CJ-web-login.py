import unittest
import time
from selenium import webdriver


class Login(unittest.TestCase):
    def setUp(self):
        # create a new Chrome session
        global driver
        options = Options()
        options.headless = True
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.binary_location = '/usr/bin/google-chrome'
        driver = webdriver.Chrome(options=options, executable_path='/usr/bin/chromedriver')
        driver.implicitly_wait(30)
        driver.maximize_window()
        # navigate to the application home page
        driver.get("http://liveinews.com/login/")

    def test_cred_login(self):
        #login to the LIVEiNEWS url
        driver.find_element_by_name('log').send_keys('u3.qallab')
        driver.find_element_by_name('pwd').send_keys('Test@1234')
        driver.find_element_by_name("wp-submit").click()
        time.sleep(4)

    def tearDown(self):
        # close the browser window
        driver.quit()

if __name__ == '__main__':
    unittest.main()


