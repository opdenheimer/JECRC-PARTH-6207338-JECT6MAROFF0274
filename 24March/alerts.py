import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
sleep(3)
wait=WebDriverWait(driver,10)

#------------------------------------------simple alert------------------------------------------------------------------
simple=wait.until(EC.presence_of_element_located((By.XPATH,"//button[text()='Click for JS Alert']")))
simple.click()

sleep(3)
alert=driver.switch_to.alert
alert.accept()
sleep(2)

#-----------------confirm alert-------------------------------------------------------
simple = wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Click for JS Confirm"]')))
# simple.click()
# sleep(2)
#
# alert = driver.switch_to.alert
# # alert.accept()
# alert.dismiss()
# sleep(2)

#------------------Prompt alert---------------------
# simple = wait.until(EC.((By.XPATH, '//button[text()="Click for JS Prompt"]')))
# simple.click()
# sleep(2)
#
# alert = driver.switch_to.alert
# alert.send_keys("Hello 1")
# # alert.accept()
# alert.dismiss()
# sleep(2)

#-----------------switching to alerts using wait------------
wait.until(EC.presence_of_element_located((By.XPATH,"//button[@oneclick='jsAlerts()']")))
alert = wait.until(EC.alert_is_present())
sleep(3)
alert.accept()
sleep(2)



driver.quit()


