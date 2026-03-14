from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

#connecting with chrome
opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver= webdriver.Chrome(options=opts)
driver.get("https://amazon.com")
driver.maximize_window()
driver.maximize_window()
sleep(2)
shortcut_menu=driver.find_element(By.ID,"shortcut-menu")
# 1️⃣ Find element by ID
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
print("Search Box:", search_box)

# 2️⃣ Find element by NAME
search_button = driver.find_element(By.ID, "nav-search-submit-button")
print("Search Button:", search_button)

# 3️⃣ Find elements by CLASS NAME
nav_links = driver.find_elements(By.CLASS_NAME, "nav-a")
print("Number of nav links:", len(nav_links))

# 4️⃣ Find elements by TAG NAME
all_links = driver.find_elements(By.TAG_NAME, "a")
print("Total links on page:", len(all_links))

# 5️⃣ Find elements by CSS Selector
images = driver.find_elements(By.CSS_SELECTOR, "img")
print("Total images:", len(images))

sleep(5)

