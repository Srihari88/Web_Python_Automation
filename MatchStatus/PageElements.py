from selenium import webdriver
import unittest


class HomePageElements(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Open Application")
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://opensource-demo.orangehrmlive.com")

    def test_password_textVerification(self):
        Credential = self.driver.find_element_by_xpath(
            "//span[contains(text(),'( Username : Admin | Password : admin123 )')]")
        print(Credential.text)
        self.assertEqual(Credential.text, "( Username : Admin | Password : admin123 )")

    def text_link(self):
        Link = self.driver.find_element_by_xpath("//a[@href='http://www.orangehrm.com']")
        print(Link.text)
        self.assertEqual(Link.text, "http://www.orangehrm.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print(" Close Application")


if __name__ == "__main__":
    unittest.main()
