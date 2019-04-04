from selenium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains


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

    def test_Directory_Link(self):
        action = ActionChains(self.driver);

        DirectoryText = self.driver.find_element_by_xpath("//a[@id='menu_directory_viewDirectory']")
        action.move_to_element(DirectoryText).perform().click()
        # DirectoryText.click()
        Url = self.driver.current_url
        print(self.driver.current_url)
        self.assertEqual(Url, "https://opensource-demo.orangehrmlive.com/index.php/directory/viewDirectory/reset/1")
