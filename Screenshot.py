from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://toolsqa.com/automation-practice-form/")

directory = "C:\\Users\\vikky\\PycharmProjects\\SeleniumTest\\Screenshot1.png"
driver.get_screenshot_as_file(directory)