import pytest
import time
from selenium import webdriver
# browser="chrome"
#
# def pytest_addoption(parser):
#     parser.addoption("--browser",action="store",default="chrome")
#
# @pytest.fixture
# def getbrowser(request):
#     _browser=request.config.getoption("--browser")
#     return _browser
#
# @pytest.fixture
# def getdriver(request,getbrowser):
#     _driver=None
#     if getbrowser=="chrome":
#         _driver=webdriver.Chrome()
#     elif getbrowser=="firefox":
#         _driver=webdriver.Firefox()
#     _driver.implicitly_wait(20)
#     request.cls.driver=_driver
#     yield request.cls.driver
#     time.sleep(2)
#     request.cls.driver.quit()























@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    return driver
