from selenium.webdriver.common.by import By


class Login:
    button_viewaccount_xpath="//span[@id='acctBtnLabel']"
    button_signin_xpath="//a[normalize-space()='Sign-In']"
    textbox_username_xpath="//input[@id='sso_username']"
    textbox_password_xpath="//input[@id='ssopassword']"
    button_final_signin_xpath="//input[@id='signin_button']"

    def __init__(self,driver):
        self.driver=driver

    def click_on_viewaccount(self):
        self.driver.find_element(By.XPATH,self.button_viewaccount_xpath).click()

    def click_signin(self):
        self.driver.find_element(By.XPATH,self.button_signin_xpath).click()

    def set_username(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)

    def click_on_final_signin(self):
        self.driver.find_element(By.XPATH,self.button_final_signin_xpath).click()




