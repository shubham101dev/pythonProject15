from selenium.webdriver.common.by import By


class Login:
    textbox_username_xpath = "//input[@id='username']"
    textbox_password_xpath = "//input[@id='password']"
    textbox_code_xpath = "//input[@id='totpcode']"
    button_sign_up_xpath = "//a[@id='log-in']"

    def __init__(self,driver):
        self.driver=driver

    def set_username(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def set_code(self, code):
        self.driver.find_element(By.XPATH, self.textbox_code_xpath).send_keys(code)

    def button_sign_up(self):
        self.driver.find_element(By.XPATH, self.button_sign_up_xpath).click()
