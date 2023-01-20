import pytest
from selenium.webdriver.common.by import By


class Test_login:
    def login001(self):
        from selenium import webdriver
        import  time
        driver=webdriver.Chrome()
        driver.get("http://j2store.net/v3/administrator/index.php")
        driver.find_element(By.XPATH,"//input[@id='mod-login-username']").send_keys("manager")
        driver.find_element(By.XPATH,"//input[@id='mod-login-password']").send_keys("manager")
        driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
        time.sleep(10)
        driver.quit()


    def login_03(self):
        from selenium import webdriver
        import  time
        driver=webdriver.Chrome()
        driver.get("http://j2store.net/v3/administrator/index.php")
        driver.find_element(By.XPATH,"//input[@id='mod-login-username']").send_keys("manager")
        driver.find_element(By.XPATH,"//input[@id='mod-login-password']").send_keys("manager")
        driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
        time.sleep(10)
        driver.quit()

# a=Test_login()
# a.login001()
