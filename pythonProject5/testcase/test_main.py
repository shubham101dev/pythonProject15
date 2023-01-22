import time

import pytest
from utilities.customlogger import Logclass

from pageobject.login_page import Login
from utilities.excel_methods import ExcelMethods
sheet_name='shubham'
@pytest.mark.usefixtures('setup')
class Test_login:
    log=Logclass.getthelog()
    @pytest.mark.parametrize("sr_No,username,password,condition",ExcelMethods('shubham').get_parametrize_list())
    def test1(self,sr_No,username,password,condition):
        self.log.info("url is open")
        self.a=Login(self.driver)
        self.a.set_username(username)
        self.log.info("username is insert ")
        self.a.set_password(password)
        self.log.info("password is insert ")
        self.a.click_login()
        time.sleep(5)
        if condition=="+":
            if "ProtoCommerce" in self.driver.title:
                self.log.info("test case pass")
                status=True
            else:
                self.driver.save_screenshot('screenshot\\test_login.png',mode="w")
                self.log.critical("test case fail")
                status=False
        elif condition=="-":
            if "LoginPage Practise | Rahul Shetty Academy" in self.driver.title:
                status=True
                self.log.info("test case pass")
            else:
                self.driver.save_screenshot('screenshot\\test_login1.png',mode="w")
                self.log.critical("test case fail")
                status=False
        ExcelMethods(sheet_name).update_result_in_excel(sr_No,status)
        assert status


