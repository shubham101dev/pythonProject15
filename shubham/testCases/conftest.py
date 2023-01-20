import pytest
from selenium import webdriver
@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
        print("launching chrome browser")
    elif browser=="firefox":
        driver=webdriver.Firefox()
        print("launching firefox browser")
    else:
        driver=webdriver.Chrome()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


############pytest HTML report####################
def pytest_configure(config):
    config._metadata['project name']='no commerce'
    config._metadata['module name']='customers'
    config._metadata['Tester name']='shubham full stack tester'





