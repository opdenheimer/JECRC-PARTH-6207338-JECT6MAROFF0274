'''
window handles
'''
from numpy.ma.core import inner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
sleep(2)

parent_window=driver.current_window_handle

#opening a website in new window
driver.switch_to.new_window('window')
sleep(2)
driver.get("https://www.cricbuzz.com/")
sleep(2)

driver.switch_to.window('tab')
sleep(2)
driver.get("https://www.cricbuzz.com/")
sleep(2)
