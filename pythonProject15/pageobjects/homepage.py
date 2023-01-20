from selenium.webdriver.common.by import By


class Main:
    button_myaccount_xpath="//a[@title='My Account']"
    button_login_link_text="Login"
    textbox_username_xpath="//input[@id='input-email' and @name='email']"
    textbox_password_xpath="//input[@id='input-password' and @placeholder='Password']"
    button_login_xpath="//input[@type='submit' and @value='Login']"

    def __init__(self,driver):
        self.driver=driver

    def click_on_myaccount_and_login(self,username,password):
        self.driver.find_element(By.XPATH,self.button_myaccount_xpath).click()
        self.driver.find_element(By.LINK_TEXT, self.button_login_link_text).click()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()



