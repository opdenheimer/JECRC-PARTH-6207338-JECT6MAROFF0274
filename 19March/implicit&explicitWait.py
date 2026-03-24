'''
Waits in selenium
in production sleep is not recommended as it makes it slower to interact and would wait for the specified fixed time
even if found earlier
instead we use waits
implicit wait(Global): only condition is that the element should be found in Dom structure otherwise it would give a
not found error , would wait till the element is found on the defined time set if not then error only drawback
is it doesn't care if the element is clickable or present on the UI if present in DOM it would return

explicit wait(confined to the particular ele):will wait for that particular element untill its found
  it will find the element ,wait for that elem, return that element ,
  -fluent wait:
  -by default it checks for tht ele in every 0.5 sec which is polling frq
   so we can handle this polling frq by giving poll_frq attribute to check it in a periodic manner shorter duratins

we are not supposed to use both waits together it will combine both of them  
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.abc.com")

#implicit wait

# driver.implicitly_wait(10)
# driver.find_element(By.XPATH,"//a[@class='AnchorLink']/parent::")


#explicit wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#will throw time out error exception
wait_obj=WebDriverWait(driver,10,poll_frequency=0.2)
#until is a boolean method which will check for the cond to be true
submit_button=wait_obj.until(EC.element_to_be_clickable((By.ID,'button')))
submit_button.click()

driver.quit()
