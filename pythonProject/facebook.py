from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("https://demo.automationtesting.in/Register.html")
# driver.maximize_window()
# first_name=driver.find_element(By.TAG_NAME,"input").send_keys("shubham")
# last_name=driver.find_element(By.TAG_NAME,"more").send_keys("more")
# time.sleep(10)
# driver.close()
serv=Service("C:\chromedriver.exe")
driver=webdriver.Chrome(service=serv)
driver.get("https://www.facebook.com/")
driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("shubhammore")
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abcdefgh")
# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("shubhammore")
driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("nikhil")
# links=driver.find_elements(By.TAG_NAME,"li")
# print(len(links))
time.sleep(10)
driver.close()
