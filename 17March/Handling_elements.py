from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)

driver.get('https://www.lenskart.com/')
driver.maximize_window()
sleep(5)
glass_cat=driver.find_element(By.XPATH,"//div[@class='sc-7b769982-0 jFhicW']")
glass_cat.click()
eye=driver.find_element(By.ID,'lrd1')
print(eye.text)
'''
assert - acts like an if else statement if the not true (else statement ) gives an assertion error with the error given 
 
'''
#assert 'GLASSES' == eye.text, 'didnt find this text'

driver.quit()