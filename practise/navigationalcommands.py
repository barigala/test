import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\DriversAuto\chromedriver.exe")
driver.maximize_window() #maximise window
driver.get("https://flipkart.com/") # launch the browser
driver.get("https://amazon.in")

driver.back()
driver.forward()

driver.refresh()

driver.quit()

