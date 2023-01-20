from selenium.webdriver.common.by import By


class Main:
    button_myaccount_xpath="//a[@title='My Account']"
    button_login_link_text="Login"
    textbox_username_xpath="//input[@id='input-email' and @name='email']"
    textbox_password_xpath="//input[@id='input-password' and @placeholder='Password']"
    button_login_xpath="//input[@type='submit' and @value='Login']"

    def __init__(self,driver):
        self.driver=driver
        self.desktop_link_text= "Desktops"
    def click_on_myaccount_and_login(self,username,password):
        self.driver.find_element(By.XPATH,self.button_myaccount_xpath).click()
        self.driver.find_element(By.LINK_TEXT, self.button_login_link_text).click()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def hover_desktop(self):
        return self.driver.find_element(By.LINK_TEXT,self.desktop_link_text)

    def hover_Laptopandnotebook(self):
        return self.driver.find_element(By.LINK_TEXT,"Laptops & Notebooks")

    def hover_componets(self):
        return self.driver.find_element(By.LINK_TEXT,"Components")

    def hover_mp3player(self):
        return self.driver.find_element(By.LINK_TEXT,"MP3 Players")

    def click_on_tablet(self):
        self.driver.find_element(By.LINK_TEXT,"Tablets").click()

    def samsung_galaxy_add(self):
        self.driver.find_element(By.XPATH,"(//button[@type='button'])[9]").click()
        #//button[@type='button' and contains(@onclick,'cart.add')]#

    def click_on_homepage(self):
        self.driver.find_element(By.XPATH,"//i[@class='fa fa-home']").click()

    def sliders(self):
        return self.driver.find_elements(By.XPATH,"//div[@class='swiper-button-prev']")


