from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\DriversAuto\chromedriver.exe")
driver.get("http://demo.nopcommerce.com/register") # launch the browser
driver.maximize_window() #maximise window

print("===========================")
#is_displayed() & is_enabled()
searchbox=driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("Display Status:", searchbox.is_displayed())
print("Enabled Status:", searchbox.is_enabled())

print("===========================")
#is_selected
rd_male=driver.find_element(By.XPATH, "//input[@id='gender-male']")
rd_fmale=driver.find_element(By.XPATH, "//input[@id='gender-female']")
print("before_Status:", rd_male.is_selected())
print("Beforestatus:", rd_fmale.is_selected())

print("===========================")
rd_male.click()
print("after_Status:", rd_male.is_selected())
print("after_status:", rd_fmale.is_selected())

print("===========================")
rd_fmale.click()
print("after_Status:", rd_male.is_selected())
print("after_status:", rd_fmale.is_selected())

print("===========================")

driver.close()