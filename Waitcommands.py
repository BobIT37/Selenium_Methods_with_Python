from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://newtours.demoaut.com/")

#Implicit Wait
driver.implicitly_wait(20)

#Explicit wait

WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.NAME, "userName")))
driver.find_element_by_name("userName").send_keys("mercury")
WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='password']")))
driver.find_element_by_name("password").send_keys("mercury")
WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.NAME, "login")))
driver.find_element_by_name("login").click()


#driver.get("file:///C:/Users/vikky/OneDrive/Desktop/SimpleAlert.html")
#driver.find_element_by_xpath("//button[text()=' Create Alert']").click()
#WebDriverWait(driver,10).until(expected_conditions.alert_is_present())
#driver.switch_to.alert.accept()