from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

service =Service()
driver=webdriver.Edge(service=service)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.minimize_window()
driver.close()
driver.quit()