from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver=webdriver.Chrome(options=opts)
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
sleep(2)

checkbox_link=driver.find_element(By.LINK_TEXT, "Checkboxes")
print("Checkboxes found")

drag_drop_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Drag")
print("Drag and Drop found")

li_elements = driver.find_elements(By.TAG_NAME, "li")
print("Total elements:", len(li_elements))

driver.get("https://the-internet.herokuapp.com/tables")
sleep(2)

website = driver.find_element(By.XPATH,"//table[@id='table1']//td[text()='jdoe@hotmail.com']/following-sibling::td[1]")
print("Website:", website.text)

delete_link = driver.find_element(By.XPATH,"//table[@id='table1']//td[text()='Bach']/parent::tr//a[text()='delete']")
print("Delete link found for Bach")

second_table = driver.find_element(By.XPATH, "(//table)[2]")
print("Second table found")

gridcell = driver.find_element(By.XPATH,"//table[@id='table2']//td[text()='$100.00']")
parent_row = gridcell.find_element(By.XPATH, "./parent::tr")
print("Parent row:", parent_row.text)
sleep(3)
driver.quit()