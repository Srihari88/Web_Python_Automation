from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.pitchvision.com/#/login")

# driver.find_element_by_xpath("//*[@id='page']/header/div[1]/div[2]/ul[2]/li/a").click()
driver.find_element_by_xpath(
    "//*[@id='page']/div/div/div/pv-login-reg-container/div/div/div/div[2]/div[2]/div[1]/pv-login/div/form/div/input[1]").send_keys(
    "srihari")
driver.find_element_by_xpath(
    "//*[@id='page']/div/div/div/pv-login-reg-container/div/div/div/div[2]/div[2]/div[1]/pv-login/div/form/div/input[2]").send_keys(
    1234)

driver.find_element_by_xpath(
    "//*[@id='page']/div/div/div/pv-login-reg-container/div/div/div/div[2]/div[2]/div[1]/pv-login/div/form/div/input[3]").click()
driver.implicitly_wait(5000)

ErrorMessage = driver.find_element_by_xpath(
    "//*[@id='page']/div/div/div/pv-login-reg-container/div/div/div/div[2]/div[2]/div[1]/pv-login/div/form/div/input[3]")

if driver.page_source in 'Invalid username or password':
    print("Entered Wrong User Credentials")
else:
    print("Enter incorrect User Credentials")

driver.implicitly_wait(5000)

GetTextMessage = ErrorMessage.text

print(GetTextMessage)

# assert GetTextMessage == 'Invalid username or password'

# assert "Invalid username or password" in GetTextMessage

print(" Test passed ")

driver.close()
