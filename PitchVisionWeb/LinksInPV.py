from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.pitchvision.com")

links = driver.find_elements_by_tag_name("a")
links2 = driver.find_elements_by_tag_name("script")
print(len(links))

for link in links:
    print(link.text)

for linkscr in links2:
    print(linkscr.text)
driver.close()
