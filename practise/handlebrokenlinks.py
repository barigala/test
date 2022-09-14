from selenium import webdriver
from selenium.webdriver.common.by import By
import requests as requests

driver = webdriver.Chrome(executable_path="C:\DriversAuto\chromedriver.exe")
driver.get("http://www.deadlinkcity.com/") # launch the browser
driver.maximize_window() #maximise window

allLinks=driver.find_elements(By.TAG_NAME,'a')
count=0

for link in allLinks:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None
    if res.status_code>=400:
        print(url, " :is a broken link")
        count+=1
    else:
        print(url, " is a valid link")

print("Total number of brokern links", count)