import logging

import pytest
import self as self
from selenium import webdriver
from pageobjects.homrpage import Login
from utilities.readproperties import Readconfig
from utilities.customlogger import Logclass


class Test_003():
    geturl=Readconfig.getapplicationURL()
    username=Readconfig.get_username()
    password=Readconfig.get_password()

    log=Logclass.getthelog()



    def test_homepagetitle(self,get_driver):

        self.driver=get_driver

        self.log.info("****************")
        self.driver.get(self.geturl)
        act_title=self.driver.title
        if act_title=="Oracle India | Cloud Applications and Cloud Platform":
            self.log.info("*********title is match************")
            self.driver.save_screenshot("screenshot"+"sh.png")
            assert True
        else:
            assert False


    def test_login002(self,get_driver):
        self.driver=get_driver
        self.driver.get(self.geturl)
        self.log.info("********print")
        self.a=Login(self.driver)
        self.a.click_view_account()
        self.a.click_sign_in()
        self.a.set_username(self.username)
        self.a.set_password(self.password)
        self.a.click_sign_in2()




