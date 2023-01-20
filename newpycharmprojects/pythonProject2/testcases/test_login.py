from testcases.confest import setup
from pageobject.loginpage import Test_login
from selenium import webdriver
class Login():
    geturl="https://seleniumbase.io/realworld/login#"
    username="demo_user"
    password="secret_pass"

    def test1(self,setup):
        self.driver=setup
        self.driver.get(self.geturl)
        act_title=self.driver.title
        if act_title=="Login / MFA Demo App":
            assert True
        else:
            assert False



