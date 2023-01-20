import pytest
from selenium import webdriver
from utilities.readproperties import Readconfig


@pytest.fixture()
def setup(browser,request):
    if browser=='chrome':
        request.cls.driver=webdriver.Chrome()
        request.cls.driver.get(Readconfig.getapplicationURL())
        print("Launching chrome browser.........")
        # yield
        # request.cls.quit()

    elif browser=='firefox':
        request.cls.driver = webdriver.Firefox()
        request.cls.driver.get(Readconfig.getapplicationURL())
        print("Launching firefox browser.........")
        # yield
        # request.cls.quit()
    else:
        request.cls.driver=webdriver.Chrome()
        request.cls.driver.get(Readconfig.getapplicationURL())
        # yield
        # request.cls.quit()
    yield
    request.cls.driver.quit()

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")
