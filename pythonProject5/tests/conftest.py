import pytest
from utilities.readproperties import Readconfig
from selenium import webdriver
driver=None
def scroll_down(driver, pixels):
    driver.execute_script("window.scrollBy(0,3000)".format(pixels))
@pytest.fixture()
def setup(request):
    global driver
    request.cls.driver=webdriver.Chrome()
    request.cls.driver.get(Readconfig.getapplicationURL())
    yield
    request.cls.driver.quit()

