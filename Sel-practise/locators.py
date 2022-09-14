from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\DriversAuto\chromedriver.exe")
driver.get("https://demo.nopcommerce.com/") # launch the browser
driver.maximize_window() #maximise window

#locator using ID & name
#driver.find_element(By.ID, "small-searchterms").send_keys("Nokia Lumia 1020")
driver.find_element(By.NAME, "q").send_keys("Nokia Lumia 1020")

#link text, when there is no ID or name available in inspect element
#driver.find_element(By.LINK_TEXT, "Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()


driver.close()