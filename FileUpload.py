from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://toolsqa.com/automation-practice-form/")

driver.find_element_by_name("photo").click()
sleep(3)

os.system("C:\\Users\\vikky\\OneDrive\\Desktop\\Java\\FileUpload.exe")