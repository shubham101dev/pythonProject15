import time

from select import select
from selenium.webdriver.support.ui import Select
import pytest
from pageobjects.loginpage import AutoMation
from utilities.customlogger import Logclass
@pytest.mark.usefixtures('setup')
class Test():
    log = Logclass.getthelog()


    # def test001(self):
    #
    #     self.log.info("this is my test shubham")
    #     act_title=self.driver.title
    #     if act_title=="Practice Page":
    #         assert True
    #         self.log.info("********title is match")
    #         self.driver.save_screenshot(".\\screenshots\\" + "test_pass.png")
    #     else:
    #         self.log.info("********title is not match")
    #         self.driver.save_screenshot(".\\screenshots\\" + "test_pass.png")
    #         assert False

    def test_002(self):
        self.a=AutoMation(self.driver)
        self.a.click_on_radio2()
        self.a.click_allcheckbox()
        self.a.textbox_1(value="shubham")
        b=self.a.my_drop()
        c=Select(b)
        c.select_by_value("option2")
        time.sleep(5)





