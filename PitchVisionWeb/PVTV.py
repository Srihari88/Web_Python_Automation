from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.pitchvision.com/#/")

PVTV = driver.find_elements_by_xpath("//ul[@class='resp-tabs-list']/li")


for names in PVTV:
    names.click()
    print(names.text)
    driver.implicitly_wait(15000)

#
# if mylist in "PV Guides":
#     driver.find_element_by_name("PV Guides").click()
# else:
#     print(" Found the playlist")

driver.close()