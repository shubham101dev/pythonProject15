import pytest
from selenium import webdriver
driver=None
@pytest.fixture
def setup(request):
    global driver
    request.cls.driver=webdriver.Chrome()
    request.cls.driver.get("https://practicetestautomation.com/practice-test-login/")
    yield
    reques.cls.driver.quit()

