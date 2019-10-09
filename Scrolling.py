from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://toolsqa.com/automation-practice-form/")
sleep(3)

#Scrolling to the bottom of the page
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#Scrolling to perticular section of the page
#element = driver.find_element_by_xpath("//input[@value='Automation Tester']")
#sleep(2)
#driver.execute_script("return arguments[0].scrollIntoView();", element)
#sleep(2)
#element.click()

#Scrolling by pixel
driver.execute_script("window.scrollBy(0, 800);")