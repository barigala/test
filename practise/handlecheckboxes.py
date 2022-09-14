import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="C:\DriversAuto\chromedriver.exe")
driver.get("https://itera-qa.azurewebsites.net/home/automation") # launch the browser
driver.maximize_window() #maximise window

# 1 select check box
#driver.find_element(By.XPATH, "//input[@id='monday']").click()

#2 select all the check boxes
checkboxes=driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))

#approach1
#for i in range(len(checkboxes)):
 #   checkboxes[i].click()

#approach 2

for checkbox in checkboxes:
    checkbox.click()

#3 select multiple checkboxes of choice

#for checkboxe in checkboxes:
 #   weekname = checkboxe.get_attribute('id')
  #  if weekname=='wednesday' or weekname=='thursday':
   #     checkboxe.click()

#4 select last 2 checkboxes

#for i in range(len(checkboxes)-2, len(checkboxes)):
 #   checkboxes[i].click()

#5 select first 2 checkboxes

#for i in range(len(checkboxes)):
 #   if i<2:
  #      checkboxes[i].click()

time.sleep(5)

#6 clearing all check boxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()