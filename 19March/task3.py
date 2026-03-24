from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

driver=webdriver.Chrome()
driver.get("https://www.amazon.com")

wait=WebDriverWait(driver,10)

searchbox=wait.until(EC.visibility_of_element_located((By.ID,"twotabsearchtextbox")))
searchbox.send_keys("Iphone")

suggest=wait.until(EC.element_to_be_clickable((By.ID,"sac-suggestion-row-4")))
suggest.click()

sort=wait.until(EC.visibility_of_element_located((By.ID,"a-autoid-0-announce")))
dropdown=Select(sort)
dropdown.select_by_visible_text("Newest Arrivals")

freeship=wait.until(EC.visibility_of_element_located((By.ID,"p_n_free_shipping_eligible/205563695031")))
freeship.click()

price=wait.until(EC.visibility_of_element_located(()))
