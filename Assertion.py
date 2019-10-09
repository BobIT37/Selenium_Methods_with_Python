import unittest
from selenium import webdriver

class AssertTest(unittest.TestCase):
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("http://newtours.demoaut.com/")

    def test1(self):
        actualTitle = self.driver.title
        expectedTitle = "Welcome: Mercury Tours"
        self.assertEqual(actualTitle,expectedTitle)
        #self.assertNotEqual(actualTitle,expectedTitle)
        print("Title is:", actualTitle)
        self.assertTrue(self.driver.find_element_by_name("userName").is_displayed())
        print("Username field is displayed")
        #self.assertFalse(self.driver.find_element_by_name("userName").is_displayed())
        print("Username field is not displayed")

        self.assertIn("Welcome", expectedTitle)
        print("Welcome is present")
        #self.assertNotIn("Python", expectedTitle)



if __name__ == "__main__":
    unittest.main()