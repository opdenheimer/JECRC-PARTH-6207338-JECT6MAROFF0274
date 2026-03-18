from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

from Week1Assessment.task2 import search_box

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)
#driver.get('https://amazon.com')
#driver.get("https://testautomationpractice.blogspot.com/")
driver.get('https://www.flipkart.com')
driver.maximize_window()


#for gender radio buttons
# gender=input("enter your gender:")
# if gender=="male":
#     radio_button=driver.find_element(By.XPATH,"//input[@id='male']")
#     radio_button.click()
# if gender=="female":
#     radio_button = driver.find_element(By.XPATH, "//input[@id='female']")
#     radio_button.click()
#
sleep(5)


#check uncheck all the days name and print their text
# for i in range(1,8):
#     Day_checkbox=driver.find_element(By.XPATH, f"//label[@for='days']//following-sibling::div[{i}]//input")
#     Day_checkbox.click()
#     dayname=driver.find_element(By.XPATH, f"//label[@for='days']//following-sibling::div[{i}]//label")
#     print(dayname.text)
#
# for i in range(7,-1,-1):
#     Day_checkbox=driver.find_element(By.XPATH, f"//label[@for='days']//following-sibling::div[{i}]//input")
#     Day_checkbox.click()
#     # dayname=driver.find_element(By.XPATH, f"//label[@for='days']//following-sibling::div[{i}]//label")
#     # print(dayname.text)


#flipkart

cross_button=driver.find_element(By.XPATH,"//span[text()='✕']")
cross_button.click()
search=driver.find_element(By.XPATH,"//input[@class='nw1UBF v1zwn25']")
search.clear()
search.send_keys("Iphone",Keys.ENTER)



