from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.guru99.com/test/drag_drop.html")

drag = driver.find_element_by_id("fourth")
sleep(2)
drop = driver.find_element_by_id("amt7")
sleep(2)

action = ActionChains(driver)
action.drag_and_drop(drag,drop).perform()




