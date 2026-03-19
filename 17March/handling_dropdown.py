from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
'''
3 ways to select the text in a dropdown
1)BY visible text
2)by value attribute
by index
'''

country_dropdown=driver.find_element(By.ID,'country')
dropdown=Select(country_dropdown)
dropdown.select_by_index(1)
sleep(5)
dropdown.select_by_value("india")