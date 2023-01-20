import pytest
from selenium import webdriver
from pageobject.loginpage import Login
from testcase.confest import setup
class Test_001:
    geturl="https://demo.automationtesting.in/Index.html"
    username="sss"


    def test1(self,setup):
        self.driver=setup
        self.driver.get(self.geturl)
        print(self.driver.title)
        self.a=Login(self.driver)
        self.a.set_username(self.username)
        self.a.click_login()

    def test2(self,setup):
        self.driver=setup
        self.driver.get(self.geturl)
        print(self.driver.title)
        self.a=Login(self.driver)
        self.a.set_username(self.username)
        self.a.click_login()
        self.a.click_on_webtable()




    @pytest.mark.skip
    def test_login5(self,setup):
        import time
        self.driver=setup
        self.driver.get(self.geturl)
        self.a=Login(self.driver)
        self.a.set_username(self.username)
        self.a.set_password(self.password)
        self.a.click_login()
        self.a.click2_practice()
        time.sleep(2)
        self.driver.close()
