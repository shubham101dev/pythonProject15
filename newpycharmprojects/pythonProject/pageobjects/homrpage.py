from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    button_view_account_xpath="//span[@id='acctBtnLabel']"
    button_signin_xpath="//a[normalize-space()='Sign-In']"
    textbox_username_xpath="//input[@id='sso_username']"
    textbox_password_xpath="//input[@id='ssopassword']"
    click_signin2_xpath="//input[@id='signin_button']"

    def __init__(self,driver):
        self.driver=driver


    def click_view_account(self):
        self.driver.find_element(By.XPATH,self.button_view_account_xpath).click()

    def click_sign_in(self):
        self.driver.find_element(By.XPATH,self.button_signin_xpath).click()



    def set_username(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)


    def click_sign_in2(self):
        self.driver.find_element(By.XPATH,self.click_signin2_xpath).click()
