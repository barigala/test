from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="C:\DriversAuto\chromedriver.exe")
driver.get("https://demo.nopcommerce.com/") # launch the browser
driver.maximize_window() #maximise window

#click on the link
#driver.find_element(By.PARTIAL_LINK_TEXT, "Digital downloa").click()

#find number of links in a page
links=driver.find_elements(By.TAG_NAME, 'a')
print("# no.of links:", len(links))

#print all the link names

for link in links:
    print(link.text)