from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://ultimateqa.com/automation")
driver.find_element(By.LINK_TEXT,"Courses").click()
driver.find_element(By.CSS_SELECTOR,"h3.card__name").click()
driver.back()
driver.find_element(By.PARTIAL_LINK_TEXT,"Complet").click()
driver.back()
driver.find_element(By.PARTIAL_LINK_TEXT,"Modern").click()
driver.find_element(By.LINK_TEXT,"Sign In").click()
# driver.find_element(By.CSS_SELECTOR,"a[href=/users/sign_up]").click()
driver.back()
driver.back()
driver.back()
driver.find_element(By.PARTIAL_LINK_TEXT,"Automation").click()
driver.find_element(By.CSS_SELECTOR,"li.et_pb_menu_page_id-213448").click()
driver.back()
driver.find_element(By.PARTIAL_LINK_TEXT,"Interactions").click()
driver.find_element(By.CSS_SELECTOR,"a.et_pb_button.et_pb_button_0.et_pb_bg_layout_light").click()
driver.find_element(By.CSS_SELECTOR,"input[id='subscribe-field-blog_subscription-2']").send_keys("shubham4121@gmail.com")
driver.find_element(By.CSS_SELECTOR,"button.wp-block-button__link").click()
driver.back()
driver.back()
driver.find_element(By.CSS_SELECTOR,"button.buttonClass").click()
driver.back()
driver.find_element(By.CSS_SELECTOR,"input#et_pb_contact_name_0").send_keys("shubham")
driver.find_element(By.CSS_SELECTOR,"input#et_pb_contact_email_0").send_keys("shubham4121@gmail.com")
driver.find_element(By.CSS_SELECTOR,"button[name='et_builder_submit_button']").click()
print(f"URL:{driver.current_url}")
currenturl=driver.current_url
expectedurl="https://ultimateqa.com/simple-html-elements-for-automation/"
if currenturl==expectedurl:
    print("url is match")
else:
    print("url not match")

# driver.find_element(By.CSS_SELECTOR,"select[xpath=1]").click()

# driver.find_element(By.LINK_TEXT,"2").click()





time.sleep(10)
driver.close()

