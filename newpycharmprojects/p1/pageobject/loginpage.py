from selenium.webdriver.common.by import By


class Login:
    text_box_username_xpath="//input[@id='email']"
    click_signin_xpath="//img[@id='enterimg']"
    click_webtable_xpath="//a[normalize-space()='WebTable']"

    def __init__(self,driver):
        self.driver=driver

    def set_username(self,username):
        self.driver.find_element(By.XPATH,self.text_box_username_xpath).send_keys(username)


    def click_login(self):
        self.driver.find_element(By.XPATH,self.click_signin_xpath).click()

    def click_on_webtable(self):
        self.driver.find_element(By.XPATH,self.click_webtable_xpath).click()


