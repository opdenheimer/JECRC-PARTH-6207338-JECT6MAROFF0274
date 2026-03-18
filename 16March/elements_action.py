from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)
#driver.get('https://amazon.com')
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#name=driver.find_element(By.ID,"name" )
# name=driver.find_element(By.XPATH,"//input[@placeholder='Enter Name']")
# name.clear()
# name.send_keys("Parth")


checkbox=driver.find_elements(By.XPATH,"//input[@id='monday']")
checkbox[0].click()
sleep(5)
checkbox_text=driver.find_elements(By.XPATH,"//input[@id='monday']/following-sibling::label")
print(checkbox_text.text)
sleep(5)

# search=driver.find_element(By.ID,'twotabsearchtextbox')
# search.clear()
# search.send_keys("Iphone",Keys.ENTER)
#search_button=driver.find_element(By.ID,"submit")

driver.quit()
sleep(5)