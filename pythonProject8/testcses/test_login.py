import pytest
from selenium import webdriver
from pageobject.loginpage import Login
from testcses.conftest import setup
class Test_001:
    geturl="https://practicetestautomation.com/practice-test-login/"
    username="student"
    password="Password123"
    @pytest.mark.skip
    def test_homepagetitle(self,setup):
        self.driver=setup
        self.driver.get(self.geturl)
        act_title=self.driver.title
        if act_title=="Test Login | Practice Test Automation":
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_hompag1.png")
            self.driver.close()
            assert False
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

