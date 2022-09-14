from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\DriversAuto\chromedriver.exe")
driver.implicitly_wait(10) #seconds
driver.get("https://www.google.com/") # launch the browser
driver.maximize_window() #maximise window

search_box=driver.find_element(By.XPATH, "//input[@title='Search']")
search_box.send_keys("Selenium")
search_box.submit()

driver.find_element(By.XPATH, "//h3[normalize-space()='Selenium']").click()