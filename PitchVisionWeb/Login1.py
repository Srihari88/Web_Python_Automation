from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.pitchvision.com/#/login")

# driver.find_element_by_xpath("//*[@id='page']/header/div[1]/div[2]/ul[2]/li/a").click()
driver.find_element_by_xpath(
    "//*[@id='page']/div/div/div/pv-login-reg-container/div/div/div/div[2]/div[2]/div[1]/pv-login/div/form/div/input[1]").send_keys(
    "Daisy.dalia")
driver.find_element_by_xpath(
    "//*[@id='page']/div/div/div/pv-login-reg-container/div/div/div/div[2]/div[2]/div[1]/pv-login/div/form/div/input[2]").send_keys(
    "dentrain")

driver.find_element_by_xpath(
    "//*[@id='page']/div/div/div/pv-login-reg-container/div/div/div/div[2]/div[2]/div[1]/pv-login/div/form/div/input[3]").click()
driver.implicitly_wait(5000)
ErrorMessage = driver.find_element_by_xpath(
    "//*[@id='page']/div/div/div/pv-login-reg-container/div/div/div/div[2]/div[2]/div[1]/pv-login/div/form/div/input[3]")
if driver.page_source in 'Invalid username or password':
    print("Entered Correct Login details: ")
    driver.implicitly_wait(5000)
else:
    print("Entered incorrect User Credentials")
    driver.implicitly_wait(5000)
    GetTextMessage = ErrorMessage.text

print(GetTextMessage)
print("Test Passed")

driver.close()
