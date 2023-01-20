# import time
#
# from selenium import  webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://www.facebook.com/")
# driver.maximize_window()
# email_element=driver.find_element(By.ID,"email")
# email_element.send_keys("shubham4121@gmail.com")
# password_element=driver.find_element(By.ID,"pass")
# password_element.send_keys("7498333541")
# login=driver.find_element(By.NAME,"login")
#
#
# login.click()
# time.sleep(10)
# driver.close()



# import time
#
# from selenium import  webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://www.facebook.com/")
# driver.maximize_window()
# email_element=driver.find_element(By.ID,"email")
# email_element.send_keys("shubham4121@gmail.com")
# password_element=driver.find_element(By.ID,"pass")
# password_element.send_keys("7498333541")
# login=driver.find_element(By.NAME,"login")
# login.click()
# time.sleep(10)
# driver.close()


import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window()
# username=driver.find_element(By.NAME,"username")
# username.send_keys("Admin")
# password=driver.find_element(By.NAME,"password")
# password.send_keys("admin123")



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver=webdriver.Chrome()
# driver.get("https://www.amazon.com/ref=nav_logo")
# driver.maximize_window()
# search=driver.find_element(By.ID,"twotabsearchtextbox")
# search.send_keys("iphone")
# c1=driver.find_element(By.ID,"nav-search-submit-button")
# c1.click()
# time.sleep(5)
# driver.close()



from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.amazon.com/gp/goldbox?ref_=nav_cs_gb")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"img[alt='Today only: Popular books on Kindle']").click()
driver.find_element(By.CSS_SELECTOR,"span.a-truncate-cut").click()
driver.find_element(By.CSS_SELECTOR,"input.a-button-input").click()
driver.back()
driver.back()
driver.back()
driver.find_element(By.CSS_SELECTOR,"a#nav-logo-sprites").click()
driver.find_element(By.CSS_SELECTOR,"span#nav-link-accountList-nav-line-1").click()
driver.find_element(By.CSS_SELECTOR,"input#ap_email").send_keys("sonarshubham101@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input#continue").click()
driver.find_element(By.CSS_SELECTOR,"input[id='ap_password']").send_keys("shubham@1001")
driver.find_element(By.CSS_SELECTOR,"input.a-button-input").click()
print(f"my page url:{driver.current_url}")
print(f"my page title\n\n{driver.title}")
driver.find_element(By.CSS_SELECTOR,"a.nav-a").click()
driver.back()
print(f"my page url:{driver.current_url}")


time.sleep(10)
driver.close()