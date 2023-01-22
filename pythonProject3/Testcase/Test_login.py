from PageObjects.login_page import Login
import time
from utilities.customlogger import Logclass
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class Testlogin():
    logger=Logclass.getLogger()
    @pytest.mark.parameterize("username,password",[("admin@yourstore.com","admin"),("shubham","admin"),("admin@yourstore.com","ad12")])
    def test__001(self,username,password):
        self.logger.info("***********testcase001")
        lg=Login(self.driver)
        lg.input_username(username)
        lg.input_password(password)
        lg.button_login()
        self.logger.info("****login successful***")

































    # def test__002(self):
    #
    #     self.driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
    #     self.driver.quit()
    #
    # def test__003(self):
    #
    #     self.driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
    #     act_title=self.driver.title
    #     expected_title="Dashboard / nopCommerce administration"
    #     if act_title==expected_title:
    #         print("title is match")
    #     else:
    #         print("title is not match")
    #     self.driver.quit()








