from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv=Service("C:\chromedriver.exe")
driver=webdriver.Chrome(service=serv)
driver.get("https://seleniumbase.io/demo_page")
# driver.find_element(By.PARTIAL_LINK_TEXT,"Features").click()
# driver.back()
driver.find_element(By.CSS_SELECTOR,"button[id=myButton]").click()
# driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("123456")
# driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_email]").send_keys("123456")
# driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("shubham")
# driver.find_element(By.CSS_SELECTOR,"button._42ft[data-testid=royal_login_button]").click()
time.sleep(5)
driver.close()
