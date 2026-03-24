from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver=webdriver.Chrome()
wait=WebDriverWait(driver,10)

driver.get(r"C:\Users\DELL\Desktop\Capegemini Training\automation &testing\20 March\playlist.html")
driver.maximize_window()

song_list=driver.find_element(By.ID,'songs')
select=Select(song_list)

l1=[i.text for i in select.options]
for song in l1 :
    if ('girl' in song.lower() or 'love' in song.lower() ):
        select.select_by_visible_text(song)

bttn=driver.find_element(By.XPATH,"//button[text()='Add to Playlist']")
bttn.click()

sleep(6)