from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# handling check boxes


service = Service("C:\\Users\\611903295\\Downloads\\python_BDD_Testing\\chromedriver.exe")
options = Options()
options.binary_location = "C:\\Users\\611903295\\AppData\\Local\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
# all_checkbox = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
# print(len(all_checkbox))

# case:-1

# for checkbox in all_checkbox:
#     time.sleep(1)
#     print(checkbox.get_property(name='value'))
#     checkbox.click()

# case:-2

# for checkbox in all_checkbox:
#     if checkbox.get_attribute('value') == 'option2':
#         checkbox.click()
#         assert checkbox.is_selected()  # this will validate whether the checkbox selected  or not
#         time.sleep(1)

# driver.minimize_window()
# driver.close()
# driver.quit()

# handling radio button

# here the index starts from 0


radio = driver.find_elements(By.NAME, "radioButton")

radio[2].click()
radio[2].is_selected()
radio[2].is_enabled()
print(radio[2].get_property(name="value"))

driver.minimize_window()
driver.close()
driver.quit()
