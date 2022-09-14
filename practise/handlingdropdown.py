from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\DriversAuto\chromedriver.exe")
driver.get("https://www.opencart.com/index.php?route=account/register") # launch the browser
driver.maximize_window() #maximise window

drpcountry_ele=driver.find_element(By.XPATH, "//select[@id='input-country']")
drpcountry=Select(drpcountry_ele)

#select optin from the dropdown
#drpcountry.select_by_visible_text("India")
#drpcountry_ele.select_by_value("12")
#drpcountry.select_by_index(13)

#apture all the options and print them
alloptions=drpcountry.options
print("Total number of options are:", len(alloptions))

#for opt in alloptions:
 #   print(opt.text)

 #select option from dropdown without using builtin method
for opt in alloptions:
    if opt.text=="India":
        opt.click()
        break

