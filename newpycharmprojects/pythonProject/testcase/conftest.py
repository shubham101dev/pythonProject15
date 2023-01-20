import pytest
import time
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome or firefox")

@pytest.fixture
def get_browser(request):
    return request.config.getoption("--browser")

@pytest.fixture
def get_driver(request, get_browser):
    driver = None
    if get_browser == "chrome":
        driver = webdriver.Chrome()
    elif get_browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Invalid browser option: {get_browser}. Only chrome and firefox are supported.")
    driver.implicitly_wait(20)
    request.cls.driver = driver
    yield driver
    time.sleep(2)
    driver.quit()




