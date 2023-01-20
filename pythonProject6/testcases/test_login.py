import time

from selenium import webdriver
import pytest
from Pageobjects.loginpage import Login
from testcases.conftest import setup

class Test_001login:
    geturl="https://heaptrace.kiwihr.com/sign-in"
    username="heaptrace@domain.com"
    password="Shubham@1001"

    # def test1(self,setup):
    #     self.driver=setup
    #     self.driver.get(self.geturl)
    #     self.url=self.driver.current_url
    #     time.sleep(5)

    def test2(self,setup):
        self.driver=setup
        self.driver.get(self.geturl)
        self.a=Login(self.driver)
        self.a.set_username(self.username)
        self.a.set_password(self.password)
        self.a.button_login()
        time.sleep(5)














