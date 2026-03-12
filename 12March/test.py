#Web driver To connect selenium to web browser
from selenium import webdriver
from time import sleep

#connecting with chrome
driver=webdriver.Chrome()

#to provide configurations to the chrome before opening what to do
# opts= webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
#driver= webdriver.Chrome(options=opts)
#
driver.get("https://supertails.com/")
print(driver.title())
print(driver.current_url())
driver.maximize_window()


driver.sleep(8)
#driver.quit()





# sleep(5)
# driver.back()
# sleep(5)
# driver.forward()
# # driver.minimize_window()
# sleep(5)

# #connecting with edge
# driver=webdriver.Edge()
# driver.get("https://supertails.com/")
# driver.maximize_window()
# sleep(5)
# driver.minimize_window()
# sleep(5)

# opts= webdriver.EdgeOptions()
# opts.add_experimental_option('detach', True)
# driver= webdriver.Edge(options=opts)
#
# driver.get("https://supertails.com/")
# driver.maximize_window()

# driver=webdriver.Firefox()
# driver.get("https://supertails.com/")
# driver.maximize_window()
# sleep(5)
# driver.minimize_window()
# sleep(5)
#
# opts= webdriver.FireFoxOptions()
# opts.set_preference('detach', True)
# driver= webdriver.FireFox(options=opts)
#
# driver.get("https://supertails.com/")
# driver.maximize_window()

#driver.close will close the current window but the connection will still be alive
#driver.quit will close the connection also