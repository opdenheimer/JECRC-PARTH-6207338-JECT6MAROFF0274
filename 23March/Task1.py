from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
wait=WebDriverWait(driver,10)
actions=ActionChains(driver)

driver.get("https://www.bjp.org/home")
driver.maximize_window()
sleep(5)
photo=driver.find_element(By.XPATH,"//div[@class='footprint d-flex flex-wrap']//descendant::div[@class='right']")
actions.scroll_to_element(photo).perform()
sleep(2)

for i in range(0,6):
    actions.send_keys(Keys.PAGE_UP).perform()

sleep(2)
driver.quit()