from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
service = Service()
driver=webdriver.Edge(service=service)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@class='search-keyword']").send_keys("ber")
time.sleep(2)
displayed_item=driver.find_elements(By.XPATH,"//div[@class='products']/div[@class='product']")
display_btn=driver.find_elements(By.XPATH,"//div[@class='products']/div[@class='product']/div[3]/button[@type='button']")

print(len(displayed_item))
for btn in display_btn:
    btn.click()
    time.sleep(2)

print(driver.find_element(By.XPATH, "//strong[text()='3']").text)

# assert driver.find_element(By.XPATH, "//tbody[contains(@style,'user-select')]/tr[1]/td[3]/strong[text(),'3']").text == "3"
driver.close()
driver.quit()