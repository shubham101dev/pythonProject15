import time

import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from pageobjects.homepage import Main
@pytest.mark.usefixtures('setup')
class Test_010:
    geturl="http://tutorialsninja.com/demo/index.php?route=common/home"
    username="niku123@gmail.com"
    password="12345678"

    def test1(self):

        act_title=self.driver.title
        if act_title=="Your Store":
            assert True
        else:
            assert False

    def test2(self):

        self.a=Main(self.driver)
        self.a.click_on_myaccount_and_login(self.username,self.password)
        time.sleep(5)


