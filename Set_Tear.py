import unittest
from selenium import webdriver

class login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://newtours.demoaut.com/")

    def test1_login(self):
        self.driver.find_element_by_name("userName").send_keys("mercury")
        self.driver.find_element_by_name("password").send_keys("mercury")
        self.driver.find_element_by_name("login").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()