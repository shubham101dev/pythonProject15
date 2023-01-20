from select import select
from selenium.webdriver.support.select import Select

from pageobject.firstpage import Login
from pageobject.next_page import Login1
import time


class Test_main:
    geturl="https://automationexercise.com/"
    username="shubham"
    password="shubham4121@gmail.com"

    # def test1(self,setup):
    #     self.driver=setup
    #     self.driver.get(self.geturl)
    #     act_title=self.driver.title
    #     if act_title=="Automation Exercise":
    #         assert True
    #     else:
    #         assert False

    # def test2(self,setup):
    #     self.driver=setup
    #     self.driver.get(self.geturl)
    #     self.a=Login(self.driver)
    #
    #
    #     self.a.click_on_signup()
    #     self.a.set_name_password(self.username,self.password)
    #     self.a.click_on_register()
    #     time.sleep(5)

    def test_form(self,setup):
        self.driver=setup
        self.driver.get(self.geturl)
        self.a=Login(self.driver)
        self.a.click_on_signup()
        self.a.set_name_password(self.username,self.password)
        self.a.click_on_register()
        self.b=Login1(self.driver)
        self.b.select_male()
        self.b.insert_password(password2="shubham@123")
        c=self.b.drop_day_select()
        selct=Select(c)
        selct.select_by_value('1')
        d=self.b.drop_month_select()
        s=Select(d)
        s.select_by_value('8')
        e=self.b.drop_year_select()
        s1=Select(e)
        s1.select_by_value("1996")
        self.b.two_check_box()
        self.b.few_down()
        time.sleep(10)











