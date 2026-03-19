from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)

driver.get("https://www.lenskart.com")

search_box=driver.find_element(By.XPATH,"//input[@class='aa-Input']")
search_box.clear()
search_box.send_keys("full rim eyeglasses",Keys.ENTER)

sort_dropdown=driver.find_element(By.ID,"sortByDropdown")
dropdown=Select(sort_dropdown)
dropdown.select_by_value('created')
sleep(2)

first=driver.find_element(By.XPATH,"(//div[@id='listing-wrapper']//div[@data-cy='plpCardContainer'])[1]")
print(first.text)
sleep(2)

driver.quit()