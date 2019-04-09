from selenium import webdriver
import unittest


class LoginORM(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(" Open Application")
        cls.driver = webdriver.Chrome(executable_path='/Library/Python/2.7/site-packages/chromedriver')

        cls.driver.get("https://opensource-demo.orangehrmlive.com/")

    def test_InValid_Login(self):
        self.driver.find_element_by_id("txtUsername").clear()
        self.driver.find_element_by_id("txtPassword").clear()
        self.driver.find_element_by_id("txtUsername").send_keys("admin123")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()

        ErrorText = self.driver.find_element_by_id("spanMessage")
        self.assertEqual(ErrorText.text, "Invalid credentials")

    def test_InvalidUsername_passwrod(self):
        self.driver.find_element_by_id("txtUsername").clear()
        self.driver.find_element_by_id("txtPassword").clear()
        self.driver.find_element_by_id("txtUsername").send_keys("admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin")
        self.driver.find_element_by_id("btnLogin").click()

        ErrorText1 = self.driver.find_element_by_id("spanMessage")
        self.assertEqual(ErrorText1.text, "Invalid credentials")

    def test_InvalidUsername_Correct_passwrod(self):
        self.driver.find_element_by_id("txtUsername").clear()
        self.driver.find_element_by_id("txtPassword").clear()
        self.driver.find_element_by_id("txtUsername").send_keys("admin123")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()

        ErrorText4 = self.driver.find_element_by_id("spanMessage")
        self.assertEqual(ErrorText4.text, "Invalid credentials")

    def test_Nousername_password(self):
        self.driver.find_element_by_id("txtUsername").clear()
        self.driver.find_element_by_id("txtPassword").clear()
        self.driver.find_element_by_id("btnLogin").click()

        ErrorText2 = self.driver.find_element_by_id("spanMessage")
        self.assertEqual(ErrorText2.text, "Username cannot be empty")

    def test_Valid_Login(self):
        self.driver.find_element_by_id("txtUsername").send_keys("admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()

    def test_Verify_title(self):
        PageTitle = self.driver.title
        self.assertEqual(PageTitle, "OrangeHRM", " Title not match")
        print(PageTitle)
        self.driver.implicitly_wait(4000)


    def test_Logout_Page(self):
        print("Reached..!!!")
        self.driver.find_element_by_xpath("//a[@id='welcome']").click()
        self.driver.find_element_by_xpath("//a[@href='/index.php/auth/logout']").click()

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        print("Close Application")


if __name__ == "__main__":
    unittest.main()
