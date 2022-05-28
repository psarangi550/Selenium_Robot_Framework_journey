from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

driver_location="C:\\Users\\611903295\\Downloads\\python_BDD_Testing\\chromedriver.exe"
options = Options()
options.binary_location="C:\\Users\\611903295\\AppData\\Local\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
driver=webdriver.Chrome(options=options,executable_path=driver_location)
driver.get("https://www.easemytrip.com/?utm_source=google&utm_medium=cpc&utm_campaign=788997081&utm_content=39319940377&utm_term=ease%20my%20trip&utm_campaign=788997081&utm_source=g_c&utm_medium=cpc&utm_term=e_ease%20my%20trip&adgroupid=39319940377&gclid=EAIaIQobChMItNafvtH_9wIV13wrCh3AXQZpEAAYASAAEgKOPvD_BwE")
driver.find_element(By.ID,"FromSector_show").clear()
driver.find_element(By.ID,"FromSector_show").send_keys("bhu")
time.sleep(2)
all_cities = driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']/div[1]/span[2]")
print(all_cities)
print(type(all_cities))
print(len(all_cities))
# driver.close()
for city in all_cities:
    if "Bhubaneswar" in city.text:
        city.click()
        break
#
props=driver.find_element(By.ID,"FromSector_show").get_property(name='value')
# result=driver.find_element(By.ID,"FromSector_show").get_attribute('value')
print(props)
assert "Bhubaneswar" in props
driver.minimize_window()
driver.close()
driver.quit()