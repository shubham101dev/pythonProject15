from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
# driver=webdriver.Firefox()
serv=Service(r"C:\\Users\\nikub\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\chromedriver.exe")
driver=webdriver.Chrome(service=serv)
driver.get("https://www.trivago.in/?__wr=21&tc=26&cip=91030227040912&cip_tc=12891-101-101_privacy_1672067409401000000&cip_ext_id=1672067409401000000&mfadid=adm")
driver.find_element(By.XPATH,"//label[@for='accommodation-type-hotel']").click()
driver.find_element(By.LINK_TEXT,"Hotels in Pune").click()
print(f"{driver.current_url}")
driver.find_element(By.XPATH,"").click()

driver.maximize_window()


time.sleep(10)
driver.close()
driver.quit()