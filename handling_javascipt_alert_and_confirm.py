from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# handling Javascript Alert boxes


# service = Service("C:\\Users\\611903295\\Downloads\\python_BDD_Testing\\chromedriver.exe")
# options = Options()
# options.binary_location = "C:\\Users\\611903295\\AppData\\Local\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
# driver = webdriver.Chrome(service=service, options=options)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,"input#name").send_keys("option3")
# driver.find_element(By.CSS_SELECTOR,"input.btn-style:nth-child(4)").click()
# alert=driver.switch_to.alert
# print(alert.text)
# assert "option3" in alert.text
# time.sleep(1)
# alert.accept()
# time.sleep(1)
# driver.minimize_window()
# driver.close()
# driver.quit()


# handling Javascript Confirm boxes

service = Service("C:\\Users\\611903295\\Downloads\\python_BDD_Testing\\chromedriver.exe")
options = Options()
options.binary_location = "C:\\Users\\611903295\\AppData\\Local\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"input#name").send_keys("option3")
driver.find_element(By.XPATH,"//input[@id='confirmbtn']").click()
alert=driver.switch_to.alert
print(alert.text)
time.sleep(1)
# alert.accept()
alert.dismiss()
driver.minimize_window()
driver.close()
driver.quit()

