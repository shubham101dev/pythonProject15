from selenium.webdriver.common.by import By


class Login:
    text_box_Xpath="//input[@id='email']"
    sigh_button_id="//img[@id='enterimg']"
    sign2_id="btn2"

    def __init__(self,driver):
        self.driver=driver

    def enter_username(self,username1):
        self.driver.find_element(By.XPATH,self.text_box_Xpath).send_keys(username1)

    def click_login(self):
        self.driver.find_element(By.ID,self.sigh_button_id).click()

    def skip_sign(self):
        self.driver.find_element(By.ID,self.sign2_id).click()






































