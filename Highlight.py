from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")

element = driver.find_element_by_name("firstname")

driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",element,"background: yellow; border: 3px solid red;")
