from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
# driver.get("http:www.google.com")
#
# driver.find_element_by_name("q").send_keys("Python")
# sleep(2)
# driver.find_element_by_name("q").send_keys(Keys.ARROW_DOWN)
# sleep(2)
# driver.find_element_by_name("q").send_keys(Keys.ARROW_DOWN)
# sleep(2)
# driver.find_element_by_name("q").send_keys(Keys.ENTER)


#Copy and Paste using Keyboard operations
driver.get("http://www.teachmeselenium.com/automation-practice")

driver.find_element_by_id("firstname").send_keys("Python")
sleep(3)
driver.find_element_by_id("firstname").send_keys(Keys.CONTROL,"a")
sleep(2)
driver.find_element_by_id("firstname").send_keys(Keys.CONTROL,"c")
sleep(2)
driver.find_element_by_class_name("lastname").send_keys(Keys.CONTROL,"v")