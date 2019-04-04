from selenium import webdriver
import unittest

class mathStatus(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://www.pitchvision.com/#/login")

    def test_login_valid(self):
        # driver.find_element_by_xpath("//*[@id='page']/header/div[1]/div[2]/ul[2]/li/a").click()
        self.driver.find_element_by_xpath(
            "//*[@id='page']/div/div/div/pv-login-reg-container/div/div/div/div[2]/div[2]/div[1]/pv-login/div/form/div/input[1]").send_keys(
            "daisy.dalia")

        self.driver.find_element_by_xpath(
            "//*[@id='page']/div/div/div/pv-login-reg-container/div/div/div/div[2]/div[2]/div[1]/pv-login/div/form/div/input[2]").send_keys(
            "dentrain")

        self.driver.find_element_by_xpath(
            "//*[@id='page']/div/div/div/pv-login-reg-container/div/div/div/div[2]/div[2]/div[1]/pv-login/div/form/div/input[3]").click()
        self.driver.implicitly_wait(10000)

    def test_profile(self):
        self.driver.find_element_by_xpath("//img[@ng-src='https://www.pitchvision.com/cdn/images/unknown.jpg']").click()
        self.driver.find_element_by_xpath("//ul[@class='dropdown-menu dropdown-menu-right']/li[3]/a").click()
        print(self.driver.current_url)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__== "__main__":
    unittest.main()



