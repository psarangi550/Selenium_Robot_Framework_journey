from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

# options=Options()
# options.binary_location="C:\\Users\\611903295\\AppData\\Local\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
# service=Service("C:\\Users\\611903295\\Downloads\\python_BDD_Testing\\chromedriver.exe")
service=Service()
driver=webdriver.Edge(service=service)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/cart")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"input.search-keyword").send_keys("ber")
time.sleep(4)
all_item=driver.find_elements(By.XPATH,"//div[@class='products']//div[@class='product']")
print(len(all_item))
all_btn=driver.find_elements(By.XPATH,"//div[@class='product-action']/button[@type='button']")
for btn in all_btn:
    btn.click()
cart_value=driver.find_element(By.XPATH,"//strong[text()='3']").text
assert cart_value == "3"
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
ww=WebDriverWait(driver=driver,timeout=6)
# time.sleep(3)
ww.until(expected_conditions.presence_of_element_located(locator=(By.XPATH,"//input[@class='promoCode']")))
driver.find_element(By.CSS_SELECTOR,"input.promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,"promoBtn").click()
ww.until(expected_conditions.presence_of_element_located(locator=(By.CLASS_NAME,"promoInfo")))
# time.sleep(5)
result=driver.find_element(By.CLASS_NAME,"promoInfo").text
assert result == "Code applied ..!"
driver.close()
driver.quit()
