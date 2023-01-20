from selenium.webdriver.common.by import By


class Login:
    textbox_username_xpath="//input[@id='username']"
    textbox_password_xpath="//input[@id='password']"
    button_login_xpath="//button[@id='submit']"
    button2_practice_text="Practice"

    def __init__(self,driver):
        self.driver=driver

    def set_username(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def click2_practice(self):
        self.driver.find_element(By.LINK_TEXT,self.button2_practice_text).click()




