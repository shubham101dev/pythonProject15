from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome()
browser.get("https://www.amazon.com/")
browser.maximize_window()
sliders = browser.find_elements(By.CLASS_NAME,'a-carousel-card')
print(len(sliders))
links=browser.find_elements(By.TAG_NAME,'a')
print(len(sliders))




