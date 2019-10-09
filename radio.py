from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://toolsqa.com/automation-practice-form/")

driver.find_element_by_xpath("//input[@value='Female']").click()

sleep(5)

driver.find_element_by_xpath("//input[@value='Selenium Webdriver']").click()

sleep(5)
