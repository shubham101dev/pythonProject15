from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Firefox()
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys('shubham')
driver.find_element(By.XPATH,"//input[@ng-model='LastName']").send_keys('more')
driver.find_element(By.CSS_SELECTOR,"textarea[ng-model='Adress']").send_keys('pune')
driver.find_element(By.XPATH,"//input[@ng-model='EmailAdress']").send_keys('abc123@gmail.com')
driver.find_element(By.XPATH,"//input[@ng-model='Phone']").send_keys('1234567891')
driver.find_element(By.XPATH,"//input[@value='Male']").click()
driver.find_element(By.ID,"checkbox1").click()
driver.find_element(By.XPATH,"//div[@id='msdd']").click()
driver.find_element(By.XPATH,"//a[text()='Hindi']").click()
driver.find_element(By.XPATH,"//a[text()='Thai']").click()
driver.find_element(By.XPATH,"//div[@class='form-group']/child::label/parent::div/ancestor::form").click()
a=driver.find_element(By.XPATH,"//select[@id='Skills' or @ng-model='Skill']")
drop=Select(a)
drop.select_by_value('Android')
alloptions=drop.options
for i in alloptions:
    print(i.text)
driver.find_element(By.XPATH,"//span[@aria-haspopup='true']").click()
d1=driver.find_element(By.ID,"select2-country-results")
d2=Select(d1)
d2.select_by_index(1)








time.sleep(5)
driver.quit()




