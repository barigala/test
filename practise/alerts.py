import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\DriversAuto\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/javascript_alerts") # launch the browser
driver.maximize_window() #maximise window

#opens alert prompt
#driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
#time.sleep(5)

#alertwindow=driver.switch_to.alert
#print(alertwindow.text)
#alertwindow.send_keys("Hello")
#alertwindow.accept() #close alert window by using OK button
#alertwindow.dismiss() #close cancel button

#opens confirm window
#driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']").click()
#time.sleep(5)

#alertwindow=driver.switch_to.alert
#print(alertwindow.text)
#alertwindow.send_keys("Hello")
#alertwindow.accept() #close alert window by using OK button
#alertwindow.dismiss() #close cancel button

#opens confirm window
driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']").click()
time.sleep(5)

alertwindow=driver.switch_to.alert
print(alertwindow.text)
#alertwindow.send_keys("Hello")
alertwindow.accept() #close alert window by using OK button
#alertwindow.dismiss() #close cancel button
