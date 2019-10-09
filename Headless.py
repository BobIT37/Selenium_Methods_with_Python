from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options1 = Options()
chrome_options1.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options1)
driver.maximize_window()
driver.get("http://toolsqa.com/automation-practice-form/")

if (driver.find_element_by_id("tool-1").is_displayed()):
    print("Element is displayed")
    driver.find_element_by_id("tool-1").click()
    sleep(3)

if (driver.find_element_by_id("tool-1").is_selected()):
    print("Checkbox element is selected")
    driver.find_element_by_id("tool-1").click()