from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


driver_location="C:\\Users\\611903295\\Downloads\\python_BDD_Testing\\chromedriver.exe"
options=Options()
options.binary_location="C:\\Users\\611903295\\AppData\\Local\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
driver=webdriver.Chrome(options=options,executable_path=driver_location)
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[contains(@id,'txtUsername')]").send_keys("admin")
driver.find_element(By.XPATH,"//input[contains(@id,'txtPassword')]").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR,"input[id*='btnLogin']").click()
print(driver.find_element(By.XPATH,"//h1[contains(text(),'Dashboard')]").text)
driver.minimize_window()
driver.close()
driver.quit()