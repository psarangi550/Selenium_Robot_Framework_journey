from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options

driver = webdriver.Edge()
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys("admin")
driver.find_element(By.XPATH,"//input[@id='txtPassword']").send_keys("admin123")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
driver.minimize_window()
driver.close()
driver.quit()