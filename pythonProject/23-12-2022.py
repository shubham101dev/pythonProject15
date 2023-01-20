
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
driver=webdriver.Chrome()
driver.get("https://www.amazon.com/")
print(f"my page title is\n\n\n::{driver.title}")
s1=driver.find_element(By.ID,"nav-cart-text-container").click()
# time.sleep(5)
driver.back()
time.sleep(5)
s2=driver.find_element(By.ID,"glow-ingress-line2").click()


driver.back()
time.sleep(10)

