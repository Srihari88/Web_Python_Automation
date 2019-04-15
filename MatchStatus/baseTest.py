from selenium import webdriver
import unittest
import time


class basTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        driver = webdriver.Chrome(executable_path='/Library/Python/2.7/site-packages/chromedriver')
        driver.get("https://opensource-demo.orangehrmlive.com")

    def test_Basetest(self):
        driver.find_element_by_id("txtUsername").send_keys("admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        print("Base Application started")


if __name__ == '__main__':
    unittest.main()
