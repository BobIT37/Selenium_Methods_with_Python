from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")
sleep(3)

selectDay = Select(driver.find_element_by_xpath("//select[@id='day']"))
#Selecting value by indexs
selectDay.select_by_index(20)
sleep(2)

selectMonth = Select(driver.find_element_by_xpath("//select[@id='month']"))
#Selecting value by visible text
selectMonth.select_by_visible_text("Jun")
sleep(2)

selectYear = Select(driver.find_element_by_xpath("//select[@id='year']"))
#Selecting value by value
selectYear.select_by_value("1990")
sleep(2)

#Printing selected options
selectedDay = selectDay.first_selected_option.get_attribute("value")
selectedMonth = selectMonth.first_selected_option.get_attribute("innerHTML")
selectedYear = selectYear.first_selected_option.get_attribute("value")

print("First Selected Day is : " +selectedDay)
print("First Selected Month is : " +selectedMonth)
print("First Selected Yesr is : " +selectedYear)

driver.quit()