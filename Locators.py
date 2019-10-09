from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://toolsqa.com/automation-practice-form/")
sleep(3)

#By id
driver.find_element_by_id("profession-0").click()
sleep(2)

#By name
driver.find_element_by_name("firstname").send_keys("Python")
sleep(2)

#By linktext
driver.find_element_by_link_text("Link Test").click()
sleep(2)

#By partial linktext
driver.find_element_by_partial_link_text("Partial Link").click()
sleep(2)

#By tag name
#driver.find_element_by_tag_name("select")
#sleep(2)

#By class name
#driver.find_element_by_class_name("radio").click()
#sleep(2)

#By css selector
#driver.find_element_by_css_selector("input[name='lastname']").send_keys("selenium")
#sleep(2)

#By xpath
#driver.find_element_by_xpath("//input[@value='Selenium Webdriver']").click()
#sleep(2)