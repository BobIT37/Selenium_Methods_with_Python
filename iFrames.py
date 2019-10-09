from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://toolsqa.com/iframe-practice-page/")

#Switching to iframe
sleep(5)
driver.switch_to.frame("iframe2")

sleep(3)
driver.find_element_by_xpath("//a[text()='Sortable']").click()


#Switching back to main window
sleep(3)
driver.switch_to.default_content()
#driver.find_element_by_xpath("//a[text()='Home']").click()

