import time
from pageobjects.homepage import Login
from utilities.readproperties import Readconfig
from testcases.confest import setup
from utilities.customlogger import Logclass


class Test_login(Readconfig):
    geturl=Readconfig.getapplicationURl()
    username=Readconfig.getusername()
    password=Readconfig.getpassword()




    def test_homepagetitle(self,setup):
        self.driver=setup
        log=self.getthelog()
        log.info("this is my test shubham")

        # self.driver=setup
        self.driver.get(self.geturl)
        log.info("************open url**********")
        a=self.driver.title
        if a=="Oracle | Cloud Applications and Cloud Platform":
            assert True
            log.info('*****test case pass******')

        else:
            log.info('*****test case fail******')
            assert False

    def test_homepagetitle11(self,setup):
        self.driver=setup
        self.driver.get(self.geturl)
        a=self.driver.title
        if a=="shubham":
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_fail3.png")
            log.info('*****screen captured********')
            assert False

    def test_login005(self,setup):
        self.driver=setup
        self.driver.get(self.geturl)
        self.b=Login(self.driver)
        self.b.click_on_viewaccount()
        self.b.click_signin()
        self.b.set_username(self.username)
        self.b.set_password(self.password)
        self.b.click_on_final_signin()
        log.info('***************')




