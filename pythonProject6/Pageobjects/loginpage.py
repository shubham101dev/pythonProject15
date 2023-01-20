from selenium.webdriver.common.by import By
from selenium import webdriver

class Login:
    textbox_username_Xpath="//input[@id='login' and @type='email']"
    textbox_password_xpath="//input[@id='password']"
    button_login_Xpath="//button[normalize-space()='Sign in']"

    def __init__(self,driver):
        self.driver=driver

    def set_username(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_Xpath).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)

    def button_login(self):
        self.driver.find_element(By.XPATH,self.button_login_Xpath).click()




