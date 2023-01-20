import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
    elif browser=="firefox":
        driver=webdriver.Firefox()
    else:
        driver=webdriver.Chrome()
    return driver


def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')

###################pytest HTML##########
def pytest_configure(config):
    config._metadata['project name']='my personal project'
    config._metadata['module name']='jasmin'
    config._metadata['Tester']='jasmin the tester'








