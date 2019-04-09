from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/")
Action = ActionChains(driver)

Action.move_to_element(driver.find_element_by_id("birthday-help")).perform()

Action.move_to_element(driver.find_element_by_id("u_0_11")).click_and_hold().perform()
Action.move_to_element(driver.find_element_by_id("u_0_11")).context_click().perform()


select=Select(driver.find_element_by_id("month"))
d=select.all_selected_options()
print(d)
select.select_by_value("8")

#
# # Text Box
# Email = driver.find_element_by_id("email")
#
# Email.send_keys("sriharinaidupudu@gmail.com")
#
# Password = driver.find_element_by_id("pass")
#
# Password.send_keys("srihari")
#
# ForgotLink = driver.find_element_by_link_text("Forgotten account?")
# ForgotLink.click()
#
# browser = driver.name
# print(browser)
# driver.back()
# driver.forward()
# driver.refresh()
# cap = driver.desired_capabilities()
# print(cap)
