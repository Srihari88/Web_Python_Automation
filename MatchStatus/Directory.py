from selenium import webdriver
import unittest


class Directory(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(" Open Application")
        cls.driver = webdriver.Chrome(executable_path='/Library/Python/2.7/site-packages/chromedriver')
        cls.driver.get("https://opensource-demo.orangehrmlive.com/")

    def test_Valid_Login(self):
        self.driver.find_element_by_id("txtUsername").send_keys("admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        curUrl = self.driver.current_url
        print(curUrl)
        self.driver.implicitly_wait(10000)
        # self.assertEqual(curUrl, "https://opensource-demo.orangehrmlive.com/index.php/dashboard", "Browser matched ")

    def test_Profile_Link(self):
        print("Reached..!!!")
        self.driver.find_element_by_id("welcome").click()
        self.driver.find_element_by_xpath("//a[@href='/index.php/auth/logout']").click()
        # DirectoryText.click()
        Url = self.driver.current_url
        print(Url)

    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        print("Close the Application")


if __name__ == "__main__":
    unittest.main()
