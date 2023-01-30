import time
from utilities.readproperties import Readconfig
import pytest
from utilities.customlogger import Logclass
from pageobject.login_page import Login
from pageobject.second_page import Second
from selenium.webdriver.common.action_chains import ActionChains
@pytest.mark.usefixtures('setup')
class Test2:
    element="Copyright © ProtoCommerce 2018"
    log = Logclass.getthelog()

    def test2(self):
        time.sleep(2)
        self.c=Login(self.driver)
        self.c.set_username(Readconfig.get_username())
        self.c.set_password(Readconfig.get_password())
        self.c.click_login()
        print(self.driver.title)
        act_title=self.driver.title
        if act_title=="LoginPage Practise | Rahul Shetty Academy":
            assert True
        else:
            assert False
        time.sleep(5)



    def test3(self):
        self.log.info("url is open")
        self.a=Login(self.driver)
        self.a.set_username(Readconfig.get_username())
        self.a.set_password(Readconfig.get_password())
        self.a.click_login()
        time.sleep(5)
        self.log.info("login successful")
        self.b=Second(self.driver)
        self.b.click_on_addcart()
        time.sleep(5)



