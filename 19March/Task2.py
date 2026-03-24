from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

driver=webdriver.Chrome()
driver.get("https://qavbox.github.io/demo/signup/")

wait=WebDriverWait(driver,20)
username= wait.until(EC.visibility_of_element_located((By.ID,'username')))
username.send_keys("Parth Agarwal")

Email= wait.until(EC.visibility_of_element_located((By.ID,'email')))
Email.send_keys("Parthagarwal@gmail.com")

tel= wait.until(EC.visibility_of_element_located((By.ID,'tel')))
username.clear()
username.send_keys("9898989899")


# fax= wait.until(EC.visibility_of_element_located((By.ID,'fax')))
# #fax.clear()
# fax.send_keys("9898989899")
# #fax.send_keys("2133132")

file_upload=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@name='datafile']")))
file_upload.send_keys(r"C:\Users\DELL\Pictures\Video Projects\1666533803406.jpg")

gender=Select(wait.until(EC.visibility_of_element_located((By.XPATH,"//select[@name='sgender']"))))
gender.select_by_value("male")

experience=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@value='four']")))
experience.click()

skills=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@value='automationtesting']")))
skills.click()

tools=wait.until(EC.visibility_of_element_located((By.XPATH,"//option[@value='selenium']")))
tools.click()

submit=wait.until(EC.visibility_of_element_located((By.ID,"submit")))
submit.click()

sleep(6)


