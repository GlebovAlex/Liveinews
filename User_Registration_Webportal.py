#!/usr/bin/python3
import json
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
serverUrl = "http://liveinews.com/login/"
class RegisterUser(unittest.TestCase):
    def setUp(self):
        global options
        options = Options()
        options.headless = True
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.binary_location = '/usr/bin/google-chrome'
    def test_register(self):
        with open('LoginData.json') as RegisterData:
            data = json.load(RegisterData)
            for users in data['new_users']:
                try:
                    driver = webdriver.Chrome(options=options, executable_path='/usr/bin/chromedriver')
                    #driver = webdriver.Chrome(executable_path='chromedriver.exe')
                    driver.get(serverUrl)
                    driver.maximize_window()
                    accounttypelocator = "select#i-e-type option[value='user']"
                    WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(accounttypelocator))
                    WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@type='email']")).send_keys(users['EmailAddress'])
                    WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@name='password']")).send_keys(users['Password'])
                    WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@name='confirm_password']")).send_keys(users['Confirm password'])
                    WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@name='login']")).send_keys(users['Username'])
                    element_submit = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@name='register']"))
                    ActionChains(driver).move_to_element(element_submit).click().perform()
                    driver.switch_to.window(driver.window_handles[-1])
                    element_accept = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id('acceptterms'))
                    ActionChains(driver).move_to_element(element_accept).perform()
                    element_accept.send_keys(Keys.END)
                    time.sleep(1)
                    element_acc =driver.find_element_by_id("acceptterms")
                    ActionChains(driver).move_to_element(element_acc).click().perform()
                    time.sleep(1)
                    element_term = driver.find_element_by_xpath("//span[@class='btn btn-default']")
                    ActionChains(driver).move_to_element(element_term).click(element_term).perform()
                    time.sleep(1)
                    element_finalsubmit =  driver.find_element_by_xpath("//input[@name='register']")
                    ActionChains(driver).move_to_element(element_finalsubmit).click().perform()
                    print(users['Username']+" registered successfully")
                    time.sleep(4)
                    error = driver.find_element_by_xpath("//p[@class='errors-p']")
                    if error:
                        print(error.text)
                except Exception as e:
                    print(users['Username'] + " cannot register successfully due to the error")
                    print(e)

    def tearDown(self):

        print("------------End of Registration  Test script execution-------------")

if __name__ == "__main__":
    unittest.main()