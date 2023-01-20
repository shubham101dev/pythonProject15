from PageObjects.login_page import Login
import time

import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class Testlogin:

    def test__001(self):
        lg=Login(self.driver)
        lg.input_username("admin@yourstore.com")
        lg.input_password("admin")
        lg.button_login()


    def test__002(self):
        lg=Login(self.driver)
        lg.input_username("shubham")
        lg.input_password("abc123")
        lg.button_login()

    def test__003(self):
        p=Login(self.driver)
        p.input_username("admin@yourstore.com")
        p.input_password("admin")
        p.button_login()
        p.click()





























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








