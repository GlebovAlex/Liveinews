#!/usr/bin/python3
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
class Registration(unittest.TestCase):
    def setUp(self):
        global driver
        options = Options()
        options.headless = True
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.binary_location = '/usr/bin/google-chrome'
        driver = webdriver.Chrome(options=options, executable_path='/usr/bin/chromedriver')
        #driver = webdriver.Chrome(executable_path='chromedriver.exe')
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://liveinews.com/login/")

    def test_web_registeration(self):
        # enter the registration details
        select_role = Select(driver.find_element_by_id("i-e-type"))
        select_role.select_by_visible_text("Citizen Journalist")
        driver.find_element_by_id("i-e-name").send_keys("u3.qallab")
        driver.find_element_by_id("reg_password").send_keys("Test@1234")
        driver.find_element_by_id("reg_email").send_keys("u3.qallab@gmail.com")
        driver.find_element_by_id("creg_password").send_keys("Test@1234")
        driver.find_element_by_id("i-e-name").send_keys("u3.qallab")
        driver.find_element_by_id("i-e-first").send_keys("u3")
        driver.find_element_by_id("i-e-last").send_keys("qallab")
        driver.find_element_by_id("i-e-address").send_keys("123 apt 123")
        driver.find_element_by_id("i-e-phone").send_keys("123-456-7890")
        driver.find_element_by_id("i-e-zip").send_keys("95008")
        select_country = Select(driver.find_element_by_id("countryId"))
        select_country.select_by_visible_text("USA")
        select_state = Select(driver.find_element_by_id("stateId"))
        select_state.select_by_visible_text("California")
        select_city = Select(driver.find_element_by_id("cityId"))
        select_city.select_by_visible_text("San Jose, Santa Clara County")
        driver.find_element_by_id("i-e-paypal").send_keys("u3.qallab@gmail.com")
        elementsubmit = driver.find_element_by_xpath('//input[@type="submit"]')
        actions = ActionChains(driver)
        actions.move_to_element(elementsubmit).click().perform()
        element_accept = driver.find_element_by_id('acceptterms')
        actions_accept = ActionChains(driver)
        actions_accept.move_to_element(element_accept).perform()
        element_accept.send_keys(Keys.END)
        #element_accept.click()
        time.sleep(4)
        element_acc=driver.find_element_by_id("acceptterms")
        actions_acc=ActionChains(driver)
        actions_acc.move_to_element(element_acc).click().perform()
        element_term =driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Terms of Service'])[1]/following::span[1]")
        actions_term=ActionChains(driver)
        actions_term.move_to_element(element_term).click().perform()
        time.sleep(4)
        element_submit = driver.find_element_by_xpath("//input[@name='register']")
        actions_submit = ActionChains(driver)
        actions_submit.move_to_element(element_submit).click().perform()
        time.sleep(4)


        def tearDown(self):
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()