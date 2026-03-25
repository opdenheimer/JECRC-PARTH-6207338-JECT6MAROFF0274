import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver=webdriver.Chrome()
driver.get("https://in.pinterest.com/")
driver.maximize_window()
sleep(3)
actions=ActionChains(driver)

#to bottom of the page
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
sleep(3)

#to origin of page
driver.execute_script("window.scrollTo(0,0);")
sleep(3)

#using Scroll By
driver.execute_script("window.scrollBy(0,500);")
sleep(4)
driver.execute_script("window.scrollBy(0,-300);")
sleep(3)

#scrolling to ele
# element=driver.find_element("//driver.find_element(By.XPATH, '(//div[@class='ADXRXN AsRsEE'])[3]//descendant::img')")
element = driver.find_element(By.XPATH, '(//div[@class="ADXRXN AsRsEE"])[3]//descendant::img')
driver.execute_script("arguments[0].scrollIntoView();",element)
sleep(4)

#clicking
click_ele=driver.find_element(By.XPATH,'(//div[text()="Join Pinterest"])[1]')

driver.execute_script("arguments[0].click();",click_ele)
sleep(3)

driver.quit()

