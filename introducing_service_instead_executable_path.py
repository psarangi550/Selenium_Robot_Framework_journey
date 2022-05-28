from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# here we are importing the Service class from chrom  module
from selenium.webdriver.chrome.options import Options
# importing the options from Options class

options=Options()
options.binary_location="C:\\Users\\611903295\\AppData\\Local\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
service=Service("C:\\Users\\611903295\\Downloads\\python_BDD_Testing\\chromedriver.exe")
driver=webdriver.Chrome(service=service,options=options)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.minimize_window()
driver.close()
driver.quit()
