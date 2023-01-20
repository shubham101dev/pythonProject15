# from select import select
# from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Login1:
    mr_button_male_xpath="//input[@id='id_gender1' and @name='title']"
    password_xpath_s="//input[@id='password']"
    drop_down_day_id="days"
    drop_down_month_id="months"

    def __init__(self,driver):
        self.driver=driver

    def select_male(self):
        self.driver.find_element(By.XPATH,self.mr_button_male_xpath).click()

    def insert_password(self,password2):
        self.driver.find_element(By.XPATH,self.password_xpath_s).send_keys(password2)

    def drop_day_select(self):
        dropdown=self.driver.find_element(By.ID,self.drop_down_day_id)
        return dropdown

    def drop_month_select(self):
        d1=self.driver.find_element(By.XPATH,"//select[@id='months']")
        return d1

    def drop_year_select(self):
        d2=self.driver.find_element(By.XPATH,"//select[@id='years']")
        return d2


    def two_check_box(self):
        self.driver.find_element(By.XPATH,"//input[@id='newsletter']").click()
        self.driver.find_element(By.XPATH,"//input[@id='optin']").click()

    def few_down(self):
        ele = self.driver.find_element(By.XPATH,"//button[normalize-space()='Create Account']")
        self.driver.execute_script("arguments[0].scrollIntoView()", ele)
        return ele







