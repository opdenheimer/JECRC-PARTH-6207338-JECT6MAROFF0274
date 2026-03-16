from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

# driver.get("https://www.cricbuzz.com")
# sleep(5)
# driver.get("https://www.amazon.com")
# sleep(5)
# driver.get("https://www.myntra.com")
# sleep(5)
# xpath_name=driver.find_element(By.XPATH,"//span[text()='All']/ancestor::div[@id='nav-main']")
# print(xpath_name.text)
# xpath_name2=driver.find_element(By.XPATH,"//div[@id='nav-main]/descendant::span[text()='All']")
# print(xpath_name2.text)
# sibling = driver.find_element(By.XPATH,"//div[@class='group1']/preceding-sibling::div")
# print(sibling.text)
# sibling2=driver.find_element(By.XPATH,"//a[text()='Fresh' ]/ancestor::li/following-sibling::li[1]")
driver.get("https://testautomationpractice.blogspot.com")
sleep(5)
# Linktext=driver.find_element(By.LINK_TEXT,"Udemy Courses")
# print(Linktext)
# driver.find_element(By.PARTIAL_LINK_TEXT,"Udemy")
# print(driver.find_element(By.PARTIAL_LINK_TEXT,"Udemy"))
#
driver.find_element(By.XPATH,"//td[text()='300'/preceding-sibling::td[3]")