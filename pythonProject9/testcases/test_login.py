import time
# import pyotp
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from pageobjects.first_page import Login
class Test:
    geturl = "https://seleniumbase.io/realworld/signup"
    username ="demo_user"
    password ="secret_pass"

    # def test1_check_title(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.geturl)
    #     act_title = self.driver.title
    #     if act_title == "Login / MFA Demo App":
    #         assert True
    #     else:
    #         assert False
    #     self.driver.close()

    def test_my_login(self,setup):
        self.driver=setup
        self.driver.get(self.geturl)
        self.a.click_on_link()
        self.a=Login(self.driver)

        self.a.set_username(self.username)
        self.a.set_password(self.password)
        secret_key="GAXG2MTEOR3DMMDG"
        totp=pyotp.now()
        totp=pyotp.TOTP(secret_key)
        # Generate the current 2FA code
        code = totp.now()
        # Enter the 2FA code
        self.a.set_code(code)
        time.sleep(5)