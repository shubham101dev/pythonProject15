from selenium import webdriver
from testcases.conftest import setup
from pageobjects.loginpage import Login
from utilities.readproperties import ReadConfig
from utilities.customlogger import Logclass

class Test__001():
    geturl =ReadConfig.getApplicationURL()
    username =ReadConfig.get_username()
    password =ReadConfig.get_password()

    log=Logclass.getthelog()


    def test2(self, setup):
        self.driver = setup
        self.driver.get(self.geturl)
        act_title = self.driver.title
        expected_title = "osCommerce Online Merchant Administration Tool"
        if act_title in expected_title:
            self.log.info('***********')
            assert True
        else:
            assert False


    def test1(self, setup):
        self.driver = setup
        self.driver.get(self.geturl)
        self.log.info('********title is open')
        act_title = self.driver.title
        expected_title = "osCommerce Online Merchant Administration Tool"
        if act_title == expected_title:
            assert True
            self.log.info('title is match')
        else:
            assert False


    def test3(self,setup):
        self.driver =setup
        self.driver.get(self.geturl)
        self.a = Login(self.driver)
        self.a.set_username(self.username)
        self.a.set_password(self.password)
        self.a.click_on_login()
