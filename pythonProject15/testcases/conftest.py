import pytest
from selenium import webdriver
from pageobjects.homepage import Main
from utilities.readproperties import Readconfig
myurl=Readconfig.getapplicationURL()
@pytest.fixture()
def setup(browser,request):
    if browser=='chrome':
        request.cls.driver=webdriver.Chrome()
        request.cls.driver.get(myurl)
        print("Launching chrome browser.........")
        # yield
        # request.cls.quit()

    elif browser=='firefox':
        request.cls.driver = webdriver.Firefox()
        request.cls.driver.get(myurl)
        print("Launching firefox browser.........")
        # yield
        # request.cls.quit()
    else:
        request.cls.driver=webdriver.Chrome()
        request.cls.driver.get(myurl)
        # yield
        # request.cls.quit()
    yield
    request.cls.driver.quit()

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")





