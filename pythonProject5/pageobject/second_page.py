from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Second():
    def __init__(self,driver):
        self.driver=driver
    def click_on_addcart(self):
        self.driver.find_element(By.XPATH,"//app-card[1]//div[1]//div[2]//button[1]").click()


    def checkout(self):
        return self.driver.find_element(By.XPATH,"//div[@id='navbarResponsive']//a").text

    # def scroll_down(self):
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(to_element=self.click_on_addcart()).move_by_offset(0, 500).perform()

    def scroll_down(driver, pixels):
        driver.execute_script("window.scrollBy(0, {})".format(pixels))
