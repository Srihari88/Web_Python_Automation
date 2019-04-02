from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.pitchvision.com/#/")

Banner = driver.find_elements_by_xpath("//ol[@class='carousel-indicators home-carousel-indicators']/li")

Size= driver.find_element_by_xpath("//img[@src='images/redesign/banners/home-page-banner-3.jpg']")

for i in Banner:
    i.click()
    print(i.size)
    print(Size.size)
    print("Clicked on first Banner")


print("Result Program executed")

driver.close()