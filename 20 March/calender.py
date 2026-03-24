from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver=webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.find_element(By.ID,'datepicker').send_keys("01/01/2020".Keys.ENTER)

month="May"
Date= '22'

driver.find_element(By.ID,'txtDate').click()
sleep(1)

select=Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']"))
select