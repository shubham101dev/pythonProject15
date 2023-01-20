from selenium import webdriver
from PageObjects.Loginpage import Login
from PageObjects.registerpage import Loginsh
from Utilities.readproperties import Readconfig
from Utilities.customlogger import LogGen
class Test_001:
    geturl=Readconfig.application_url()
    username=Readconfig.get_username()
    username1=Readconfig.get_username()
    surname=Readconfig.get_surname()
    email=Readconfig.get_email()
    number=Readconfig.get_phone()

    logger=LogGen.log_gen()

    def test_ll(self,setup):
        self.logger.info("********")
        self.driver=setup
        self.driver.get(self.geturl)
        self.a=Login(self.driver)

        # self.a.sigh_button_id()
        self.driver.close()

    def test_003(self,setup):
        self.logger.info("******")
        self.driver=setup
        self.driver.get(self.geturl)
        self.b=Login(self.driver)
        self.b.skip_sign()
        self.driver.close()

    def test_004(self,setup):
        import time
        self.driver=setup
        self.driver.get(self.geturl)
        self.c=Login(self.driver)
        self.c.skip_sign()
        self.c=Loginsh(self.driver)
        self.c.enter_first(self.username1)
        self.c.enter_last(self.surname)
        self.c.male1()
        self.c.email_enter(self.email)
        self.c.enter_phone(self.number)
        self.c.final()
        time.sleep(5)
        self.driver.close()



