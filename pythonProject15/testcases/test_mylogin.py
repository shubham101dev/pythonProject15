import time
from selenium.webdriver import ActionChains
import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from pageobjects.homepage import Main
from utilities.readproperties import Readconfig
from utilities.customlogger import Logclass
@pytest.mark.usefixtures('setup')
class Test_010:
    geturl=Readconfig.getapplicationURL()
    username=Readconfig.getusername()
    password=Readconfig.getpassword()

    log=Logclass.getthelog()
    def test1(self):

        act_title=self.driver.title
        if act_title=="Your Store":
            assert True
            self.driver.save_screenshot(".\\screenshots\\" + "any1.png")
            self.log.info("*******title is match**********")
        else:
            self.log.info("*******title is not  match**********")
            assert False

    def test2(self):
        self.log.info("*******open URL**********")
        self.a=Main(self.driver)
        self.a.click_on_myaccount_and_login(self.username,self.password)
        self.driver.save_screenshot(".\\screenshots\\" + "any.png")
        ActionChains(self.driver).move_to_element(self.a.hover_desktop()).click().perform()
        ActionChains(self.driver).move_to_element(self.a.hover_componets()).click().perform()
        ActionChains(self.driver).move_to_element(self.a.hover_mp3player()).click().perform()
        ActionChains(self.driver).move_to_element(self.a.hover_componets()).click().perform()
        self.a.click_on_tablet()
        self.a.samsung_galaxy_add()
        self.a.click_on_homepage()
        print(len(self.a.sliders()))

        time.sleep(5)


