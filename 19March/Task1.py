from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opts)
driver.get("https://abc.com")
driver.maximize_window()
circle_obj=WebDriverWait(driver,10)
images = circle_obj.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="tile--hero__container"]//descendant::picture//img')))
for image_link in images:
    print(image_link.get_attribute('src'))
