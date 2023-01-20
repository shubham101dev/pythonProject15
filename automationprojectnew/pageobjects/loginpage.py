from selenium.webdriver.common.by import By
import pytest

class Login:
    textbox_username_xpath="//input[@name='username']"
    textbox_password_xpath="//input[@name='password']"
    button_login_xpath="//button[@id='tdb1']"

    def __init__(self,driver):
        self.driver=driver

    def set_username(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)

    def click_on_login(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()


