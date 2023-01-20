from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import time
browser = webdriver.Chrome()
browser.get("https://www.amazon.com/ref=nav_logo")
#elem = browser.find_element(By.NAME,'field-keywords')
#elem.send_keys('iphone' + Keys.RETURN)
#elem = browser.find_element(By.ID,'twotabsearchtextbox')
#elem.send_keys('mobile' +Keys .RETURN)
#elem = browser.find_element(By.NAME,'field-keywords')
#elem.send_keys('books'+Keys.RETURN)
browser.find_element(By.PARTIAL_LINK_TEXT,"Care").click()
#browser.find_element(By.LINK_TEXT,"Careers").click()


time.sleep(10)

browser.quit()

