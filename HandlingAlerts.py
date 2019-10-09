from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
#driver.get("file:///C:/Users/vikky/OneDrive/Desktop/Java/SimpleAlert.html")

#Handling Simple Alert
driver.find_element_by_xpath("//button[text()=' Create Alert']").click()
sleep(2)

#Getting text of the Alert pop up
obj = driver.switch_to.alert
msg = obj.text
print(msg)
driver.switch_to.alert.accept()


#Handling Confirmation Alert
driver.get("file:///C:/Users/vikky/OneDrive/Desktop/Java/confirmation.html")
sleep(2)

driver.find_element_by_xpath("//button[text()=' Create Alert']").click()
sleep(2)

#Accepting Alert
driver.switch_to.alert.accept()
sleep(2)

driver.find_element_by_xpath("//button[text()=' Create Alert']").click()
sleep(2)
#Dismissing Alert
driver.switch_to.alert.dismiss()

#Handling Prompt Alert
#driver.get("file:///C:/Users/vikky/OneDrive/Desktop/Java/prompt_alert.html")


#obj = driver.switch_to.alert
#obj.send_keys('python')
#sleep(3)

#obj.accept()
#msg = obj.text
#print(msg)
#sleep(2)

#obj.accept()

