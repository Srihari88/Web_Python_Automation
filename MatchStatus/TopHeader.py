from selenium import webdriver
import unittest
import time
from MatchStatus.baseTest import basTest


class TopHead(unittest.TestCase):
    def setUpClass(cls):
        global driver
        base = basTest(webdriver)
        base.test_Basetest()


