import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

#would join the folder and dir name
folder=os.path.join(os.getcwd(),'screenshots')
#if dir already there it wont give any error and execute the code further
os.makedirs(folder,exist_ok=True)

driver=webdriver.Chrome()
actions=ActionChains(driver)
driver.get("https://www.inc.in")
driver.maximize_window()
sleep(3)

ele=driver.find_element(By.XPATH,"(//div[@class='section_7_home_slider_wrapper']//descendant::a[@href='our-inspiration/babu-jagjivan-ram'])[1]")
sleep(2)
actions.move_to_element(ele).perform()
sleep(2)

ele.screenshot(f"{folder}/full_page.png")

sleep(3)