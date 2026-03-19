from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
sleep(3)

driver.find_element(By.ID, "firstName").send_keys("Ravi")
driver.find_element(By.ID, "lastName").send_keys("Kishan")
driver.find_element(By.ID, "userEmail").send_keys("ravikishan@gmail.com")

driver.find_element(By.XPATH, "//label[text()='Male']").click()

driver.find_element(By.ID, "userNumber").send_keys("976569999")
driver.find_element(By.ID, "subjectsInput").send_keys("English")
sleep(3)
driver.find_element(By.XPATH, "//div[contains(text(),'English')]").click()

driver.find_element(By.XPATH, "//label[text()='Sports']").click()
driver.find_element(By.XPATH, "//label[text()='Reading']").click()

driver.find_element(By.ID, "currentAddress").send_keys("Jaipur Rajasthan")
driver.find_element(By.ID, "state").click()
driver.find_element(By.XPATH, "//div[text()='NCR']").click()

driver.find_element(By.ID, "city").click()
driver.find_element(By.XPATH, "//div[text()='Delhi']").click()

driver.find_element(By.ID, "submit").click()

sleep(3)
driver.quit()