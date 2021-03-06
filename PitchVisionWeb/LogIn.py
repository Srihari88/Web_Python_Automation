from selenium import webdriver
import unittest


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://www.pitchvision.com/#/login")

    def test_login_valid(self):
        # driver.find_element_by_xpath("//*[@id='page']/header/div[1]/div[2]/ul[2]/li/a").click()
        self.driver.find_element_by_xpath(
            "//*[@id='page']/div/div/div/pv-login-reg-container/div/div/div/div[2]/div[2]/div[1]/pv-login/div/form/div/input[1]").send_keys(
            "srihari")
        self.driver.find_element_by_xpath(
            "//*[@id='page']/div/div/div/pv-login-reg-container/div/div/div/div[2]/div[2]/div[1]/pv-login/div/form/div/input[2]").send_keys(
            1234)

        self.driver.find_element_by_xpath(
            "//*[@id='page']/div/div/div/pv-login-reg-container/div/div/div/div[2]/div[2]/div[1]/pv-login/div/form/div/input[3]").click()
        self.driver.implicitly_wait(5000)
        ErrorMessage = self.driver.find_element_by_xpath(
            "//*[@id='page']/div/div/div/pv-login-reg-container/div/div/div/div[2]/div[2]/div[1]/pv-login/div/form/div/input[3]")

        if self.driver.page_source in 'Invalid username or password':
            print("Entered Wrong User Credentials")
        else:
            print("Enter incorrect User Credentials")

        self.driver.implicitly_wait(5000)

        GetTextMessage = ErrorMessage.text

        print(GetTextMessage)
        print("Test Passed")

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()
        print(" Tests are completed")
