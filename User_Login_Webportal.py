#!/usr/bin/python3
import json
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
serverUrl = "http://liveinews.com/login/"
class LoginUser(unittest.TestCase):
    def setUp(self):
        global options
        options = Options()
        options.headless = True
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.binary_location = '/usr/bin/google-chrome'
    def test_login(self):
        with open('LoginData.json') as LoginData:
            data = json.load(LoginData)
            for user in data['users']:
                try:
                    driver = webdriver.Chrome(options=options, executable_path='/usr/bin/chromedriver')
                    #driver = webdriver.Chrome(executable_path='chromedriver.exe')
                    driver.get(serverUrl)
                    driver.maximize_window()
                    WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@name='log']")).send_keys(user['Username'])
                    WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@type='password']")).send_keys(user['Password'])
                    driver.find_element_by_xpath("//button[@name='wp-submit']").click()
                    print(user['Username']+" logged into the webpage successfully")
                    driver.quit()
                except Exception as e:
                    print(user['Username']+"cannot login into the webpage due to the error"+e)
    def tearDown(self):
        print("------------End of Login Test script execution-------------")
if __name__ == "__main__":
   unittest.main()

                


