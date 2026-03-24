from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opts)
# driver.get("https://abc.com")
# driver.maximize_window()
#
# wait=WebDriverWait(driver,10)
# loadingcircles=wait.until(EC.invisibility_of_element_located((By.ID," preloader-animated_svg__svg3")))
#
# title_abc=driver.find_element(By.XPATH,"//span[text()='ABC SHOWS, SPECIAL & MORE'] ")
#
# assert "SPECIALS" in title_abc.text, "the text is not visible"
#
# print('working fine')
# driver.quit()

driver.get("https://demoqa.com/dynamic-properties")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

enable_before=driver.find_element(By.ID,'enableAfter')
print(enable_before.is_enabled())

enablebtn=wait.until(EC.element_to_be_clickable((By.ID,'enableAfter')))

if enablebtn.is_enabled():
    enablebtn.click()
    print(enablebtn.text)

visible_ele=wait.until(EC.visibility_of_element_located(By.ID,'visibleAfter'))
print(visible_ele.text)

