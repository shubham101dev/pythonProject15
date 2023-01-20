import pytest
from selenium import  webdriver
from calc import*
class Test_id001_login:
    baseurl="https://admin-demo.nopcommerce.com/admin/"
    username="admin@yourstore.com"
    password="admin"

    def test_homepagetitle(self):
        self.driver=webdriver.Chrome()
        self.driver.get(self.baseurl)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Your store. Login":
            assert True
        else:
            assert False
    def test_login(self):
        self.driver=webdriver.Chrome()
        self.driver.get(self.baseurl)
        self.lp=Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.driver.close()








