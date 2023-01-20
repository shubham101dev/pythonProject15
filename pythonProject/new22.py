from selenium import  webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/")
sliders=driver.find_elements(By.CLASS_NAME,"_1mIbUg")
print(len(sliders))

driver.find_element(By.PARTIAL_LINK_TEXT,"Us").click()
print(f"my URL::{driver.current_url}")
driver.find_element(By.XPATH,"//a[normalize-space()='Login']").click()
time.sleep(5)
driver.close()
