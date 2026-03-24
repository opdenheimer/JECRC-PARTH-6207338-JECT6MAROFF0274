'''
action chains- a class used to interact with the actions taking place through keyboards or mouse
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver=webdriver.Chrome()
wait=WebDriverWait(driver,10)

#drag and drop
# driver.get("https://the-internet.herokuapp.com/drag_and_drop")
# sleep(5)
# actions=ActionChains(driver)
#
# original_ele=driver.find_element(By.ID,'column-a')
# target_ele=driver.find_element(By.ID,'column-b')
#
# #to perform any action use .perform()
# actions.drag_and_drop(original_ele,target_ele).perform()
# sleep(5)

#hover actions
# driver.get("https://supertails.com/")
# driver.maximize_window()
# actions=ActionChains(driver)
# element=driver.find_element(By.XPATH,"(//span[contains(text(),'Dogs')])[1]")
# actions.move_to_element(element).perform()
# sleep(2)

