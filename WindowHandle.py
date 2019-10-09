from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.quackit.com/html/codes/html_popup_window_code.cfm")
print(driver.title)

sleep(3)
driver.switch_to.frame("result1")

sleep(3)
driver.find_element_by_xpath("//a[text()='Open a popup window']").click()

sleep(3)
handels = driver.window_handles
size = len(handels)
print(size)

sleep(3)
for x in range(size):
    if(handels[x] != driver.current_window_handle):
        driver.switch_to.window(handels[x])
        print(driver.title)
        sleep(3)
        driver.find_element_by_xpath("//a[text()='Close']").click()
