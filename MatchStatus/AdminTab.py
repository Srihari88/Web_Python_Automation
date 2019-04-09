from selenium import webdriver
import unittest


class AdminTab(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(" Open Application")
        cls.driver = webdriver.Chrome(executable_path='/Library/Python/2.7/site-packages/chromedriver')

        cls.driver.get("https://opensource-demo.orangehrmlive.com/")
    def test_Valid_Login(self):
        self.driver.find_element_by_id("txtUsername").send_keys("admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        self.driver.implicitly_wait(5000)
        self.driver.find_element_by_id("menu_admin_viewAdminModule").click()


    def test_AdminTab(self):
        print("Hello")

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        print("Close Application")


if __name__ == "__main__":
    unittest.main()
