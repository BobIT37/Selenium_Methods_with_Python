import unittest
from time import sleep
from selenium import webdriver

class SkipTest(unittest.TestCase):
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("http://newtours.demoaut.com/")

    def test1_login(self):
        self.driver.find_element_by_name("userName").send_keys("mercury")
        self.driver.find_element_by_name("password").send_keys("mercury")
        self.driver.find_element_by_name("login").click()
        sleep(3)

    @unittest.skip("skip sub function")
    def test2_title(self):
        title = self.driver.title
        print(title)

if __name__ == "__main__":
    unittest.main()