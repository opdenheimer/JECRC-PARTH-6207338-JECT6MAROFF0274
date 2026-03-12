from selenium import webdriver
from time import sleep
opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver= webdriver.Chrome(options=opts)

driver.get("https://youtube.com/")
print(driver.title())
print(driver.current_url())
driver.maximize_window()
sleep(2)
driver.minimize_window()
sleep(2)
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.refresh()
driver.sleep(2)
#driver.close()
driver.quit()



