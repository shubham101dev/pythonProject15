from selenium.webdriver.common.by import By

from utilities.readproperties import Readconfig
class AutoMation:
    geturl=Readconfig.getapplicationURL()

    def __init__(self,driver):
        self.driver=driver

    def open_main_url(self):
        return self.driver.find_element(By.XPATH,self.geturl)

    def click_on_radio1(self):
        self.driver.find_element(By.XPATH,(Readconfig.radiobutton1xpath())).click()

    def click_on_radio2(self):
        self.driver.find_element(By.XPATH,(Readconfig.radiobutton2xpath())).click()

    def click_on_radio3(self):
        self.driver.find_element(By.XPATH,(Readconfig.radiobutton3xpath())).click()

    def click_on_option1(self):
        self.driver.find_element(By.XPATH,Readconfig.checkbox1()).click()

    def click_on_option2(self):
        self.driver.find_element(By.XPATH, Readconfig.checkbox2()).click()

    def click_on_option3(self):
        self.driver.find_element(By.XPATH,Readconfig.checkbox3()).click()







