import unittest
from selenium import webdriver
from time import sleep

class testing(unittest.TestCase):
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("http://newtours.demoaut.com/")

    def test_login(self):
        self.driver.find_element_by_name("userName").send_keys("mercury")
        self.driver.find_element_by_name("password").send_keys("mercury")
        self.driver.find_element_by_name("login").click()
        sleep(3)

    def test_title(self):
        title = self.driver.title
        print(title)

    def test_abc(self):
        self.driver.find_element_by_xpath("//a[text()='Hotels']").click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[text()='Home']").click()

if __name__ == '__main__':
    unittest.main()