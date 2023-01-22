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
        self.driver.save_screenshot(".\\screenshots\\" + "test2.png")
        self.log.info("***********value insert*************")
        b=self.a.my_drop()
        c=Select(b)
        c.select_by_value("option2")
        self.driver.save_screenshot(".\\screenshots\\" + "test3.png")
        self.a.insert_click()

        self.log.info("***********msg print*************")
        time.sleep(5)





