from selenium import webdriver

# driver = webdriver.Chrome(executable_path='/Users/reenupanwar/PycharmProjects/MyPythonProjects/Drivers/chromedriver')
driver = webdriver.Chrome()

driver.get("https://www.pitchvision.com")
print(driver.title)

Headers = driver.find_elements_by_xpath("//div[@class='header-bar']/ul/li")

list = []

for i in Headers:
    list.append(i.text)
print(list)

assert 'HOME' in list
assert 'MATCHES' in list
assert 'PRODUCTS' in list
assert 'ARTICLES' in list
assert 'PODCASTS' in list
assert 'ABOUT US' in list
assert 'DOWNLOAD APP' in list
# assert 'CSA SCHOOLS T20' in list


PVTV = driver.find_elements_by_xpath("//div[@class='pv-tv-global-tab scroll-pane']/ul/li")

for lis in PVTV:
    print(lis.text)

print("All tests passed..!! ")
driver.close()
