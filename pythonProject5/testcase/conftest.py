import pytest
from utilities.readproperties import Readconfig
from selenium import webdriver
driver=None
@pytest.fixture()
def setup(request):
    global driver
    request.cls.driver=webdriver.Chrome()
    request.cls.driver.get(Readconfig.getapplicationURL())
    yield
    request.cls.driver.quit()

