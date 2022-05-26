from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

driver_location = "C:\\Users\\611903295\\Downloads\\python_BDD_Testing\\chromedriver.exe"
options = Options()
options.binary_location="C:\\Users\\611903295\\AppData\\Local\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
driver=webdriver.Chrome(options=options,executable_path=driver_location)
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
driver.find_element(By.CSS_SELECTOR,"input[id='txtUsername']").send_keys("admin")
driver.find_element(By.CSS_SELECTOR,"input[id='txtPassword']").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR,"input[id='btnLogin']").click()
time.sleep(2)
driver.minimize_window()
time.sleep(1)
driver.close()
