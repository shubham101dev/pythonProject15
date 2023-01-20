# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# driver=webdriver.Chrome(r"C:\Users\nikub\AppData\Local\Programs\Python\Python311\chromedriver.exe")
# driver.get("https://www.flipkart.com/")
# driver.maximize_window()
# print(f"page title:{driver.title}")
# # s=driver.find_elements(By.NAME,"q")
# driver.close()
# from selenium import  webdriver
# import time
# driver=webdriver.Chrome()
# driver.get("https://www.amazon.com/")
# driver.maximize_window()
# print(f"page title:{driver.title}")
# print(f"page URL:{driver.current_url}")
#
#
# driver.get("https://www.flipkart.com/")
#
# print(f"page title:{driver.title}")
# print(f"page URL:{driver.current_url}")
#
# # time.sleep(5)
# driver.close()
from selenium import webdriver
import  time
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.maximize_window()
time.sleep(5)
driver.close()












