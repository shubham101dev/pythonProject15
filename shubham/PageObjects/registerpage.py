from selenium.webdriver.common.by import By


class Loginsh:


        first_name_xpath="//input[@placeholder='First Name']"
        last_name_xpath="//input[@placeholder='Last Name']"
        male_xpath="//input[@value='Male']"
        submit_xpath="//button[@id='submitbtn']"
        email_xpath="//input[@ng-model='EmailAdress']"
        phone_xpath="//input[@type='tel']"

        def __init__(self,driver):
            self.driver=driver

        def enter_first(self,username):
            self.driver.find_element(By.XPATH,self.first_name_xpath).send_keys(username)

        def enter_last(self,surname):
            self.driver.find_element(By.XPATH,self.last_name_xpath).send_keys(surname)

        def male1(self):
            self.driver.find_element(By.XPATH,self.male_xpath).click()

        def final(self):
            self.driver.find_element(By.XPATH,self.submit_xpath).click()

        def email_enter(self,email):
            self.driver.find_element(By.XPATH,self.email_xpath).send_keys(email)

        def enter_phone(self,number):
            self.driver.find_element(By.XPATH,self.phone_xpath).send_keys(number)




