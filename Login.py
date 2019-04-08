import time
from selenium import webdriver

appBusURL = 'https://dev.e-dapt.net:5554/edapt-admin/login.jsp'
try:

    driver = webdriver.Chrome(executable_path="chromedriver")
    driver.get(appBusURL)

    driver.find_element_by_xpath("//input[@name ='username']").send_keys('edapt-setup')
    driver.find_element_by_xpath("//input[@name = 'password']").send_keys('511maps')
    driver.find_element_by_xpath("//input[@value='Login']").click()
    time.sleep(10)
    driver.quit()
except Exception as e:
    print("Exception Occured",e)





