# import pyotp
# import time
#
# import pytest
#
# from utilities.readproperties import Readconfig
# from utilities.customlogger import Logclass
# from pageobjects.mypage import Login
# from testcases.conftest import setup
# from pageobjects.second_main_page import My_Mainpage
#
# class Test_login():
#     geturl =Readconfig.getapplicationURL()
#     username =Readconfig.getusername()
#     password =Readconfig.getpassword()
#
#     log = Logclass.getthelog()
#
#
#     def test_title(self,setup):
#         self.driver=setup
#         self.driver.get(self.geturl)
#         self.log.info("*********open URL***********")
#         act_title=self.driver.title
#         if act_title=="Login / MFA Demo App":
#             assert True
#             self.log.info("*********title is match***********")
#             self.driver.save_screenshot(".\\screenshots\\"+"test_title.png")
#         else:
#             assert False
#
#
#     def test_login(self,setup):
#         self.driver=setup
#         self.driver.get(self.geturl)
#         self.a=Login(self.driver)
#         self.a.set_username(self.username)
#         self.a.set_password(self.password)
#         secret_key="GAXG2MTEOR3DMMDG"
#         totp = pyotp.TOTP(secret_key)
#         code = totp.now()
#         self.a.set_code(code)
#         self.a.button_sign_up()
#         self.log.info("*********screenshot captured**************")
#         self.driver.save_screenshot(".\\screenshots\\" + "login.png")
#         self.b=My_Mainpage(self.driver)
#         self.b.click_on_demopage()
#         print(self.driver.title)
#         print(self.driver.current_url)
#         time.sleep(5)
