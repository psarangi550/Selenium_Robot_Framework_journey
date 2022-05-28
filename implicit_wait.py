from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

service = Service()
driver = webdriver.Edge(service=service)
driver.implicitly_wait(5)  # here providing the implicitly_wait for 5 seconds
# this will be applied for all the driver objects
# hence this considered as the global wait
# wait until 5 mins if the object is not loaded
# else proceed if the object is loaded
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"input.search-keyword").send_keys("ber")
# time.sleep(5)
all_items=driver.find_elements(By.XPATH,"//div[@class='products']/div[@class='product']")
print(len(all_items))
assert len(all_items)== 3
all_btn=driver.find_elements(By.XPATH, "//div[@class='products']/div[@class='product']/div[3]/button")
for btn in all_btn:
    btn.click()
    time.sleep(1)
time.sleep(1)
assert driver.find_element(By.XPATH,"//strong[text()='3']").text == '3'
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR,"input.promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,"promoBtn").click()
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
assert driver.find_element(By.CLASS_NAME,"promoInfo").text == "Code applied ..!"
driver.close()
driver.quit()