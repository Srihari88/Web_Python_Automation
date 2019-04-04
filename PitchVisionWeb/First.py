import unittest


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(" Open Application")

    @classmethod
    def setUp(self):
        print(" This is the login functioality")

    def test_testcase1(self):
        print(" 1st Testcase")

    def test_search(self):
        print(" 2nd TestCase")

    def test_google(self):
        print(" 3rd Testcase")

    def test_yahoo(self):
        print(" 4th Testcase")

    @classmethod
    def tearDown(self):
        print(" Logout functionality")

    @classmethod
    def tearDownClass(cls):
        print(" Open Application")


if __name__ == "__main__":
    unittest.main()
