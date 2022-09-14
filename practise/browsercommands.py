import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\DriversAuto\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/") # launch the browser
driver.maximize_window() #maximise window

driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']").click()

time.sleep(5)

#driver.close()
driver.quit()