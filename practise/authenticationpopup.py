from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\DriversAuto\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/") # launch the browser
driver.maximize_window() #maximise window

driver.find_element(By.XPATH, "//a[normalize-space()='Basic Auth']").click()

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")