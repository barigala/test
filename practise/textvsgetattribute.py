from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\DriversAuto\chromedriver.exe")
driver.get("https://admin-demo.nopcommerce.com/") # launch the browser
driver.maximize_window() #maximise window

email_field=driver.find_element(By.XPATH, "//input[@id='Email']")
email_field.clear()
email_field.send_keys("abce@gmail.com")

print("Result of Text:", email_field.text)
print("Result of get_attribute():", email_field.get_attribute('value'))