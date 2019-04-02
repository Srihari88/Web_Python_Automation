from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/reenupanwar/PycharmProjects/MyPythonProjects/Drivers/chromedriver')

#driver = webdriver.Chrome()

driver.get("https://www.pitchvision.com")
print(driver.title)
print(driver.page_source)
driver.fullscreen_window()
print(driver.current_url)
driver.get_screenshot_as_png()
driver.refresh()
driver.save_screenshot("/Users/reenupanwar/Desktop/Resume/ssri.png")


driver.close()