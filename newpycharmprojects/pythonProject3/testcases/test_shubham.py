from pageobject.loginpage import Login
from selenium import webdriver
import pytest
from utilities.readproperties import Readconfig
from utilities.customlogger import Logclass
class Test:
    geturl=Readconfig.getapplicationURL()
    username=Readconfig.getusername()
    password=Readconfig.getpassword()


    def test_title(self,setup):
        log=Logclass.getthelog()
        self.driver=setup
        self.driver.get(self.geturl)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            log.info("********************title is match*********************")
            self.driver.save_screenshot("test_my.png")
        else:assert False

    def test_login1(self,setup):
        log = Logclass.getthelog()
        self.driver=setup
        self.driver.get(self.geturl)
        log.info("**************open URL****************")
        self.a=Login(self.driver)
        self.a.set_username(self.username)
        self.a.set_password(self.password)
        self.a.click_on_login()
        act_title=self.driver.title
        expected_title="Dashboard / nopCommerce administration"
        if act_title==expected_title:
            log.info("*************second title is match****************")
            self.driver.save_screenshot(".\\screenshots\\" + "test_shubham.png")
            assert True
        else:assert False
