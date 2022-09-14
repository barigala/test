from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\DriversAuto\chromedriver.exe")
driver.get("https://money.rediff.com/gainers/") # launch the browser
driver.maximize_window() #maximise window

#capture text of the element
text_msg=driver.find_element(By.XPATH, "//a[normalize-space()='PTC India Financial']/self::a").text
print(text_msg)
