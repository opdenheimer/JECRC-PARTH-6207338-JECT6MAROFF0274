'''
scroll_to()- scroll acc to coordinates by pixels given to the specified pixelwise(specific pixel to which we have to scroll)
scroll_by()-scroll down to pixel by specified pixels after that(these are dist to be added)
scroll up -ve values
scroll down +ve values
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
wait=WebDriverWait(driver,10)
actions=ActionChains(driver)
#
# driver.get("https://demoqa.com/droppable")
# driver.maximize_window()
# sleep(5)
# dragbox=wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@id="draggable"]')))
# dropbox=wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@id="droppable"]')))
#
# actions.drag_and_drop(dragbox,dropbox).perform()
# sleep(5)

#------------------------------------------------------------------------------------------------------------------
# driver.get("https://demoqa.com/droppable")
# driver.maximize_window()
# sleep(5)
#
# bttn=driver.find_element(By.ID,"droppableExample-tab-preventPropogation")
# bttn.click()
# dragbox=driver.find_element(By.ID,"dragBox")
# dropbox=driver.find_element(By.ID,"notGreedyInnerDropBox")
#
# actions.drag_and_drop(dragbox,dropbox).perform()
# sleep(5)

# ----------------------------Scrolling element---------------------------------------------------------------------------------------------------------------
# driver.get("https://supertails.com/")
# driver.maximize_window()
#
# persian_cat=driver.find_element(By.XPATH,"//div[@data-ganame='Breed 5']")
# actions.scroll_to_element(persian_cat).perform()
# sleep(5)
#
# actions.scroll_by_amount(0,-15000).perform()
# sleep(5)
#
# driver.quit()
#
#----------------------------------Keyboard Actions-------------------------------------------------------------------------------------------------------
# driver.get("https://supertails.com/")
# driver.maximize_window()

# actions.send_keys(Keys.PAGE_DOWN).perform()
# sleep(6)
# actions.send_keys(Keys.PAGE_UP).perform()
# sleep(6)
# actions.key_down(Keys.CONTROL).send_keys('a').perform()
# sleep(6)
# actions.key_up(Keys.CONTROL).perform()
# sleep(6)

#------------------------------------------------------------------------------------------------------------------------------------------
# driver.get(r"C:\Users\DELL\Desktop\Capegemini Training\automation &testing\23March\webpage.html")
# driver.maximize_window()
#
# present=driver.find_element(By.ID,'presentAddress')
# permanent=driver.find_element(By.ID,'permanentAddress')
# present.send_keys('JECRC, JAIPUR,RJ')
# sleep(4)
# present.click()
#
# actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
# sleep(2)
# actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
# permanent.click()
# sleep(2)
# actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
# sleep(2)


#--------------------------password visibilty-------------------------------------------------------------------
driver.get(r"C:\Users\DELL\Desktop\Capegemini Training\automation &testing\21March\index1.html")
driver.maximize_window()
sleep(4)

driver.find_element(By.ID,"password").send_keys("Password")
sleep(3)

show_pwd=driver.find_element(By.ID,"eyeBtn")
actions.click_and_hold(show_pwd).perform()
sleep(3)
actions.release()
sleep(2)
driver.quit()