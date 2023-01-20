class Test_login:
    def login001(self):
        import pytest

        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.select import Select
        import  time
        driver=webdriver.Chrome()
        driver.get("http://j2store.net/v3/administrator/index.php")
        driver.find_element(By.XPATH,"//input[@id='mod-login-username']").send_keys("manager")
        driver.find_element(By.XPATH,"//input[@id='mod-login-password']").send_keys("manager")
        driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
        time.sleep(10)
        driver.close()

