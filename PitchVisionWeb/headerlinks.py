from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.pitchvision.com")

Expected = "https://www.pitchvision.com/#/pv-matches"

driver.find_element_by_xpath("//*[@id='page']/header/div[3]/ul/li[2]/a").click()

if driver.current_url == Expected:
    print("Test Passed")
else:
    print("Test Failed")

driver.implicitly_wait(4000)

Article = "https://www.pitchvision.com/academy#/"

driver.find_element_by_xpath("//*[@id='page']/header/div[3]/ul/li[4]/a/span").click()

driver.implicitly_wait(8000)

if driver.current_url == Article:
    print("Test Passed")
else:
    print("Test Failed")
driver.close()
