from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\DriversAuto\chromedriver.exe")
driver.get("http://facebook.com/") # launch the browser
driver.maximize_window() #maximise window

# tag & id
#driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc")
#driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc")  #can use '#' for id only

#tag & class
#driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abce@gmail.com")
#driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("abce@gmail.com")

#tag & attribute
#driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_email]").send_keys("abce@gmail.com")
#driver.find_element(By.CSS_SELECTOR, "[data-testid=royal_email]").send_keys("abce@gmail.com")

#tag & class & attribute
driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_email]").send_keys("abce@gmail.com") #email
driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_pass]").send_keys("123456") # pwd
