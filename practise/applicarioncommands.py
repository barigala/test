from selenium import webdriver
from selenium.webdriver.chrome.service import service

driver = webdriver.Chrome(executable_path="C:\DriversAuto\chromedriver.exe")
driver.get("http://opensource-demo.orangehrmlive.com/") # launch the browser
driver.maximize_window() #maximise window

print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.close()
