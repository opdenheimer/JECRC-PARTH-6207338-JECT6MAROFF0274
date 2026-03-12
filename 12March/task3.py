from selenium import webdriver
from time import sleep

list1=[webdriver.Chrome(),webdriver.Edge(),webdriver.Firefox()]
for item in list1:
    driver = item
    driver.get("https://google.com/")
    print(driver.title)
    print(driver.current_url)
    sleep(2)
    #driver.quit()