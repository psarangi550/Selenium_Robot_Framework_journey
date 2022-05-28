from selenium import webdriver
from selenium.webdriver.support.select import Select
# importing the Select class from select module of selenium.webdriver.support
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

driver_location = "C:\\Users\\611903295\\Downloads\\python_BDD_Testing\\chromedriver.exe"
options = Options()
options.binary_location = "C:\\Users\\611903295\\AppData\\Local\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
driver = webdriver.Chrome(options=options, executable_path=driver_location)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
dropdown=Select(driver.find_element(By.ID,"dropdown-class-example"))
dropdown.select_by_visible_text("Option1")
time.sleep(1)
dropdown.select_by_index(2)
time.sleep(1)
dropdown.select_by_value("option3")
time.sleep(1)
driver.minimize_window()
driver.close()
driver.quit()