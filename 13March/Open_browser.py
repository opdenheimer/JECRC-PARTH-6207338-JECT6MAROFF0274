from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

#connecting with chrome
opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver= webdriver.Chrome(options=opts)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(2)
name=driver.find_element(By.ID,"name")
phone_no=driver.find_element(By.ID,"phone")
print(name)
print("name Textfield found")
