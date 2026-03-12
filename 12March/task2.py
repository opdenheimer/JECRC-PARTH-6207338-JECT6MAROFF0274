from selenium import webdriver
from time import sleep

list1=[webdriver.Chrome(),webdriver.Edge(),webdriver.Firefox()]
for item in list1:
    driver=item
    driver.get("https://google.com")
    # dri.maximize_window()
    sleep(5)