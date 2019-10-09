from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.com/")
sleep(5)

driver.find_element_by_xpath("//button[text()='✕']").click()
sleep(3)

action = ActionChains(driver)
action.move_to_element(driver.find_element_by_xpath("(//span[@class='_1QZ6fC _3Lgyp8'])[1]")).perform()
sleep(3)

driver.find_element_by_xpath("//a[text()='Samsung']").click()