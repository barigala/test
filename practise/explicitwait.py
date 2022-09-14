from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\DriversAuto\chromedriver.exe")

#mywait=WebDriverWait(driver,10) #basic explicit wait declaration
mywait=WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[Exception,NoSuchElementException])

driver.get("https://www.google.com/") # launch the browser
driver.maximize_window() #maximise window

search_box=driver.find_element(By.XPATH, "//input[@title='Search']")
search_box.send_keys("Selenium")
search_box.submit()

searchlink=mywait.until(EC.presence_of_element_located((By.XPATH, "//h3[normalize-space()='Selenium']")))
searchlink.click()

