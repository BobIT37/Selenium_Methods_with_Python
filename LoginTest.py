from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://newtours.demoaut.com/")

driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")
driver.find_element_by_name("login").click()

sleep(5)

driver.quit()