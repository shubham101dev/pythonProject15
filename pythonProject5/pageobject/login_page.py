from selenium.webdriver.common.by import By

from utilities.readproperties import Readconfig

class Login:
    def __init__(self,driver):
        self.driver=driver

    def set_username(self,username):
        self.driver.find_element(By.XPATH,Readconfig.get_username_xpath()).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.XPATH,Readconfig.get_password_xpath()).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,Readconfig.get_box_xpath()).click()
        self.driver.find_element(By.XPATH,Readconfig.get_signin_xpath()).click()


