import pytest

class Homepage:
    def test__001login(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        driver=webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
        driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
        driver.find_element(By.XPATH,"//input[@id='login-button']").click()
        driver.quit()


    def test__002login(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        driver=webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("locked_out_user")
        driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
        driver.find_element(By.XPATH,"//input[@id='login-button']").click()
        driver.quit()

    def test__003login(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        driver=webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("problem_user")
        driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
        driver.find_element(By.XPATH,"//input[@id='login-button']").click()
        driver.quit()

    def test__004login(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        driver=webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("performance_glitch_user")
        driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
        driver.find_element(By.XPATH,"//input[@id='login-button']").click()
        driver.quit()

