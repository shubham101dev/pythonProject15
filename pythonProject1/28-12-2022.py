# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver import ActionChains
# driver=webdriver.Chrome()
# driver.get("https://seleniumbase.io/demo_page")
# parent=driver.find_element(By.ID,"div.dropbtn").click()
# s=ActionChains(driver)
#
#
#
# time.sleep(10)



from selenium import  webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
driver.get("http://www.qafeast.com/demo")
driver.maximize_window()
driver.find_element(By.XPATH,"//label[text()='Drag & Drop']").click()
source=driver.find_element(By.XPATH,"//p[normalize-space()='Java']")
target=driver.find_element(By.XPATH,"//div[contains(@class,'dropable-box')]//div[2]")
s1=driver.find_element(By.XPATH,"//p[text()='Python']")
t1=driver.find_element(By.XPATH,"//div[contains(@class,'dropable-box')]//div[1]")
action=ActionChains(driver)
action.drag_and_drop(source,target).perform()
time.sleep(10)
action2=ActionChains(driver)
action2.drag_and_drop(s1,t1).perform()
time.sleep(5)