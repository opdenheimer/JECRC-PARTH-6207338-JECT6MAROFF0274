'''
iframes are html pages embedded in another html page (nested html)
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
#----------single iframe--------------------------------------------------------------------------------------------
# driver.get("https://demo.automationtesting.in/Frames.html")
# driver.maximize_window()
# sleep(3)
#
# iframe=driver.find_element(By.ID,'singleframe')
# driver.switch_to.frame(iframe)
# sleep(3)
# driver.find_element(By.XPATH,"//input[@type='text']").send_keys("1232")
# sleep(3)

#--------------------------------------------nested iframe------------------------------------------------------
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
sleep(3)

driver.find_element(By.XPATH,"//a[text()='Iframe with in an Iframe']").click()
nested_iframe=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(nested_iframe)

inner_iframe=driver.find_element(By.XPATH,"//iframe[@src='SingleFrame.html']")
driver.switch_to.frame(inner_iframe)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("1232")
sleep(3)
