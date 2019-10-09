from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://newtours.demoaut.com/")

driver.find_element_by_xpath("//a[text()='REGISTER']").click()
sleep(3)
driver.find_element_by_name("firstName").send_keys("python")
driver.find_element_by_name("lastName").send_keys("selenium")
driver.find_element_by_name("phone").send_keys("1234567890")
driver.find_element_by_id("userName").send_keys("python@selenium.com")
sleep(3)

driver.find_element_by_name("address1").send_keys("main road")
driver.find_element_by_name("city").send_keys("Bengaluru")
driver.find_element_by_name("state").send_keys("Karnataka")
sleep(3)

select = Select(driver.find_element_by_name("country"))
select.select_by_visible_text("INDIA ")
sleep(3)

driver.find_element_by_name("email").send_keys("python")
driver.find_element_by_name("password").send_keys("selenium")
driver.find_element_by_name("confirmPassword").send_keys("selenium")
sleep(3)

driver.find_element_by_name("register").click()
sleep(5)


#driver.quit()