from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.remote_connection import
import time



driver=webdriver.Firefox()
driver.get("https://seleniumbase.io/demo_page")
s1=driver.find_element(By.XPATH,"//input[@id='myTextInput2']")
print("is selected",s1.is_enabled())



# c1=driver.find_element(By.XPATH,"//a[@id='dropOption3']")
# print("displayed",c1.is_displayed())
# c2=driver.find_element(By.XPATH,"//input[@id='myTextInput2']")
# print("enabled",c2.is_enabled())
# p=driver.find_element(By.XPATH,"//button[@id='myButton']")
# print(p.is_enabled())


# s1=driver.find_element(By.ID,'dropOption1')
# print("displayed ::",s1.is_displayed())
# s2=driver.find_element(By.XPATH,"//*[@id='dropOption2']")
# print("displayed or not",s2.is_displayed())
# print("enable or not",s2.is_enabled())
# s3=driver.find_element(By.XPATH,"//input[@id='radioButton2']")
# print("this button enable or not",s3.is_enabled())
# s4=driver.find_element(By.XPATH,"/html/body/form/table/tbody/tr[2]/td[2]/input")
# print("enable or not",s4.is_enabled())
# s5=driver.find_element(By.XPATH,"//input[@id='myTextInput2']")
# print("enable",s5.is_enabled())


time.sleep(10)
driver.close()
driver.quit()
