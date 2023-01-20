import pytest

from selenium.webdriver.common.by import By
import time
from selenium import webdriver
import requests
class Login:
    code_xpath="//span[@id='totp']"
    link_xpath="//a[normalize-space()='seleniumbase.io/realworld/login']"
    username_xpath="//input[@id='username']"
    password_xpath="//input[@id='password']"
    sign_in_xpath="//a[@id='log-in']"


    def __init__(self,driver):
        self.driver=driver




    def click_on_link(self):
        self.driver.find_element(By.XPATH,self.link_xpath).click()



    def set_username(self,username):
        self.driver.find_element(By.ID,"username").send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.XPATH,self.password_xpath).send_keys(password)

    def set_code(self,code):
        self.driver.find_element(By.XPATH,"//input[@id='totpcode']").send_keys(code)

    def click_signin(self):
        self.driver.find_element(By.XPATH,self.sign_in_xpath).click()

    def set_code_2fa(self):















