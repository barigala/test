from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\DriversAuto\chromedriver.exe")
driver.get("http://automationpractice.com/") # launch the browser
driver.maximize_window() #maximise window



sliders=driver.find_elements(By.CLASS_NAME, "homeslider-description")
print(len(sliders)) #total no.of sliders

allinks=driver.find_elements(By.TAG_NAME, "a")
print(len(allinks)) # total no.of links on homepage

driver.close()