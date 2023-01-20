from selenium import webdriver
from selenium.webdriver.common.by import By
class Login:
    button_home_xpath="//a[normalize-space()='Home']"
    button_product_xpath="//a[@href='/products']"
    signup_button_xpath="//a[normalize-space()='Signup / Login']"
    textbox_username_xpath="//input[@placeholder='Name' and @name='name']"
    textbox_password_xpath="//input[@data-qa='signup-email']"
    button_register_signup_xpath="//button[@data-qa='signup-button' and @class='btn btn-default' and @type='submit']"

    def __init__(self,driver):
        self.driver=driver

    def click_home(self):
        self.driver.find_element(By.XPATH,self.button_home_xpath).click()

    def click_products(self):
        self.driver.find_element(By.XPATH,self.button_product_xpath).click()

    def click_on_signup(self):
        self.driver.find_element(By.XPATH,self.signup_button_xpath).click()

    def set_name_password(self,username,password):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)

    def click_on_register(self):
        self.driver.find_element(By.XPATH,self.button_register_signup_xpath).click()





