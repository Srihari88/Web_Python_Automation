from selenium import webdriver
import time
import unittest


class PIM(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        print(" Open Application")
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/")

    @unittest.skipIf(setUpClass, "SriHari")
    def test_AValid_Login(self):
        driver.find_element_by_id("txtUsername").send_keys("admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        time.sleep(5)

    @unittest.skip("Don't want run this test")
    def test_BPVMConfirgOption(self):
        driver.find_element_by_id("welcome").click()
        time.sleep(3)
        driver.find_element_by_xpath("//a[text()='Logout']").click()

    @classmethod
    def tearDownClass(setUpClass):
        driver.close()
        print("Close Application")


if __name__ == '__main__':
    unittest.main()
