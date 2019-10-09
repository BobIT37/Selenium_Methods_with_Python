from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import TimeoutException

try:
    driver = webdriver.Chrome()
except WebDriverException:
    print("Driver not found")

driver.maximize_window()
driver.get("file:///C:/Users/vikky/OneDrive/Desktop/Java/SimpleAlert.html")

try:
    driver.find_element_by_xpath("//button[text()=' Create Alrt']").click()

except NoSuchElementException as exception:
    print ("Element not found and test failed", exception)

try:
    #driver.find_element_by_xpath("//button[text()=' Create Alert']").click()
    driver.switch_to.alert

except NoAlertPresentException as NoAlertPresent:
    print("Alert not found", NoAlertPresent)

try:
    driver.switch_to.frame("id")
except NoSuchFrameException as NoFrameException:
    print("Frame not found", NoFrameException)

try:
    driver.set_page_load_timeout(1)
    driver.get("http://www.google.com")
except TimeoutException as TimeOut:
    print("webpage timed out", TimeOut)



