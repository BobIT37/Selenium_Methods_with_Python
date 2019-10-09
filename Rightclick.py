from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")

action = ActionChains(driver)
action.context_click(driver.find_element_by_xpath("//span[text()='right click me']")).perform()
sleep(3)

driver.find_element_by_xpath("//ul[@class='context-menu-list context-menu-root']/li[3]").click()
sleep(2)

obj = driver.switch_to.alert
msg = obj.text
print(msg)
sleep(2)
obj.accept()