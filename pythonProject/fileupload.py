import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("https://the-internet.herokuapp.com/upload")

fileInput = driver.find_element(By.ID, 'file-upload')
button = driver.find_element(By.ID, 'file-submit')

fileInput.send_keys(r"C:\s.jpg")

button.click()

time.sleep(10)
