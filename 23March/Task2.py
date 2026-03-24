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

driver.get("https://www.myntra.com/")
driver.maximize_window()
sleep(2)

men_cat=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@data-reactid=20]//descendant::a[@data-index=0]")))
actions.move_to_element(men_cat).perform()
sleep(2)

cat=wait.until(EC.visibility_of_element_located((By.XPATH,"//a[text()='Suits']")))
cat.click()
sleep(2)

produtct=wait.until(EC.presence_of_element_located((By.XPATH,"//ul[@class='results-base']/descendant::li[23]")))
actions.scroll_to_element(produtct).perform()
sleep(2)
driver.quit()
