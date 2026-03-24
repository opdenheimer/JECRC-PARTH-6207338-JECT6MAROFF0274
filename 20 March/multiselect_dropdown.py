from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver=webdriver.Chrome()
wait=WebDriverWait(driver,10)

# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
#
# multidrop=driver.find_element(By.ID,"colors")
# select=Select(multidrop)
#
# if select.is_multiple:
#     select.select_by_value("blue")
#     select.select_by_index(2)
#     select.select_by_visible_text("Red")
#
# sleep(3)
# select.deselect_by_value("blue")
# print('after')

#---------------------------------------------------------------------------------------------------------------------------

driver.get(r"C:\Users\DELL\Desktop\Capegemini Training\automation &testing\20 March\playlist.html")
driver.maximize_window()

song_list=driver.find_element(By.ID,'songs')
select=Select(song_list)

if select.is_multiple:
    select.select_by_index(0)
    select.select_by_visible_text("Shape of You")
    select.select_by_visible_text("Galway Girl")

print([i.text for i in select.all_selected_options])
print([i.text for i in select.options])
bttn=driver.find_element(By.XPATH,"//button[text()='Add to Playlist']")
bttn.click()

sleep(5)
driver.quit()