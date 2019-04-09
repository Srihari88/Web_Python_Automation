from selenium import webdriver
import time
import pytest


def setUpClass():
    global driver
    print(" Open Application")
    driver = webdriver.Chrome()

    driver.get("https://opensource-demo.orangehrmlive.com/")


def test_Valid_Login(setUpClass):
    driver.find_element_by_id("txtUsername").send_keys("admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
    time.sleep(5)


def test_PVMConfirgOption(setUpClass):
    driver.find_element_by_name("welcome").click()


def tearDownClass(setUpClass):
    print("Close Application")
