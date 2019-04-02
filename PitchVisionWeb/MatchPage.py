# To test login functionality on Web.


from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.pitchvision.com/#/pv-matches")

driver.implicitly_wait(10)

driver.find_element_by_xpath("//input[@ng-model='playerName']").send_keys("srihari")

driver.find_element_by_xpath("//*[@id='page']/div/div/div/section/div/div[3]/div/div[2]/div[6]/img").click()

driver.implicitly_wait(5000)

Results = driver.find_elements_by_xpath("//div[@ng-repeat='match in matches track by $index']")

driver.implicitly_wait(5000)

for i in Results:
    print(i.text)
# driver.find_element_by_xpath("//*[@id='page']/div/div/div/section/div/div[3]/div/div[2]/div[7]/img").click
print(" Tests Passed")

driver.close()
