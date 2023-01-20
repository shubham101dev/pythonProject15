from selenium.webdriver.common.by import By


class Login:
    def __init__(self,driver):
        self.driver=driver
        self.textbox_username_xpath="//input[@id='Email']"
        self.textbox_password_xpath="//input[@id='Password']"
        self.button_login_xpath="//button[normalize-space()='Log in']"
        self.click="//a[normalize-space()='nopCommerce']"


    def input_username(self,username):
        c=self.driver.find_element(By.XPATH,self.textbox_username_xpath).clear()
        username=self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)

    def input_password(self,password):
        e=self.driver.find_element(By.XPATH,self.textbox_password_xpath).clear()
        password=self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)


    def button_login(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def button_click(self):
        self.driver.find_element(By.XPATH,self.click).text()


