from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://toolsqa.com/automation-practice-form/")

if (driver.find_element_by_id("tool-1").is_displayed()):
    print("Element is displayed")
    driver.find_element_by_id("tool-1").click()
    sleep(3)

if (driver.find_element_by_id("tool-1").is_selected()):
    print("Checkbox element is selected")
    driver.find_element_by_id("tool-1").click()

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_button_disabled")

sleep(2)
driver.switch_to.frame("iframeResult")
sleep(2)
ele = driver.find_element_by_xpath("//button[text()='Click Me!']").is_enabled()
print("Element is Enabled : ",ele)