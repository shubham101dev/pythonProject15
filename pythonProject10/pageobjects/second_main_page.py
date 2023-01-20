from selenium.webdriver.common.by import By


class My_Mainpage:
    demo_page_xpath="//a[normalize-space()='Demo Page']"
    Text_Input_Field_id="myTextInput"
    preText2_xpath="//textarea[@id='myTextarea']"




    def __init__(self,driver):
        self.driver=driver

    def click_on_demopage(self):
        self.driver.find_element(By.XPATH,self.demo_page_xpath).click()

    def box1(self,box1):
        self.driver.find_element(By.ID,self.Text_Input_Field_id).send_keys(box1)

    def box2(self,box2):
        self.driver.find_element(By.XPATH,self.preText2_xpath).send_keys(box2)








