from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\DriversAuto\chromedriver.exe")
driver.get("https://demo.nopcommerce.com/") # launch the browser
driver.maximize_window() #maximise window

#locator matching with single webelement
#elemts=driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
#elemts.send_keys("Apple MacBook Pro 13-inch")

#locator matching with multiple webelements
#element=driver.find_element(By.XPATH, "//div[@class='footer']//a")
#print(element.text)

#element not available then throw nosuchelementexception
#login_element=driver.find_element(By.LINK_TEXT, "Login")
#login_element.click()

#####################################
#locator matching with single webelements
#elemts=driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
#print(len(elemts))
#elemts[0].send_keys("Apple MacBook Pro 13-inch")

#locator matching with multiple webelements
#element=driver.find_elements(By.XPATH, "//div[@class='footer']//a")
#print(len(element)) #23
#print(element[0].text) #sitemap
#for ele in element:
 #   print(ele.text)


#element not available then throw nosuchelementexception
login_element=driver.find_elements(By.LINK_TEXT, "Login")
print(len(login_element))