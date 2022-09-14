from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\DriversAuto\chromedriver.exe")
driver.get("http://automationpractice.com/index.php") # launch the browser
driver.maximize_window() #maximise window

#abs xpath
#driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[2]/form[1]/input[4]").send_keys("T-shirts")
#driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[2]/form[1]/button[1]").click()

#Relative Xpath
driver.find_element(By.XPATH, "//input[@id='search_query_top']").send_keys("T-shirts")
driver.find_element(By.XPATH, "//button[@name='submit_search']").click()

